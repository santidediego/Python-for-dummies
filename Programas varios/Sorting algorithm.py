#! /usr/bin/env python
#We assume a 100 sized list


import random

def bubble(mat):
    i=1
    while i<100:
        j=0
        while j<100-i:
            if mat[j]>mat[j+1]:
                aux=mat[j]
                mat[j]=mat[j+1]
                mat[j+1]=aux
            j=j+1
        i=i+1
    return mat

def selection(mat):
    i=0
    while i<99:
        min=i
        j=i+1
        while j<100:
            if mat[j]<mat[min]:
                min=j
            j=j+1
        aux=mat[i]
        mat[i]=mat[min]
        mat[min]=aux
        i=i+1

def main():
    #First, we create the matrix
    m=[]
    i=0
    while i<100:
        m.append(random.randrange(101)) #A number between 0 and 100
        i=i+1
    print (m)
    bubble(m)
    print (m)
    selection(m)
    print (m)

main()
