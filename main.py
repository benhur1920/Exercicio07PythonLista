#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import random
import math


def carregarVetorComNumerosAleatorios():
  vetor = []
  num = ''
  for i in range(5):
    num = random.randint(1,20)
    vetor.append(num)
  return vetor

def somaDosElementosDoVetor(vetor):
  soma = sum(vetor)
  return soma

def multiplicacaoDosElementosDoVetor(vetor):
  multiplicacao = math.prod(vetor)
  return multiplicacao

def exibirResutados(vetor, soma, multiplicacao):
  print(f'Lista de números foi {vetor}')
  print(f'Soma dos elementos é {soma}')
  print(f'Multiplicação dos elementos é {multiplicacao} ')


vetor = carregarVetorComNumerosAleatorios()
soma = somaDosElementosDoVetor(vetor)
multiplicacao = multiplicacaoDosElementosDoVetor(vetor)
exibirResutados(vetor,soma, multiplicacao)