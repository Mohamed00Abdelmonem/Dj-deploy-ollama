from django.shortcuts import render, redirect
from .models import Task
from .serilzer import TaskListSerilize
from rest_framework import generics



from django.shortcuts import render
from langchain_community.llms import Ollama
# Create your views here.


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerilize


class Taskdetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerilize






from django.shortcuts import render, redirect
from langchain_community.llms import Ollama

def generate_ollama3_text(request):
    generated_text = None
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')  
        llm = Ollama(model="llama3")
        generated_text = llm.invoke(input_text)

    return render(request, 'ollama3_generator.html', {'generated_text': generated_text})
