from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    data = {
            "School_start": datetime.datetime.now(),

            "data": [
            {
                'id': '01', 
                'name': 'Modhon lal', 
                'course': ['English','math', 'chemistry', 'physics']
            },
            {
                'id': '02', 
                'name': 'ismail ahmed', 
                'course': ['js','math', 'java', 'physics']
            },
            {
                'id': '03', 
                'name': 'Abul', 
                'course': ['English','cpp', 'chemistry', 'python']
            } ]}



    return render(request,'home.html',data)