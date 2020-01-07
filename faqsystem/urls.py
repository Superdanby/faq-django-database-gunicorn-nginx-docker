from django.urls import path

from . import views

app_name = 'faqsystem'
urlpatterns = [
    path('', views.FAQView.as_view(), name='home'),
    path('<str:pk>/', views.FAQView.as_view(), name='home'),
]
