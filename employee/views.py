from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import BlogPost, Employee

def index(request):
  myEmployees = Employee.objects.all().values()
  # myEmployees = Employee.objects.all().order_by('title')
  # myEmployees = Employee.objects.all().values_list('title')
  # myEmployees = Employee.objects.filter(title='Team') | Employee.objects.filter(title='CEO') # select * from Employee where title = 'Team'
  # myEmployees = Employee.objects.filter(title__startswith = 'C') 
  template = loader.get_template('employee/index.html')
  context = {
    'myEmployees': myEmployees
  }
  return HttpResponse(template.render(context, request))
 
def create(request):
  template = loader.get_template('employee/create.html')
  return HttpResponse(template.render({},request))

def createData(request):
  data1 = request.POST['name']
  data2 = request.POST['title']
  newEmployee = Employee(name=data1, title=data2)
  newEmployee.save()
  return HttpResponseRedirect(reverse('employee'))

def delete(request, id):
  deleteEmployee = Employee.objects.get(id=id)
  deleteEmployee.delete()
  return HttpResponseRedirect(reverse('employee'))

def update(request, id):
  updateEmployee = Employee.objects.get(id=id)
  template = loader.get_template('employee/update.html')
  context = {
    'Employee': updateEmployee
  }
  return HttpResponse(template.render(context,request))


def updateData(request, id):
  data1 = request.POST['name']
  data2 = request.POST['title']
  updateEmployee = Employee.objects.get(id=id)
  updateEmployee.name = data1
  updateEmployee.title = data2
  updateEmployee.save()
  return HttpResponseRedirect(reverse('employee'))


def blog(request):
  posts = BlogPost.objects.all()
  featuredPosts = BlogPost.objects.filter(featured = True)
  template = loader.get_template('employee/blog.html')
  context = {
    'posts': posts ,
    'featuredPosts': featuredPosts
  }
  return HttpResponse(template.render(context, request))

def blogDetail(request, id):
  blogdetail = BlogPost.objects.get(id=id)
  template = loader.get_template('employee/blogDetail.html')
  context = {
    'post': blogdetail
  }
  return HttpResponse(template.render(context,request))