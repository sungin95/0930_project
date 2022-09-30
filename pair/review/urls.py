from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("create", views.create, name="create"),
    path("detail/<int:pk_>", views.detail, name="detail"),
    path("detail/edit/<int:pk_>", views.edit, name="edit"),
    path("detail/edit/update/<int:pk_>", views.update, name="update"),
    path("detail/edit/delete/<int:pk_>", views.delete, name="delete"),
]
