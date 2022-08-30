from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la visa de encuestas!")

def detalle(request, pregunta_id):
    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id)

def resultados(request, pregunta_id):
    response = "Estas viendo los resultado de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Estas votando por la pregunta %s." % pregunta_id)
    
def sumar(request, pregunta_id,pregunta_id2):
    suma=pregunta_id + pregunta_id2
    return HttpResponse("%s es la suma de %s y %s ." %(suma,pregunta_id,pregunta_id2) )

def resta(request, pregunta_id,pregunta_id2):
    restar=pregunta_id -  pregunta_id2
    return HttpResponse("%s es la resta de %s y %s ." %(restar,pregunta_id,pregunta_id2) )

def multiplicacion(request, pregunta_id,pregunta_id2):
    multiplicar=pregunta_id *  pregunta_id2
    return HttpResponse("%s es la multiplicacion de %s y %s ." %(multiplicar,pregunta_id,pregunta_id2) )



