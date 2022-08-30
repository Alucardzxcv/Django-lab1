from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/polls/
    path('', views.index, name='index'),
    # ex: localhost:8080/polls/5/
    path('<int:pregunta_id>/', views.detalle, name='detail'),
    # ex: localhost:8080/polls/5/results/
    path('<int:pregunta_id>/results/', views.resultados, name='results'),
    # ex: localhost:8080/polls/5/vote/
    path('<int:pregunta_id>/vote/', views.votar, name='vote'),
    
    path('<int:pregunta_id>/<int:pregunta_id2>/suma/', views.sumar, name='suma'), 
    path('<int:pregunta_id>/<int:pregunta_id2>/restar/', views.resta, name='restar'), 
    path('<int:pregunta_id>/<int:pregunta_id2>/multiplicar/', views.multiplicacion, name='multiplicacion'),
]
