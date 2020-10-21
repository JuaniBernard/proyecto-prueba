from repoPartidas import RepoPartidas
from servicesPartidas import ServicesPartidas


class Ahorcado:
    def menu_ahorcado(self):
        print('\n\tAHORCADO')
        print('\n\t1. Un jugador')
        print('\n\t2. Dos jugadores')
        print('\n\t   Salir (otro número)')
        return int(input('\n\tElija una opción: '))

    def un_jugador(self):
        services = ServicesPartidas()
        _nombre = input('\n----> \tIngrese su nombre: ')
        _dificultad = int(input('\n----> \tIngrese la dificultad: '))
        p = services.iniciar_partida(_nombre, _dificultad)
        res = 'Continua'
        while res == 'Continua':
            letra = input('\n----> \tIngrese una letra: ')
            if letra == 'salir':
                return True
                break
            res = services.intentar_letra(p, letra)
            print('\t', p._palabra_aciertos)
        if res == 'Gano':
            print('\n----> \tFelicitaciones {}, adivinaste!'.format(_nombre))
            return True
        elif res == 'Perdio':
            print('\n----> \tPerdiste {}, mejor suerte la próxima.'
                  .format(_nombre))
            return False

    def dos_jugadores(self):
        services = ServicesPartidas()
        _nombre1 = input('\n----> \tIngrese el nombre del jugador 1: ')
        _dificultad1 = int(input('\n----> \tIngrese la dificultad para {}: '
                                 .format(_nombre1)))
        _palabra1 = input('\n----> \t¿Qué palabra deberá adivinar '
                          '{}?: '.format(_nombre1))
        _tipo_palabra1 = input('\n----> \t¿Qué tipo de palabra es?: ')
        p1 = services.iniciar_partida(_nombre1, _dificultad1, _palabra1,
                                      _tipo_palabra1)
        res1 = 'Continua'
        while res1 == 'Continua':
            letra = input('\n----> \tIngrese una letra: ')
            if letra == 'salir':
                return True
            res1 = services.intentar_letra(p1, letra)
            print('\t', p1._palabra_aciertos)
        if res1 == 'Gano':
            print('\n----> \tFelicitaciones {}, adivinaste!'.format(_nombre1))
        elif res1 == 'Perdio':
            print('\n----> \tPerdiste {}, mejor suerte la próxima.'
                  .format(_nombre1))
        _nombre2 = input('\n----> \tIngrese el nombre del jugador 2: ')
        _dificultad2 = int(input('\n----> \tIngrese la dificultad para {}: '
                                 .format(_nombre2)))
        _palabra2 = input('\n----> \t¿Qué palabra deberá adivinar '
                          '{}?: '.format(_nombre2))
        _tipo_palabra2 = input('\n----> \t¿Qué tipo de palabra es?: ')
        p2 = services.iniciar_partida(_nombre2, _dificultad2, _palabra2,
                                      _tipo_palabra2)
        res2 = 'Continua'
        while res2 == 'Continua':
            letra = input('\n----> \tIngrese una letra: ')
            if letra == 'salir':
                return True
            res2 = services.intentar_letra(p2, letra)
            print('\t', p2._palabra_aciertos)
        if res2 == 'Gano':
            print('\n----> \tFelicitaciones {}, adivinaste!'.format(_nombre2))
        elif res2 == 'Perdio':
            print('\n----> \tPerdiste {}, mejor suerte la próxima.'
                  .format(_nombre2))
        print(RepoPartidas.partidas_list)
        return True


if __name__ == '__main__':
    juego = Ahorcado()

    while True:
        opcion_menu = juego.menu_ahorcado()
        if opcion_menu == 1:
            print('\n\tModo: Un jugador')
            juego.un_jugador()
        if opcion_menu == 2:
            print('\n\tModo: Dos jugadores')
            juego.dos_jugadores()
        else:
            break
