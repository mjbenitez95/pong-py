import pygame

MOVEMENT_SPEED = 2

def process_player_input(movement_direction):
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        movement_direction = "UP"
      elif event.key == pygame.K_DOWN:
        movement_direction = "DOWN"
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP and movement_direction == "UP":
        movement_direction = "NONE"
      elif event.key == pygame.K_DOWN and movement_direction == "DOWN":
        movement_direction = "NONE"

  return movement_direction

def main():
  pygame.init()
  logo = pygame.image.load("logo.png")
  player_paddle = pygame.image.load("paddle.png")
  player_x = 50
  player_y = 200

  pygame.display.set_icon(logo)
  pygame.display.set_caption("MyGame")

  screen = pygame.display.set_mode((800, 600))
  screen.fill((0, 0, 0))
  screen.blit(player_paddle, (player_x, player_y))
  
  movement_direction = "NONE"
  running = True

  while running:
    screen.fill((0, 0, 0))
    screen.blit(player_paddle, (player_x, player_y))
    pygame.display.flip()

    if movement_direction == "UP" and player_y >= 15:
      player_y -= MOVEMENT_SPEED
    elif movement_direction == "DOWN" and player_y <= 425:
      player_y += MOVEMENT_SPEED

    movement_direction = process_player_input(movement_direction)

if __name__ == "__main__":
  main()
