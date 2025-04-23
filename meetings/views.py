from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from meetings.models import Meeting, Room

@login_required
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})

@login_required
def rooms(request):
    return render(request, 'meetings/rooms.html', {'rooms': Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])
'''
#View as function
@login_required
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {"form": form})

@login_required
def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'meetings/edit.html', {"form": form})

@login_required
def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("welcome")
    return render(request, 'meetings/confirm_delete.html', {"meeting": meeting})
'''
#View as class
class MeetingBaseView(LoginRequiredMixin):
    model = Meeting
    fields = '__all__'
    success_url = reverse_lazy('welcome')

class MeetingCreateView(MeetingBaseView, CreateView):
    template_name = 'meetings/new.html'

class MeetingUpdateView(MeetingBaseView, UpdateView):
    template_name = 'meetings/edit.html'

class MeetingDeleteView(MeetingBaseView, DeleteView):
    template_name = 'meetings/confirm_delete.html'