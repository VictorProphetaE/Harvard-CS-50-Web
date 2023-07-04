document.addEventListener('DOMContentLoaded', function() {
    let button = document.querySelectorAll(".like-button");

    button.forEach((element) => {
      likeelement(element);
    });
});

function likeelement(element){
    element.addEventListener("click", function() {
    id = element.getAttribute("idpost");
    count = document.querySelector(`#countlike${id}`);

    form = new FormData();
    form.append("id", id);
    fetch("/postlike/", {
        method: "POST",
        body: form,
    })
    .then((response) => response.json())
    .then(async (response) => {
      if (response.status == 201) {
      like = response.likes ? "Liked" : "Unliked";
      if(like === "Liked"){
        if ($(this).hasClass("Unliked")) {
          $(this).removeClass("Unliked");
          $(this).addClass("Liked");
          }
      }else{
        if ($(this).hasClass("Liked")) {
          $(this).removeClass("Liked");
          $(this).addClass("Unliked");
          }
      }
      count.innerHTML = response.counte;
      }
    }).catch(error =>console.log(error));
  });
}

function edit(id) {
    // Show compose view and hide other views
    document.querySelector(`#compose-body${id}`).style.display = 'block';
    document.querySelector(`#save-edit${id}`).style.display = 'block';
    document.querySelector(`#compose-body${id}`).value = '';
    document.querySelector(`#editbutton${id}`).style.display = 'none';
    var url = '/edit/'+ id
    document.querySelector(`#save-edit${id}`).addEventListener('click', () => {fetch(url, {
        method: 'POST',
        body: JSON.stringify({
            post:  document.querySelector(`#compose-body${id}`).value,
        }),
        })

        document.querySelector(`#post${id}`).innerHTML =  document.querySelector(`#compose-body${id}`).value;
        document.querySelector(`#compose-body${id}`).style.display = 'none';
        document.querySelector(`#save-edit${id}`).style.display = 'none';  
        document.querySelector(`#editbutton${id}`).style.display = 'block';
    });
}