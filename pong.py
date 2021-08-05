import pygame, random

PLAYER_START_X = 50
PLAYER_START_Y = 200
PLAYER_SPEED = 2

BALL_START_X = 390
BALL_START_Y = 290
BALL_SPEED = 2

def process_player_input(player_direction):
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player_direction = "UP"
      elif event.key == pygame.K_DOWN:
        player_direction = "DOWN"
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP and player_direction == "UP":
        player_direction = "NONE"
      elif event.key == pygame.K_DOWN and player_direction == "DOWN":
        player_direction = "NONE"
        

  return player_direction

def setup_screen(player, ball):
  screen = pygame.display.set_mode((800, 600))
  screen.fill((0, 0, 0))
  return screen

def main():
  random.seed()
  pygame.init()
  
  logo = pygame.image.load("logo.png")

  player = pygame.image.load("paddle.png")
  player_x = PLAYER_START_X
  player_y = PLAYER_START_Y

  ball = pygame.image.load("red-ball.png")
  ball_x = BALL_START_X
  ball_y = BALL_START_Y

  pygame.display.set_icon(logo)
  pygame.display.set_caption("MyGame")

  screen = setup_screen(player, ball)
  
  player_direction = "NONE"
  ball_x_direction = "LEFT"
  ball_y_direction = random.choice(["DOWN", "UP"])
  running = True

  while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (player_x, player_y))
    screen.blit(ball, (ball_x, ball_y))
    pygame.display.flip()

    if ball_y <= 0:
      ball_y_direction = "DOWN"
    elif ball_y >= 600:
      ball_y_direction = "UP"

    if player_x <= ball_x <= player_x + 25 and player_y <= ball_y <= player_y + 160:
      ball_x_direction = "RIGHT"
    elif ball_x >= 800:
      ball_x_direction = "LEFT"

    if player_direction == "UP" and player_y >= 15:
      player_y -= PLAYER_SPEED
    elif player_direction == "DOWN" and player_y <= 425:
      player_y += PLAYER_SPEED

    if ball_y_direction == "UP":
      ball_y -= BALL_SPEED
    else:
      ball_y += BALL_SPEED

    if ball_x_direction == "LEFT":
      ball_x -= BALL_SPEED
    else:
      ball_x += BALL_SPEED

    player_direction = process_player_input(player_direction)

if __name__ == "__main__":
  main()
