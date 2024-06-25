from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from notes.models import Note

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the MyNotes App.")


def notes_list(request):

    print(request)
    notes = Note.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note_detail.html', {'note': note})

def login_form(request):
    return render(request, 'login_form.html')

def login_attempt(request):

    username = request['username']
    password = request['password']

    user = authenticate(username= username, password=password)

    if user is not None:
        pass
    else:
        return ValueError("User not found.")
    