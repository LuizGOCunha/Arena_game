import random
from exibicao import *

def ataqueduplo(playervidalocal, playerdanolocal, inimigovida, inimigodano):
    mensagem = random.randint(0, 5)
    print(mensagem)
    if mensagem == 0:
        print('Vocês atingem um ao outro com inúmeros ataques, recuando ao mesmo tempo quando a dor se torna insuportável.')
    elif mensagem == 1:
        print('Você ergue sua arma e atinge seu oponente no ombro, sem notar que o outro também já balançava o braço, atingindo-lhe no pescoço de raspão')
    elif mensagem == 2:
        print('Notando que seu inimigo tinha uma postura larga, você abre um corte em sua perna, enquanto ele aproveita sua falta de equilíbrio, atingindo sua nuca.')
    elif mensagem == 3:
        print('Seu oponente abre um corte fundo em seu queixo. Você segura o pulso deste e atinge-o com uma cabeçada no nariz, que faz sangue espirrar.')
    elif mensagem == 4:
        print('Seu oponente acerta-lhe o joelho, mas perde o equilíbrio em meio movimento, o que facilita seu trabalho de cortar-lhe o estômago.')
    elif mensagem == 5:
        print("Você e seu oponente atacam ao mesmo tempo, vocês se atingem com o mesmo golpe ao lado da face. Os dois sacodem a cabeça, desorientados.")
    playervidafinal = playervidalocal - inimigodano
    inimigovidafinal = inimigovida - playerdanolocal
    return playervidafinal, inimigovidafinal

def ataque(vidaalvo, dano):
    vidaalvo -= dano
    return vidaalvo

def defesa(playervidalocal, playerdanolocal, inimigovida, inimigodano, contador3):
    playervidalocal = (ataque(playervidalocal, inimigodano/2))
    contador3 += 1
    playerdanolocal += playerdanolocal/20
    print("Você ergue suas mãos e tolera o impacto do golpe. Reservando sua energia para dar o troco.")
    return playervidalocal, playerdanolocal, contador3

def desviofalho(playervidalocal, inimigodano, inimigovida, contador3):
        print("Você tenta sair do caminho mas acaba sendo atingido no meio do movimento, recebendo um impacto ainda maior.")
        playervidalocal -= (inimigodano + inimigodano / 5)
        contador3 += 1
        exibicaodevida(playervidalocal, inimigovida)
        return playervidalocal, contador3

def esquiva(playervida, playervidalocal, playerdanolocal, inimigovida, inimigodano, contador3):
    esquivavar = random.randint(0, 10)
    print(esquivavar)
    if playervida > 4000:
        if esquivavar > 8:
            print("Você salta para longe do perigo com dificuldade. Atingindo seu oponente sem ser tocado.")
            inimigovida -= playerdanolocal
            exibicaodevida(playervidalocal, inimigovida)
        else:
            playervidalocal, contador3 = desviofalho(playervidalocal, inimigodano, inimigovida, contador3)
    elif playervida > 3000:
        if esquivavar > 5:
            print("Você dá um salto para trás e seu inimigo atinge o vento.")
            print("Logo após, você avança em uma estocada, e pega seu oponente sem equilíbrio.")
            inimigovida -= playerdanolocal
            exibicaodevida(playervidalocal, inimigovida)
        else:
            playervidalocal, contador3 = desviofalho(playervidalocal, inimigodano, inimigovida, contador3)
    elif playervida > 2000:
        if esquivavar > 3:
            print('Você dobra seus joelhos e escapa do golpe no último segundo. ')
            print('Seu inimigo lhe perde de vista, e parece confuso, até que você o atinge na lateral do torso.')
            inimigovida -= playerdanolocal
            exibicaodevida(playervidalocal, inimigovida)
        else:
            playervidalocal, contador3 = desviofalho(playervidalocal, inimigodano, inimigovida, contador3)
    elif playervida > 500:
        if esquivavar > 2:
            print("Você salta por cima de seu oponente, então pelo meio de suas pernas, acertendo-o nas costas enquanto ele lhe procura")
            inimigovida -= playerdanolocal
            exibicaodevida(playervidalocal, inimigovida)
        else:
            playervidalocal, contador3 = desviofalho(playervidalocal, inimigodano, inimigovida, contador3)
    elif playervida <= 500:
        if esquivavar > 1:
            print("Você se move ao redor do golpe como se a lâmina de seu oponente lhe repelisse. ")
            print("Desaparecendo por um instante antes de acertar seu inimigo na nuca, cortando fundo.")
            inimigovida -= playerdanolocal * 2
            exibicaodevida(playervidalocal, inimigovida)
        else:
            playervidalocal, contador3 = desviofalho(playervidalocal, inimigodano, inimigovida, contador3)
    return playervidalocal, inimigovida, contador3


