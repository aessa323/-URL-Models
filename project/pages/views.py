from datetime import date
from django.shortcuts import render
from .models import Student

def index(request):
    context = {
        'first_name': 'aessa',
        'last_name': ' Abu Ajairim',
        'student_id': 120213382,
        'address': 'Gaza, Palestine',
        'email': 'aessabaraka323@gmailcom',
        'date_of_birth': date(2003, 3, 23),
        'major': 'Web Development',
        'university': 'Islamic University of Gaza',
    }

    return render(request, 'pages/index.html', context)


def home(request):
    student = Student.objects.order_by('-id').first()
    return render(request, 'pages/home.html', {
        'student': student
    })