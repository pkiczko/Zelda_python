#pip3 install pygbag --user --upgrade
#przenieslismy zawartosc folderu code poziom wyzej (by te pliki byly luzem w folderze projektu)
#by odpalic pygame:
#w terminalu wychodzimy z folderu projektu (poziom wyzej):
#cd ..
#teraz odpalamy pygbag-a wskazujac folder projektu:
#py -m pygbag .\Zelda_python (gdzie Zelda_python to nazwa folderu)
#po pomyslnym wykonaniu odpala sie lokalny serwer www, gdzie projekt mozna podejrzec pod linkiem:
# http://localhost:8000
import pygame, sys
import asyncio
from settings import *
from level import Level
from debug import debug

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda 2000')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	async def run(self):
		while True:
			await asyncio.sleep(0)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			debug('')
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	asyncio.run(game.run())