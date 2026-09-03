from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def components_view(request):
    return render(request, 'showcases/components.html')

class javascripts_view(TemplateView):
    template_name = "showcases/javascripts.html"