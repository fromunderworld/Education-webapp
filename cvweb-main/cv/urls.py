from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("comment/<str:comment>/", views.leaveacomment, name="leaveacomment"),
]