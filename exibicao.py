def barradevida (vida):
    quantblip = int(round(vida, -2) / 100)
    barra = quantblip * "█"
    return barra

def exibicaodevida(playervidalocal, inimigovida):
    print(f"vida do inimigo: {inimigovida}")
    print(barradevida(inimigovida))
    print(f"Sua vida: {playervidalocal}")
    print(barradevida(playervidalocal))

