from between import *
from ClassesInimigos import *

gabriel = Inimigo("Gabriel", "proeliano", 2500, 250)
manuel = Inimigo("Manuel", "dannumiano", 2300, 500)
elias = Inimigo("Elias", "zarbatiano", 1500, 1000)
bjorn = Boss("Bjorn", "homem do norte", 4600, 600)
benedito = Inimigo("Benedito", "ni'kaniano", 3000, 500)
rafael = Inimigo('Rafael', "zarbatiano", 2000, 1200)
eliseu = Inimigo('Eliseu', "ni'kaniano", 4000, 600)
farelius = Boss("Farelius", "líbiro", 4000, 1500)

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
    manuel.combate(playernome, playerdano, playervida)
    playervida, playerdano = (descanso(playervida, playerdano))
    despertar(playernome)
    elias.combate(playernome, playerdano, playervida)
    playervida, playerdano = (descanso(playervida, playerdano))
    despertar(playernome)
    bjorn.entrada_agressiva()
    bjorn.combate(playernome, playerdano, playervida)
    playervida, playerdano = (descanso(playervida, playerdano))
    despertar(playernome)
    benedito.combate(playernome, playerdano, playervida)
    playervida, playerdano = (descanso(playervida, playerdano))
    despertar(playernome)
    rafael.combate(playernome, playerdano, playervida)
    playervida, playerdano = (descanso(playervida, playerdano))
    despertar(playernome)
    eliseu.combate(playernome, playerdano, playervida)
    final()
    fimdejogo()


