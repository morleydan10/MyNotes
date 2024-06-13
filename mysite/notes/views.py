from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the MyNotes App.")


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes_list.html/', {'notes': notes})