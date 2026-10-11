from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Task

PAGE_SIZE = 5


def filtered_page(user, q, page_number):
    tasks = Task.objects.filter(owner=user)
    if q:
        tasks = tasks.filter(title__icontains=q)
    return Paginator(tasks, PAGE_SIZE).get_page(page_number)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = filtered_page(self.request.user, '', 1)
        context['q'] = ''
        return context


@login_required
def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Task.objects.create(owner=request.user, title=title)
    page = filtered_page(request.user, '', 1)
    return render(request, 'tasks/partials/task_page_rows.html', {'page': page, 'q': ''})


@login_required
def task_filter(request):
    q = request.GET.get('q', '').strip()
    page = filtered_page(request.user, q, 1)
    return render(request, 'tasks/partials/task_page_rows.html', {'page': page, 'q': q})


@login_required
def task_load_more(request):
    q = request.GET.get('q', '').strip()
    page = filtered_page(request.user, q, request.GET.get('page', 1))
    return render(request, 'tasks/partials/task_page_rows.html', {'page': page, 'q': q})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'DELETE':
        task.delete()
        return HttpResponse('')
    return HttpResponse(status=405)
