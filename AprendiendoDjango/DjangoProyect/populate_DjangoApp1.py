import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProyect.settings')

import django
django.setup()

from DjangoApp1.models import Bares, Tapas


def populate():
    nuevo_bar = add_bar('Bar Alberto','Calle Gran Vía, 8')

    add_tapa(bar=nuevo_bar,
        nombre='Emparedado de atún')

    add_tapa(bar=nuevo_bar,
        nombre='Bocadillo de jamón')

    add_tapa(bar=nuevo_bar,
        nombre='Emparedado vegetal')


    nuevo_bar= add_bar('La taberna', 'Calle Larga, 24')

    add_tapa(bar=nuevo_bar,
        nombre='Tapa de salmón')

    add_tapa(bar=nuevo_bar,
        nombre='Tapa de queso')

    add_tapa(bar=nuevo_bar,
        nombre='Ración de calamares')


    # Print out what we have added to the user.
    for b in Bares.objects.all():
        for t in Tapas.objects.filter(bar=b):
            print("- {0} - {1}".format(str(b), str(t)))

def add_tapa(bar, nombre):
    t = Tapas.objects.get_or_create(bar=bar, nombre=nombre)[0]
    t.bar=bar
    t.nombre=nombre
    t.save()
    return t

def add_bar(nombre, direccion):
    b = Bares.objects.get_or_create(nombre=nombre, direccion=direccion)[0]
    return b

# Start execution here!
if __name__ == '__main__':
    print("Starting DjangoApp population script...")
    populate()
