from django.shortcuts import render
from usuarios.models import Usuario

# Create your views here.
from django.http import HttpResponse

def usuario_view(request):

    # Obtengo los datos del modelo Usuario
    usuarios = Usuario.objects.all()
    """
    datos = {
        "nombre": "Ana",
        "apellidos": "Martínez Pérez",
        "edad": 30,
        "email": "ana@example.com",
    }
    """

    html1 = f"""
            <html>
            <head><title>Datos de un Usuario</title></head>
            <body>
                <h1>Información personal</h1>"""
    
    # Recorro los usuarios
    for usuario in usuarios:       
        html2 = f"""
                <!--Para incluir datos que se encuentran en la vista, usamos llaves como se ve a continuación -->
                <ul>
                    <li>
                        <strong>Nombre: </strong>{usuario.nombre}</br>
                        <strong>Apellidos: </strong>{usuario.apellidos}</br>
                        <strong>DNI: </strong>{usuario.dni}</br>
                        <strong>Email: </strong>{usuario.email}</br>
                        <strong>Teléfono: </strong>{usuario.telefono}</br>
                    </li>
                </ul>                
        """
    html3 = """
            </body>
            </html>"""
    htmlfinal = html1 + html2 + html3

    return HttpResponse(htmlfinal)