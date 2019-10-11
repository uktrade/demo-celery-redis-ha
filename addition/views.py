from .tasks import adding_task
from .forms import AdditionForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from celery import current_app
# Create your views here.


class HomeView(FormView):
    template_name = 'home.html'
    form_class = AdditionForm
    success_url = reverse_lazy('task')
    task_id = None

    def form_valid(self, form):

        a = int(form.cleaned_data["a"])
        b = int(form.cleaned_data["b"])

        task = adding_task.delay(a, b)
        self.task_id = task.task_id
        return super(HomeView, self).form_valid(form)

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.task_id})


class TaskView(TemplateView):
    template_name = 'task.html'

    import time
    time.sleep(5)

    def get_context_data(self, *args, **kwargs):
        context = super(TaskView, self).get_context_data(*args, **kwargs)
        task_id = context['pk']
        task = current_app.AsyncResult(task_id)
        context['task_status'] = task.status
        context['task_id'] = task_id
        if task.status == 'SUCCESS':
            context['result'] = task.get()
        return context
