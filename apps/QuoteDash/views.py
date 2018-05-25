from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'htmlQuoteDash/index.html')

def register(request):
  errors = User.objects.Validator(request.POST)
  if len(errors):
    for key, value in errors.items():
      messages.error(request, value)
    return redirect('/', value)
  else:
    hashPass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'], password=hashPass)
    return redirect ("/success")

def quotedash(request):
  
  context = {
      'Quotes' : Quote.objects.all()
        }
  return render (request, 'htmlQuoteDash/quote.html', context)

def validate_login(request):
  if len(User.objects.filter(email=request.POST['email_log']))!=0:
    a = User.objects.get(email=request.POST['email_log'])
    request.session['id'] = a.id
    # print("user id........from login", request.session['id'])
    request.session['first_name'] = a.first_name
    request.session['last_name'] = a.last_name
    print(request.session['first_name'])
    # context = { 
    #   'first_name' : a.first_name,
    #   'id' : a.id
    #  }
    if bcrypt.checkpw(request.POST['password_log'].encode(), a.password.encode()):
      queryQ = Quote.objects.all()
      # context = {
      # 'Quotes' : Quote.objects.all()
      #   }
      return redirect("/quotedash")
    else:
      context ={
        'loginerror' : 'Password do not match' 
      }
      return render(request, 'htmlQuoteDash/index.html', context)
  else:
    context ={
        'loginerror' : 'The email is not registered yet' 
      }
    return render(request, 'htmlQuoteDash/index.html', context)

def edit(request, id):
  tagUser = User.objects.get(id=id)
  context = {
    "userID" : tagUser }
  return render(request, 'htmlQuoteDash/edit.html', context)

def destroy(request, idu, idq):
  dstry = Quote.objects.get(id=id)
  dstry.delete()
  return render(request, 'htmlQuoteDash/edit.html')

def editUser(request):
  return render(request, 'htmlQuoteDash/edit.html', user = User.objects.get(id=id))

def update(request, id): # lesson learn
  errors_update = User.objects.UpdateValidator(request.POST)
  if len(errors_update):
    for key, value in errors_update.items():
      messages.error(request, value)
    return render(request, 'htmlQuoteDash/edit.html')
  if len(User.objects.filter(email = request.POST['email']))!= 0:
    context ={
      'email' : "email address already exist in database",
      'UserID.first_name' : request.POST['first_name'],
      'UserID.last_name' : request.POST['last_name'],
      'UserID.email' : request.POST['email']
    }
    return render(request, 'htmlQuoteDash/edit.html', context)
  else:
    i = User.objects.get(id=id)
    i.first_name = request.POST['first_name']
    i.last_name = request.POST['last_name']
    i.email = request.POST['email']
    i.save()
    return render (request, 'htmlQuoteDash/quote.html')

def quote(request,id):
  userInfo = User.objects.get(id = id)
  context = { 
    'first_name' : userInfo.first_name,
    'id' : id
    }
  return render(request, 'htmlQuoteDash/quote.html', context)

def addQuote(request):
  errors_quote = Quote.objects.QuoteValidator(request.POST)
  
  if len(errors_quote):
    for key, value in errors_quote.items():
      messages.error(request, value)
    return render (request, 'htmlQuoteDash/quote.html')
  else:
    person = User.objects.get(id = request.session['id'])
    Quote.objects.create(author = request.POST['author'], quote_text = request.POST['quote_text'], posted_by = person)
    context ={
      'Quotes' : Quote.objects.all()
    }
    return render (request, 'htmlQuoteDash/quote.html', context)

def likes(request,idq):
  print("quote id.......", idq)
  print("user id.......", request.session['id'])
  Quote.objects.get(id = idq).likes_by.add(User.objects.get(id=request.session['id']))
  q = Quote.objects.get(id=idq)

  print(q.likes_by.count())
  return redirect("/quotedash")

def logout(request):

  request.session.clear()
  return redirect("/")

def userQuotes (request, id):
  usr = User.objects.get(id = id)
  quo = Quote.objects.filter(posted_by = usr)
  context = {
    'userQuotes' : quo,
    'user' : usr,
    'id' : id
  }
  return render(request, 'htmlQuoteDash/showQuotes.html', context)