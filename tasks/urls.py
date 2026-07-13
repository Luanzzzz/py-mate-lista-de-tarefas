from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("tasks/add/", views.task_create, name="task_create"),
    path("tasks/<int:pk>/update/", views.task_update, name="task_update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task_delete"),
    path("tasks/<int:pk>/toggle/", views.task_toggle, name="task_toggle"),
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/add/", views.tag_create, name="tag_create"),
    path("tags/<int:pk>/update/", views.tag_update, name="tag_update"),
    path("tags/<int:pk>/delete/", views.tag_delete, name="tag_delete"),
]
