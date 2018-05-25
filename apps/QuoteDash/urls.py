from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^Registration$', views.register, name="register"),
    url(r'^Login$', views.validate_login, name="login"),
    url(r'^(?P<id>\d+)/edit$', views.edit, name="edit"),
    url(r'^(?P<id>\d+)/update$', views.update, name="update"),
    url(r'^delete/(?P<idu>\d+)/(?P<idq>\d+)$', views.destroy, name="delete"),
    url(r'^(?P<id>\d+)/quote$', views.quote, name="quote"),
    url(r'^addQuote$', views.addQuote, name="addQuote"),
    url(r'^likes/(?P<idq>\d+)$', views.likes, name="likes"),
    url(r'^quotedash$', views.quotedash),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<id>\d+)$', views.userQuotes)
]                            
