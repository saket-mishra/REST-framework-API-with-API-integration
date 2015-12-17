from django.shortcuts import render
import json
from django import template
import requests
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django import template
from patients.models import Person
from datetime import date, timedelta
from datetime import datetime

def cities(request):
    data = requests.get('http://djangoapi.herokuapp.com/patients/cities/').json()
    context = RequestContext(request, {
        'cities': data['results'],'count': data['count'],
    }) 
    return render_to_response('taskmanager/cities.html', context)

def personlist(request, id):
    data = requests.get('http://djangoapi.herokuapp.com/patients/cities/' + id + '/persons/').json()
    context = RequestContext(request, {
        'persons': data['results'],'count': data['count'],'city': data['results'][0]['id'],'city_name': data['results'][0]['city']['city_name'],
    })
    
    return render_to_response('taskmanager/persons.html', context)

def person_details(request, id):
    data = requests.get('http://djangoapi.herokuapp.com/patients/person/' + id).json()
    context = RequestContext(request, {
        'city': data['city'],'name': data['name'],'title': data['title'],'address': data['address'],'test_set': data['test_set'],
    })
    return render_to_response('taskmanager/person_detail.html', context)


def persons_by_month(request):
    today = date.today()
    p = Person.objects.all()
    s=[]
    for per in p:
        this_m = per.test_set.filter(date__month=today.month,date__year=today.year)
        s.extend(this_m)
    count=0
    for i in s:
        count+=1
    context = RequestContext(request, {
     'test_list': s,'count':count,
    })
    return render_to_response('taskmanager/person_date_month.html', context)

def persons_by_week(request):
    today = date.today()
    f_this = date.today() - timedelta(today.weekday())
    e_this = f_this + timedelta(days=6)
    f_that = f_this-timedelta(days=6)
    e_that = f_this-timedelta(days=1)
    p = Person.objects.all()
    s_this=[]
    s_that=[]
    for per in p:
        this_m = per.test_set.filter(date__range=[f_this, e_this])
        s_this.extend(this_m)
    for per in p:
        that_m = per.test_set.filter(date__range=[f_that, e_that])
        s_that.extend(that_m)
    count_this=0
    count_that=0
    for i in s_this:
        count_this +=1
    for j in s_that:
        count_that +=1
    context = RequestContext(request, {
     'this_test_list': s_this,'that_test_list': s_that,'count_this':count_this,'count_that':count_that,
    })
    return render_to_response('taskmanager/person_date_weekly.html', context)


def persons_by_day(request):
    today = datetime.now()
    min = today - timedelta(hours=12)
    max = today + timedelta(hours=12)
    p = Person.objects.all()
    s=[]
    for per in p:
        this = per.test_set.filter(date__range=(min,max))
        s.extend(this)
    count=0
    for i in s:
        count+=1
    context = RequestContext(request, {
     'test_list': s,'count':count,
    })
    return render_to_response('taskmanager/person_date_daily.html', context)
 

