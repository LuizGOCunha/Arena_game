def descanso(playervida, playerdano):
    while True:
        print("Você retorna a sua cela e é colocado novamente aos grilhões."
              "A noite é tranquila, e nada quebra o silêncio além de seus próprios pensamentos.")
        print("Aqui você pode remoer sobre sua condição, ou descansar o melhor que pode.")
        print("O que deseja fazer?")
        decisao = input(">")
        if decisao == "remoer":
            playerdano += playerdano / 10
            playervida -= playervida / 10
            print("Você mal dorme, permanecendo desperto por horas remoendo a injustiça de sua situação.")
            print("Em meio a ranger de dente você compreende a injustiça que lhe foi cometida. Você promete retribuir na mesma moeda.")
            print("A começar pelo pobre bastardo de amanhã")
            break
        elif decisao == "descansar":
            if playerdano > 500:
                pesadelos(playerdano, playervida)
                break
            else:
                print("Você renova suas energias, e suas esperanças.")
                playervida += playervida/20
                break
        else:
            print("Não entendido")
    return playervida, playerdano

def pesadelos(playerdano, playervida):
    if playerdano in range(501,650):
        print("Você dorme com o som do gotejar de seu teto. Em seu sono você vê a faces de muitas almas que feriu, elas lhe ameaçam.")
        print("Você sua frio a noite inteira, acordando ainda cansado.")
        playervida -= (playerdano/30)
        playerdano += 100
    elif playerdano in range(650,800):
        print('Você tem dificuldade em dormir, mas dorme. Em seu sono você sente que está sendo arrastado por uma mão de unhas longas, enquanto vozes riem e comemoram.')
        print('Você salta da cama e grita, percebendo que está de volta em sua cela. Você tenta descansar novamente, mas apenas retorna ao pesadelo.')
        playervida -= (playerdano/25)
        playerdano += 100
    elif playerdano in range(800,1000):
        print('Seu coração demora a relaxar, dormindo apenas em meio à madrugada. Você sente o cheiro de uma ceia e o som de cantoria.')
        print('Quando olha ao redor você percebe uma comemoração, mas você não é convidado. Você está amarrado, com uma forca enlaçada no pescoço.')
        print('Lhe empurram de um degrau e você sente o terrível apertar em seu pescoço. O regozijo dos convidados é a ultima coisa que escuta antes da morte.')
        print('Você acorda, nem mesmo se alerta. Está exausto. Apenas busca um cochilo antes do amanhecer.')
        playervida -= (playerdano/20)
        playerdano += 100
    elif playerdano >= 1000:
        print('Em seu sonho você está sendo enforcado. Mas as cordas são frágeis como papel molhado. Assim como aqueles que festejam sua morte.')
        print('Você se solta de suas amarras e salta na direção dos convidados. Você os destroi com grande gosto')
        print('Você fere, e as feridas nunca deixam de fluir, assim como os gritos nunca deixam de ecoar. No fim você nada em um mar de sangue, em uma cacofonia de guinchos.')
        print('Você desperta, com o mesmo olhar alucinado que tinha naquela alucinação. Imóvel, você encara o teto. Com punhos ansiosos para tornar sonho realidade')
        playervida -= (playerdano/10)
        playerdano += 150
    if playervida <= 0:
        print("Os guardas chamam o seu nome, mas você não se levanta. Quando eles abrem a sua cela lhe encontram imóvel, de olhos entreabertos.")
        print("Eles lhe cutucam, mas não há reação. Após um tempo percebem que você está morto. Tomado por algum mal súbito.")
        print('Ou apenas, como reza a lenda no local, um corpo que rejeitou sua própria decrépita alma.')
        exit()
    return playerdano, playervida


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