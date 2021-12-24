from django.shortcuts import render, redirect, get_object_or_404,redirect
from .models import Question, Choice  #, Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .forms import  CreateUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
  questions = Question.objects.all()
  return render(request, 'home.html', {'questions': questions})

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
    id_number = request.POST['user_id_number']
    inputvalue = request.POST['choice']

    if Choice.objects.filter(userid=id_number).exists():
      messages.error(request, 'User: ' + id_number + ' has already voted!')
      return redirect('index')
    else:
      selected_options = options.get(id=inputvalue)
      selected_options.userid = id_number
      selected_options.vote +=1
      selected_options.save()
   return render(request, 'result.html', {'question':question, 'options': options})



# def final(request, pk):
#    question = Question.objects.get(id=pk)
#    options = question.choices.all()

#    return render(request, 'finalres.html', {'question':question, 'options': options})


def final(request,pk):
  question = Question.objects.get(id=pk)
  options = question.choices.all()

  
  
  return render(request, 'finalres.html', {'question':question, 'options':options})


# @login_required

# def result(request,pk):
#    question = Question.objects.get(id=pk)
#    options = question.choices.all()
#    current_user = request.user
#    print('____')
#    print(current_user.id)
#    user = Account.objects.get(user=current_user.id)
#    print(type(user.status))
#    #user = User.objects.get(id=current_user.id)
#    #print(user)
#    print('_______')
#    if user.status == True:
#      print('CANNNOT VOTE')
#      return redirect('index')

#    else:
#      if request.method == 'POST':
       
#           inputvalue = request.POST['choice']
#           selected_options = options.get(id=inputvalue)
#           selected_options.vote +=1
#           selected_options.save()
          

#    return render(request, 'result.html', {'question':question, 'options': options})


