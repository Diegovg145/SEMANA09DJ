from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
# Create your views here.
def saludo(request):
    mensaje ="""
    <h1>Inicio</h1>
    """
    return HttpResponse(mensaje)
def saludo(request):
    mensaje = """
    <h1>Bienvenidos</h1>
    <h2>Flor Cerdan</h2>
    <h3>Python....</h3>
    """
    return HttpResponse(mensaje)

def rango(request):
    a=10
    b=20
    resultado =f"""
    <h2>Numeros de [{a},{b}]</h2>
    Resultado : <br>
    <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
        resultado +="<url"
        return HttpResponse(resultado)