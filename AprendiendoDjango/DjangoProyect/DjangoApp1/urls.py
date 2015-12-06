from django.conf.urls import patterns, url
from DjangoApp1 import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^about/$', views.about, name='about'),
        url(r'^bar/(?P<bar_name_slug>[\w\-]+)/$', views.bares, name='bar'),) # New!


'''
El caracter r antes de la cadena de texto indica que es una cadena de caracteres en crudo. Esto permite que no tengamos que poner constantemente sentencias de escape para caracteres propios de expresiones regulares.
El caracter ^ indica el comienzo de nuestra expresión.
El caracter $ indica el fin de nuestra expresión.

'''
