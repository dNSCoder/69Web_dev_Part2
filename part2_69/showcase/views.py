from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import DemoItem


def components_view(request):
    return render(request, 'showcases/components.html')


def htmx_demo_view(request):
    return render(request, 'showcases/htmx_demo.html', {'items': DemoItem.objects.all()})


def demo_item_add_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            DemoItem.objects.create(title=title)
    return render(request, 'showcases/partials/demo_item_list.html', {'items': DemoItem.objects.all()})


def demo_search_view(request):
    q = request.GET.get('q', '').strip()
    items = DemoItem.objects.filter(title__icontains=q) if q else DemoItem.objects.all()
    return render(request, 'showcases/partials/demo_item_rows.html', {'items': items})


def demo_item_delete_view(request, pk):
    item = get_object_or_404(DemoItem, pk=pk)
    if request.method == 'DELETE':
        item.delete()
        return HttpResponse('')
    return HttpResponse(status=405)
