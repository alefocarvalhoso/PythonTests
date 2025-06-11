import time
import math
#3 variaveis diferentes: Nome, Altura e Peso
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))




#pega o peso da pessoa e divide por altura x altura
IMC = peso /  (altura ** 2)
#espera dois segundos antes de printar o IMC final
time.sleep(2)
#printa o IMC final
print(f"O Indice de Massa Corporal de {nome} é: {IMC:.2f}")

if IMC < 18.5:
    print("Abaixo do peso")
    
if IMC >= 18.6 and IMC <= 24.9:
    print("Peso ideal")

if IMC >=  25.0 and IMC <= 29.9:
    print("Sobrepeso")

if IMC >= 30.0 and IMC <= 34.9:
    print("Obesidade Grau 1")

if IMC >= 35.0 and IMC <= 39.9:
    print("Obesidade Grau 2")  

if IMC >= 40.0:
    print("Obesidade Grau 3")    

