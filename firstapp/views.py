from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Create your views here.


def hello_app(request):
    return HttpResponse('Hello world')


class HelloWorld(View):
    def get(self, request):
        return HttpResponse('Hello class View')


def home(request):
    form = ReservationForm()  # Create Variable with reservationForm()

    if request.method == 'POST':
        # Pass user input to form, as request.POST contain all user input
        form = ReservationForm(request.POST)
        if form.is_valid():  # Django build-in form validation is_valid()
            form.save()  # if valid Save to model
            return HttpResponse('success')

    return render(
        request,
        'index.html',
        {'form': form}  # key 'form' - a variable that we want to use in out template and value form - is the actual variable we have in view.py
    )
