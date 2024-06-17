from django.shortcuts import render, get_object_or_404
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
    