from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_student, name="add"),
    path("all", views.all_students, name="all"),
    path("update/<str:slug>", views.update_student, name="update"),
    path("delete/<str:reg>", views.delete_student, name="delete"),
    path("search/<str:reg>", views.search_student, name="search"),
    
]
