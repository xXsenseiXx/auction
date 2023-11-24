from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("list_item", views.create_listing, name="list_item"),
    path("detail/<int:listing_id>", views.listing_detail, name="listing_detail"),
    path("watchlist", views.watch_list, name="watch_list"),
    path("categorys", views.categorys, name="categorys"),
    path("categorys/<str:cate>", views.each_category, name="each_category")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)