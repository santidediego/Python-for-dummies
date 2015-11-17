#!/usr/bin/env python


"""
Este programa esta creado para generar, con python 2.7, la base de datos 
que va a utilizar ejer3.py, ya que en python 3.4 dbm no funciona
"""


import dbm

bd=dbm.open('base_datos.dat','c')
bd.close()