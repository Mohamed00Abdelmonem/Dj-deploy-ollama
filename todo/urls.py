from django.urls import path
from .views import TaskListView, Taskdetailview, generate_ollama3_text


urlpatterns = [

    path("task/", TaskListView.as_view()),
    path("task/<int:pk>", Taskdetailview.as_view()),

    path('generate-ollama3/', generate_ollama3_text, name='generate_ollama3'),
    # Add other URL patterns as needed
]
