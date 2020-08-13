from django.core.paginator import Paginator
from .models import Post,Categoria,RedesSociales,Web

def consulta(id):
    try:
        return Post.objects.get(id = id)
    except:
        return None

def obtenerRedes():
    return RedesSociales.objects.filter(estado = True).first()

def obtenerWeb():
    return Web.objects.filter(estado = True).latest('fecha_creacion')

def generarCategoria(request,nombre_categoria):
    posts = Post.objects.filter(
                        estado = True,
                        publicado = True,
                        categoria = Categoria.objects.filter(nombre = nombre_categoria).first()
                        )
    try:
        categoria = Categoria.objects.filter(nombre = nombre_categoria).first()
    except:
        categoria = None

    paginator = Paginator(posts,3)
    pagina = request.GET.get('page')
    posts = paginator.get_page(pagina)
    contexto = {
        'posts':posts,
        'sociales':obtenerRedes(),
        'web':obtenerWeb(),
        'categoria':categoria,
    }
    return contexto
