from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'myapp/index.html', {'todo_items':todo_items})

@csrf_exempt
def add_todo(request):
    current_time = timezone.now()
    content = request.POST.get('content')
    Todo.objects.create(added_date=current_time, text=content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.all().filter(pk = todo_id).delete()
    return HttpResponseRedirect("/")
