from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
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
    # Django docutmentation recommends using POST requests rather than a GET request because it is more difficult for hackers to break in using a POST request
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username= username, password=password)

        if user is not None:
            login(request,user)
            return redirect('notes/')
        else:
            return HttpResponse("Invalid login credentials.")
    else:
        return HttpResponse("Invalid request method. Must be POST.")