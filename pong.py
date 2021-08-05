import pygame

def main():

  pygame.init()
  logo = pygame.image.load("logo.png")
  paddle = pygame.image.load("paddle.png")
  pygame.display.set_icon(logo)
  pygame.display.set_caption("MyGame")

  screen = pygame.display.set_mode((800, 600))

  running = True

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

if __name__ == "__main__":
  main()
