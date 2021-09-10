from django.shortcuts import render

from .models import Course


def index(request):

	courses = Course.objects.all()
	return render(request,'course/main.html',{'courses':courses})


def handler500(request):
    return render(request, 'course/500.html', status=500)
	