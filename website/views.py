from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        context = {}
    return render(request, 'website/welcome.html', context)

def aboutMe(request):
    return HttpResponse("This is the about me page.")
