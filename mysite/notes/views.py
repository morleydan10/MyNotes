from django.shortcuts import render, get_object_or_404
from notes.models import Note

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the MyNotes App.")


def notes_list(request):
    notes = Note.objects.all()
    return Htt

def note_detail(request, pk):
    note = get_object_or_404(Note, pk)
    return render(request, 'notes/note_deatil.html/', {'note': note})
    