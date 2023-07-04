from django import forms
from django.shortcuts import render, redirect
from markdown2 import Markdown
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

import random

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="",widget=forms.TextInput(
            attrs={"placeholder": "Title"}))
    text = forms.CharField(label="",widget=forms.Textarea(attrs={
                "placeholder": "Content (markdown)"}))
class Edition(forms.Form):
    text = forms.CharField(label="",widget=forms.Textarea(attrs={
                "placeholder": "Content (markdown)"}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_cont = util.get_entry(title)
    if title not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
        "title": title
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": Markdown().convert(entry_cont)
        })

def search(request):
    title = request.GET.get("q", "")
    cont = 0
    name_related = []
    for entry_name in util.list_entries():
        if title.lower() in entry_name.lower():
            name_related.append(entry_name)
            cont += 1
    if cont > 1:
        return render(request, "encyclopedia/search.html", {
        "title": title,
        "name_related": name_related,
        })
    elif cont == 1:
        return redirect("entry", name_related[0])
    else:
        return render(request,"encyclopedia/search.html",
            {"name_related": "", "title": title},
        )

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html", {
          "new_entry": NewEntryForm() })
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            text = form.cleaned_data.get("text")
            forfinal = "# "+title
            finaltext = "\n\n".join((forfinal,text))
            if util.get_entry(title):
                messages.add_message(request, messages.WARNING,
                    message=f'Entry "{title}" already exists'
                )
            else:
                util.save_entry(title, finaltext)
                messages.success(request, f'New page "{title}" created successfully!')
                return redirect("entry", title)
        else:
            messages.add_message(
                request, messages.WARNING, message="Invalid request form"
            )
    return render(request,"encyclopedia/newpage.html",{"form": form})

def edit(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        return render(request,"encyclopedia/edit.html",
            {"title": title, "form": Edition(initial={"text":content})},
        )
    if request.method == "POST":
        form = Edition(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            removingspace = text.replace("\n", "")
            util.save_entry(title, removingspace)
            messages.success(request, f'Entry "{title}" updated successfully!')
            return redirect("entry", title)

def random_ent(request):
    title = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("entry", args=[title]))

def page_not_found(request, *args):
    return render(request, "404.html", {})