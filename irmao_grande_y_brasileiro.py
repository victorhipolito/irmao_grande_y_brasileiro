from time import sleep as pausa
from random import randint as bingo
from random import choice as escolha

class Setup:
    def __init__(self):
        self.qt_irmaos = int(input("Insira aqui a quandtidade de participantes\n _ "))
        self.irmaos = list()
        for n in range(1, self.qt_irmaos + 1):
            cara = input(f"Qual o nome do {n}° participante?\n _ ")
            tipo = int(input(f"O participante é:\n1 - Caos\n2 - Neutro\n _ "))
            self.irmaos.append([cara, tipo])
        self.casa = ["no quarto", "na cozinha", "nos banheiros", "na sala principal",
                     "no quarto do líder", "nos dormitórios", "na piscina", "na sacada", "no confessionário",
                     "no porão", "no corredor", "no jardim", "num beco escuro"]



