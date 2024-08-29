from django.urls import  path
from . import views

app_name= "student"
urlpatterns = [
   path('', views.index, name="index"),
   path('ajouterStudent', views.ajoutStudent, name="ajouterStudent" ),  
   path('modifierStudent/<int:id>/', views.modifierStudent, name="modifierStudent" ),
   path('suprimer/<int:id>', views.suprimer, name ='suprimer' ),
   
]
