from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def cuenta(request):
    return render(request, 'app/cuenta.html')

def api(request):
    return render(request, 'app/api.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def inicio(request):
    return render(request, 'app/inicio.html')

def objetos(request):
    return render(request, 'app/objetos.html')

def recuperar(request):
    return render(request, 'app/recuperar.html')

def soporte(request):
    return render(request, 'app/soporte.html')

def souls(request):
    return render(request, 'app/souls.html')
