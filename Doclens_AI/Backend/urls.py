# urls.py
from django.urls import path
from .views import verify_document
from Backend import views

urlpatterns = [
    path('', views.home, name='home'),  # This is the root URL, it will display home.html
    path('upload/', views.render_form, name='render_form'),
    path('verify/', views.verify_document, name='process_document'),
]

