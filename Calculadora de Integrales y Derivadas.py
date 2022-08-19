from sympy import integrate, init_printing, diff
import numpy as np
from sympy.abc import *
import os
init_printing(use_latex="mathjax")
 

while(True):
    def Integrar_Funcion():
        try:
            print("[*]Ejemplo de sintaxis")
            print("[*] 3*x+2**3")
            print("[*] Donde '**' representa un numero elevado")
            i = input("[*]ingresa tu funcion a integrar\n\n[#]")
            result = (integrate(i))
            os.system("cls")
            print("El resultado es: " + str(result)+"\n")
            input("[!]Toque cualquier tecla para volver al menu")
            os.system("cls")
        except: NameError
        os.system("cls")
            
    def Derivar_Funcion():
        try:
            print("[*]Ejemplo de sintaxis")
            print("[*] 3*x+2**3")
            print("[*] Donde '**' representa un numero elevado")
            d = input("[*]ingresa tu funcion a integrar\n\n[#]")
            result = diff(d)
            os.system("cls")
            print("[#] El resultado es: " + str(result)+"\n")
            input("[!]Toque cualquier tecla para volver al menu")
            os.system("cls")
        except:NameError

    print("[*] Welcome to the Integrate Calculadora")
    print("1 - Integrar")
    print("2 - Derivar")
    answer = input("Elige una Opcion\n\n [#]")
    os.system("cls")

    if answer == "1":
        Integrar_Funcion()

    if answer == "2":
        Derivar_Funcion()
    
    if answer != "1" or "2":
        print("[!] Escribe un numero correcto!!\n")