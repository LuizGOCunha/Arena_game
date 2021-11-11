def descanso(playervida, playerdano):
    while True:
        print("Você retorna a sua cela e é colocado novamente aos grilhões."
              "A noite é tranquila, e nada quebra o silêncio além de seus próprios pensamentos.")
        print("Aqui você pode remoer sobre sua condição, ou descansar o melhor que pode.")
        print("O que deseja fazer?")
        decisao = input(">")
        if decisao == "remoer":
            playerdano += playerdano / 5
            playervida -= playervida / 5
            print("Você é consumido aos poucos por seus pensamentos destrutivos."
                  "Uma pequena morte e uma vil divindade se alargam em seu espírito."
                  "As celas ao lado escutam ranger de dentes pela madrugada.")
            break
        elif decisao == "descansar":
            print("Você renova suas energias, e suas esperanças.")
            playervida += playervida/10
            break
        else:
            print("Não entendido")
    return playervida, playerdano


def despertar(playernome):
    print(f'Seus olhos se abrem de uma noite de sono. Os berros da plateia ao lado de fora clamam o nome "{playernome}" Você levanta?')
    while True:
        levantar = input(">")
        if levantar == "sim":
            print("Você se ergue, apanha sua arma, e caminha na direção do portão, alcançando as areias da Arena.")
            break
        if levantar in ("nao", "não"):
            print(
                "Você não tem escolha, os guardas ferem suas costas com armas pontiagudas. "
                "Você se ergue contra sua vontade e atravessa os portões.")
            break
        else:
            print("não entendido")

def final():
    print("Você conquista sua liberdade, uma escapada feita através do sangue de desconhecidos. "
          "Você atravessa os portões e vê o sol. O brilho lhe cega.")
    print("Não há vida para homens como você. Uma vez um demônio, sempre um demônio.")
    print("Mas nada lhe impede de tentar")

def fimdejogo():
    print("Jogar de novo?")
    end = input(">")
    if end.lower() == "sim":
        pass
    elif end.lower() in ("não", "nao"):
        print("GAME OVER")
        exit()
    else:
        print("Não entendido.")