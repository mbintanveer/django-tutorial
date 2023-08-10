from django.urls import path

from core_apps.autointerviewer import views

urlpatterns = [
    path("", views.generate_questions, name='generate_questions')

]
