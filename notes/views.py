from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from notes.forms import NoteForm
from notes.models import Note

# Create your views here.


@login_required
def show_notes(request, id):
    print(id)
    notes = get_object_or_404(Note, id=id)
    # notes.id
    context = {
        "notes_object": notes,
    }
    return render(request, "notes/detail.html", context)


@login_required
def create_notes(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            notes = form.save(False)
            notes.author = request.user
            notes.save()
            return redirect("show_my_tasks")
    else:
        form = NoteForm()
    context = {
        "form": form,
    }
    return render(request, "notes/create.html", context)


@login_required
def edit_notes(request, id):
    notes = get_object_or_404(Note, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return redirect("show_notes", id=id)
    else:
        form = NoteForm(instance=notes)
    context = {
        "notes_object": notes,
        "form": form,
    }
    return render(request, "notes/edit.html", context)
