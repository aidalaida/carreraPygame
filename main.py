import pygame
import sys

class Game():
    
    corredores = []
    
    def __init__(self): #estructura pantalla, fondo, enemigos, jugadores
        
        self.__screen = pygame.display.set_mode((640,480)) #crear pantalla en pygame, ((tammaño en una tupla, x, y))
        pygame.display.set_caption("Carrera de bichos") #Pantalla ponerle un titulo
        self.background = pygame.image.load("images/background.png") #Cargar imagen de fondo de la pantalla. (ponemos la direccion de donde esta guardada la foto)
        
        self.runner = pygame.image.load("images/smallball.png")
            
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while True: #vaciando los eventos
            #comprobación eventos
            for event in pygame.event.get(): #metodo. atributo event tiene un metodo get(), event es un objetos (listener/escuchador de eventos). iterable desd la última comprobación
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #refresacr / renderizar la pantalla
            self.__screen.blit(self.background, (0,0)) #blit -> pintar el fondo con lo que hay en self.background. Con tupla de coordenadas
            self.__screen.blit(self.runner, (x,240))
            pygame.display.flip() #refresca
            
            x += 3
            if x >= 250:
                hayGanador = True
        
        pygame.quit()
        sys.exit() #Para acabar


if __name__ == '__main__':
    pygame.init() #comando para que funciones
    game = Game()
    game.competir()