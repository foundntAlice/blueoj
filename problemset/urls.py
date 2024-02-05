from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('problemset/', views.problemset, name = 'problemset'),
    path('problemset/details/<int:id>', views.details, name = 'details'),
    path('problemset/details/submit_code/', views.submit_code, name = 'submit_code'),
]