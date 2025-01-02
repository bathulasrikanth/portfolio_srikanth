from django.urls import path
from srikanth import views
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("resume/",views.resume,name="resume"),
    path('projects/', views.project_list, name='projects'),
    path('certificate',views.certificate,name="certificate"),
    path("contact1",views.contact1,name="contact1")

]