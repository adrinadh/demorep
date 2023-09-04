from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Task
from django.http import HttpResponse
from .forms import updateForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class homeview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task_detail'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task_update'
    fields = ['name', 'priority', 'date']

    def get_success_url(self):
        return reverse_lazy('detailview', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'update.html'
    success_url = 'homeview'


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')

        if not name:
            return HttpResponse('<p style="font-size: 50px; text-align: center;">⚠Provide a Name for the Task</p>')
        elif not priority:
            return HttpResponse('<p style="font-size: 50px; text-align: center;">⚠Provide Task Priority</p>')
        else:
            task = Task(name=name, priority=priority, date=date)
            task.save()

    task1 = Task.objects.all()
    return render(request, 'home.html', {'task1': task1})


def confirm_delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = updateForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request, 'update.html', {'form': f, 'task': task})
