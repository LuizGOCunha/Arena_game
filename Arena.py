from between import *
from ClassesInimigos import *

gabriel = Inimigo("Gabriel", "Humano", 1500, 300)
fernish = Inimigo("Fernish", "Goblin", 1200, 600)
gorgoth = Inimigo("Gorgoth", "Orc", 2000, 500)
tarmanto = Boss("Tarmanto", "Ogro", 3500, 600)

while True:
    print("Faz tanto tempo que está em cativeiro que sua memória se esvai aos poucos.")
    print("Você encara a parede tentando lembrar seu nome")
    print("Qual o seu nome?")
    playernome = input(">")
    while True:
        print("Além disso você tenta lembrar o quão bom você é em machucar seu próximo.")
        print("Qual o seu dano? (Entre 100-1000)")
        playerdano = int(input(">"))
        if playerdano < 100 or playerdano > 1000:
            print("dano invalido")
        else:
            break
    while True:
        print("Você toca o seu corpo e tenta lembrar o seu tamanho, se é grande e resistente ou pequeno e ágil.")
        print("Quanto tem de vida?(Entre 500 e 5000)")
        playervida = int(input(">"))
        if playervida < 500 or playervida > 5000:
            print("vida inválida")
        else:
            break

    print("Você lembra de tudo mais uma vez, inclusive da memória que fez a si mesmo.")
    print("Uma promessa de não esquecer quem é, ou o que é.")
    print("Isso se repete a cada noite, e por hoje você manteve sua promessa consigo mesmo.")
    print("Você se deita, e tenta não sonhar.")

    despertar(playernome)
    gabriel.combate(playernome, playerdano, playervida)
    playervida, playerdano = (descanso(playervida, playerdano))
    despertar(playernome)
    fernish.combate(playernome, playerdano, playervida)
    playervida, playerdano = (descanso(playervida, playerdano))
    despertar(playernome)
    gorgoth.combate(playernome, playerdano, playervida)
    playervida, playerdano = (descanso(playervida, playerdano))
    despertar(playernome)
    tarmanto.entrada()
    tarmanto.combate(playernome, playerdano, playervida)
    final()
    fimdejogo()


