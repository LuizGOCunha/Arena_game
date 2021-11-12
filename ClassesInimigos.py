from exibicao import *
from acoes import *
class Inimigo:
    def __init__(self, nome, raca, vida, dano):
        self.nome = nome
        self.raca = raca
        self.vida = vida
        self.dano = dano

    def combate(self, playernome, playerdano, playervida):
        contador1, contador2, contador3 = 0, 0, 0
        inimigodano, inimigovida = self.dano, self.vida
        playervidalocal, playerdanolocal = playervida, playerdano
        print("Seu oponente é um", self.raca, "chamado", self.nome)
        if type(self) == Inimigo:
            if inimigodano < 300:
                print("Ele treme de uma ponta a outra no corpo, engolindo em seco. Ele claramente não quer lutar, resta saber se ele vai.")
            elif inimigodano in range(300, 600):
                print('Ele cerra os dentes, seus olhos tentam desviar. "Eu não quero fazer isso, amigo. Me perdoe." Ele declara, enquanto avança com remorso')
            elif inimigodano in range(600,800):
                print("Ele move seu pescoço de lado a outro, emitindo um estalar barulhento. Seus olhos são frios, e enxergam através de você.")
            elif inimigodano in range(800,1000):
                print("Ele salta de pé em outro, sua boca de poucos dentes sorri, suas mãos tremem em entusiasmo, extasiadas em derramar sangue uma vez mais.")
            elif inimigodano > 1000:
                print('Seu oponente já corre em sua direção com olhos doentes de um cão em frenesi. Ele range os dentes antes de bramir como uma criatura, iniciando seu ataque')
        else:
            pass
        while True:
            print("Você pode atacar, defender ou desviar. O que quer fazer?")
            acao = input(">")
            if acao.lower() == ("atacar"):
                playervidalocal, inimigovida = (ataqueduplo(playervidalocal, playerdanolocal, inimigovida, inimigodano))
                contador3 += 1
                exibicaodevida(playervidalocal, inimigovida)
            elif acao.lower() == ("defender"):
                playervidalocal, playerdanolocal, contador3 = (defesa(playervidalocal, playerdanolocal, inimigovida, inimigodano, contador3))
                exibicaodevida(playervidalocal, inimigovida)
            elif acao.lower() == "desviar":
                playervidalocal, inimigovida, contador3 = (esquiva(playervida, playervidalocal, playerdanolocal, inimigovida, inimigodano, contador3))

            if playervidalocal <= 0:
                print("Sua visão apaga, e seus ouvidos zunem. Nem mesmo escuta seu corpo bater ao chão. Perdendo a sensação das pernas você nota que jamais será agraciado pela luz solar, definhando no escuro.")
                print("Sua alma morre antes do corpo.")
                exit()
            elif playervidalocal <= 1000 and contador1 == 0 and contador3 != 0:
                print("Sua visão escurece e você sente gosto de sangue, o fim está próximo.")
                contador1 += 1
            if inimigovida <= 0:
                print("Seu oponente desfalece, morto antes mesmo de atingir o chão. Você vence, mas a vitória não é doce.")
                break
            elif inimigovida <= 1000 and contador2 == 0:
                print("Os olhos do seu oponente se alargam e seus joelhos tremem, a vitória está próxima.")
                contador2 += 1


class Boss(Inimigo):
    def entrada_agressiva(self):
        print("Você sente o chão tremer, e as paredes sacudirem. A plateia permanece calada, temerosa, apenas então explodindo em entusiasmo.")
        print(f"O portão a sua frente se abre, dele saindo uma alta figura. Um gigantesco {self.raca}. Todos repetem seu nome: {self.nome}.")
        print("Ele aponta em sua direção e traça sua garganta com seu dedão estirado. Você sente que esses podem ser seus últimos momentos.")
