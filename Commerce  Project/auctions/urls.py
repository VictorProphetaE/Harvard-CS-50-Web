from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing/", views.new_listing, name="new_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addcomment/<int:listing_id>", views.addcomment, name="addcomment"),
    path("listing_page/<int:listing_id>", views.listing_page, name="listing_page"),
    path("endlisting/<int:listing_id>", views.endlisting, name="endlisting"),
    path("categories/<str:category>", views.categories, name="categories"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)