from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse


from .models import DemoItem

# Create your views here.
def components_view(request):
    return render(request, 'showcases/components.html')

class javascripts_view(TemplateView):
    template_name = "showcases/javascripts.html"

def htmx_demo_view(request):
    demo_items = DemoItem.objects.all()
    return render(request, "showcases/htmx_demo.html", {"demo_items" : demo_items})

def htmx_item_add_view(request):
    if request.method == 'POST':
        title = request.POST.get("title").strip()
        print(title)
        if title:
            DemoItem.objects.create(title=title)
    return render(request, "showcases/partials/demo_item_list.html", {"demo_items": DemoItem.objects.all()})

def htmx_item_delete_view(request, pk):
    item_delete = get_object_or_404(DemoItem, pk=pk)
    if request.method == 'DELETE':
        item_delete.delete()
        return HttpResponse("") #จะเอาค่าเปล่าไปแทน
    return HttpResponse(status=405) #method not allowed