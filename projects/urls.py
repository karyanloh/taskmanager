from django.urls import path
from .views import list_projects, show_project, create_project

urlpatterns = [
    path("projects/", list_projects, name="list_projects"),
    path("projects/<int:id>/", show_project, name="show_project"),
    path("projects/create/", create_project, name="create_project"),
]
