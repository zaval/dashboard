from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
# Create your views here.
from panel.models import ParseTask


@login_required()
def index(request):

    try:
        parseTasks = ParseTask.objects.filter(user=request.user)
    except:
        parseTasks = []

    tasks = []

    for task in parseTasks:
        data ={
            'name': task.name,
        }
        data.update(task.result)
        rendered = render_to_string('panel/{}.html'.format(task.service), data)
        tasks.append(rendered)

    return render(request, 'panel/index.html', {'tasks': tasks})


def login_view(request):

    if request.method == 'POST' and request.POST.__contains__('username') and request.POST.__contains__('password'):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('/')

    return render(request, 'panel/login.html')


def logout_view(request):

    logout(request)
    return redirect('/')
