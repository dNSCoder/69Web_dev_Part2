from django.shortcuts import render

# Create your views here.
def components_view(request):
    return render(request, 'showcases/components.html')