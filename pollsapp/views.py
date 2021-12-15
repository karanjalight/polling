from django.shortcuts import render
from .models import Question, Choice

def index(request):
  questions = Question.objects.all()
  return render(request, 'index.html', {'questions': questions})


def vote(request,pk):
  question = Question.objects.get(id=pk)
  options = question.choices.all()
  

  # if request.method == 'POST':
  #   inputvalue = request.POST['choice']
  #   selected_options = options.get(id=inputvalue)
  #   selected_options.vote +=1
  #   selected_options.save()
  if request.method == 'POST':
    inputvalue = request.POST['choice']
    selected_options = options.get(id=inputvalue)
    selected_options.vote +=1
    selected_options.save() 


  return render(request, 'vote.html', {'question':question, 'options':options})


def result(request,pk):
   question = Question.objects.get(id=pk)
   options = question.choices.all()
   if request.method == 'POST':
    inputvalue = request.POST['choice']
    selected_options = options.get(id=inputvalue)
    selected_options.vote +=1
    selected_options.save()
   return render(request, 'result.html', {'question':question, 'options': options})


