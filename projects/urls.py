from django.urls import path
from .views import list_projects

urlpatterns = [
    path("projects/", list_projects, name="list_projects"),
]
