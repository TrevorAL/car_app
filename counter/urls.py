from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Main home page route
    path("home/", views.home, name="home"),  # Additional route to home, if needed
    path("about/", views.about, name="about"),  # About page route
    # Detail view for cars, expects 'make', 'model', and 'year' as parameters
    re_path(
        r"^car/(?P<make>[^/]+)/(?P<model>.+)/(?P<year>[0-9]+)/$",
        views.car_detail,
        name="car_detail",
    ),
    path(
        "back_to_list/", views.back_to_list, name="back_to_list"
    ),  # Route for back to list button
]
