from django.urls import path
from clinical_app import views
urlpatterns = [
    path('show/',views.Patient_show),
    path('add/',views.Patient_add),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
    path('showclinical/<int:id>',views.show_clinical_data),
    path('analysis/<int:pk>',views.analysis),
 

]