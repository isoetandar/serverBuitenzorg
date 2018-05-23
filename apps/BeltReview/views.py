from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'htmlLoginRegistration/index.html')

def register(request):
  errors = User.objects.Validator(request.POST)
  if len(errors):
    for key, value in errors.items():
      messages.error(request, value)
    return redirect('/', value)
  else:
    hashPass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'], password=hashPass)
    return render (request, 'htmlLoginRegistration/success.html')

def validate_login(request):
  if len(User.objects.filter(email=request.POST['email_log']))!=0:
    a = User.objects.get(email=request.POST['email_log'])
    if bcrypt.checkpw(request.POST['password_log'].encode(), a.password.encode()):
      return render(request, 'htmlLoginRegistration/success.html')
    else:
      print("checkpoint#14")
      context ={
        'loginerror' : 'Password do not match' 
      }
      return render(request, 'htmlLoginRegistration/index.html', context)
  else:
    print("checkpoint#11")
    context ={
        'loginerror' : 'The email is not registered yet' 
      }
    # return HttpResponse(request, )
    return render(request, 'htmlLoginRegistration/index.html', context)