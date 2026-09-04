import os 
from argumentos import leerDatos
from argumentos import imprimirDatos

def main():
    os.system("cls")
    cif,nomb,prom,beca=leerDatos()
    imprimirDatos(cif,nomb,prom,beca)

main()
