from django.urls import path
from app import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('allow/',views.verifyToken,name='verify'),
    path('niveles/<int:id>',views.niveles,name='niveles'),
    path('materias/<int:id>',views.materias,name='materias'),
    path('filtros/',views.filtros,name='filtros')
]