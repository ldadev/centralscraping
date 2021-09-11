from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Course


def index(request):

	courses = Course.objects.all()
	exmple = request,'course/main.html',{'courses':courses}
	return example

"""
def handler500(request):
    return render(request, 'course/500.html', status=500)
"""