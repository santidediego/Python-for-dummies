from django.shortcuts import render  #For render templates
from DjangoApp1.models import Bares, Tapas
from django.http import HttpResponse


''' Basic index
def index(request):
    return HttpResponse("Hello world!")
'''

#Now we show an index with templates

def index(request):
    #Ordenamos los bares en orden descendente por nombre
    bares_list = Bares.objects.order_by('-nombre')
    context_dict = {'bares': bares_list}

    # Render the response and send it back!
    return render(request, 'DjangoApp1/index.html', context_dict)

def bares(request, bar_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:

        bar = Bares.objects.get(slug=bar_name_slug)
        context_dict['bar_nombre'] = bar.nombre


        tapas = Tapas.objects.filter(bar=bar)

        context_dict['tapas'] = tapas

        context_dict['bar'] = bar
    except Bares.DoesNotExist:

        pass

    # Go render the response and return it to the client.
    return render(request, 'DjangoApp1/bar.html', context_dict)
