import os, sys
sys.path.append(os.getcwd())

""" en cada script cada vez que vaya importar una libreria local es necesario
escribir os, sys que son librerias que ayuden a buscar la carpeta en la que
estoy ejecutando el script """

from HLF.utils import config
class Tablero:
    BOARD_SIZE = config.BOARD_SIZE
    
    def __init__(self,size):
        if size is not None:
            self.BOARD_SIZE= size
        pass
    pass

if __name__=="__main__":

    tablero_player= Tablero()
    print(tablero_player)