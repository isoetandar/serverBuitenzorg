from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^Registration$', views.register, name="register"),
    url(r'^Login$', views.validate_login, name="login")

]                            
