from django.core.mail import EmailMessage
from django.shortcuts import render

from django.shortcuts import redirect, render
from django.http import *
from .models import *  
from .forms import TraditionForm
from django.core.mail import send_mail
# Create your views here.

def hello(request , name):
    if name == u'Waldo':
        raise Http404("Where's Waldo?")
    return HttpResponse(u'Hello {name}!'.format(name=name))
def main (request):

    return render(request,'main.html')

def  products (request) :
 post = Types.objects.all()
 return render(request,'products.html', {'posts' : post})
 
def  prices (request) :
  facts = Facts.objects.order_by('importantyears')
  return render(request,'prices.html',{'facts' : facts})

def  login (request) :
  parks = Nationalparks.objects.all()
  return render(request, 'login.html', {'parks' : parks})

def insert(request):
    form = TraditionForm()
    if request.method == 'POST':
        form = TraditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'insert.html', context)
def send_message(request):
      email = EmailMessage("sasa",
            'Im',
             "200103514@stu.sdu.edu.kz",
             ["200103213@stu.sdu.edu.kz","baizhumanali@gmail.com"]
             )
      email.attach_file(r"D:\SPRINGSEM2021-2022\WEBLABS\labka5\project1\qurt\tests\Astana.jpg")    
      email.send(fail_silently = False)
      return render(request,'success.html')
