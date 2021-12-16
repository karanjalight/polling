from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .forms import  CreateUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User



def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
  questions = Question.objects.all()
  return render(request, 'index.html', {'questions': questions})

@login_required
def vote(request,pk):
  question = Question.objects.get(id=pk)
  options = question.choices.all()
  
  return render(request, 'vote.html', {'question':question, 'options':options})

  

@login_required

def result(request,pk):
   question = Question.objects.get(id=pk)
   options = question.choices.all()
   if request.method == 'POST':
    inputvalue = request.POST['choice']
    selected_options = options.get(id=inputvalue)
    selected_options.vote +=1
    selected_options.save()
   return render(request, 'result.html', {'question':question, 'options': options})


