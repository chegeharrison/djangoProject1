from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from classschedule.models import PersonalData


# Create your views here.
def kusoma(request):
    return render(request, template_name='website/welcome.html',
                  context={'studentnumbers':PersonalData.objects.count})

def datetoday(request):
    return HttpResponse("Todays Date is " +str(datetime.now()))

def monday(request):
    return HttpResponse("First Django class")
def monarch(request):
    return HttpResponse("Rose Avenue, off Argwings Kodhek")