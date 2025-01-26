from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

##===================================Gestión de Errores==================================
def error_404_view(request, exception):
    return render(request, 'main/404.html')

def error_403_view(request, exception):
    return render(request, 'main/403.html')