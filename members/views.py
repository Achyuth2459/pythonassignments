from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from members.models import Member


def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'my_members': my_members,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    my_members = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_members': my_members,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    # mydata = Member.objects.all()
    #mydata = Member.objects.all().values()
    #mydata = Member.objects.values_list('firstname') # specific column
    mydata = Member.objects.filter(firstname='Achyuth').values()
    mydata= Member.objects.filter(firstname='Achyuth',lastname='Refsnes').values()
    mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    mydata = Member.objects.filter(firstname__startswith='A').values()

    #sorting query sets - for descending
    mydata = Member.objects.all().order_by('-firstname').values()
    mydata = Member.objects.all().order_by('lastname', '-id').values()
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context,request))
