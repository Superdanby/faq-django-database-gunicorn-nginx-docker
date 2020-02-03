from django.urls import path, re_path

from . import views

app_name = 'faqsystem'
urlpatterns = [
    path('feedback', views.FeedbackView.as_view(), name='feedback'),
    re_path(r'^feedback/.*', views.FeedbackView.as_view(), name='feedback'),
    re_path(r'^.*$', views.FAQView.as_view(), name='home'),
]
