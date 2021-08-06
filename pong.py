import pygame, random, time, sys

CPU_START_X = 725
CPU_START_Y = 200
CPU_SPEED = 3

PLAYER_START_X = 50
PLAYER_START_Y = 200
PLAYER_SPEED = 4

BALL_START_X = 390
BALL_START_Y = 290
BALL_SPEED = 4

FPS = 90

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
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  return player_direction

def setup_screen(player, ball):
  screen = pygame.display.set_mode((800, 600))
  screen.fill((0, 0, 0))
  return screen

def main():
  random.seed()
  pygame.init()
  pygame.font.init()
  fps_clock = pygame.time.Clock()

  my_font = pygame.font.SysFont('Times New Roman', 30)
  logo = pygame.image.load("logo.png")

  player = pygame.image.load("paddle.png")
  player_x = PLAYER_START_X
  player_y = PLAYER_START_Y

  cpu = pygame.image.load("paddle.png")
  cpu_x = CPU_START_X
  cpu_y = CPU_START_Y

  ball = pygame.image.load("red-ball.png")
  ball_x = BALL_START_X
  ball_y = BALL_START_Y

  pygame.display.set_icon(logo)
  pygame.display.set_caption("MyGame")

  screen = setup_screen(player, ball)
  
  player_direction = "NONE"
  ball_x_direction = "RIGHT"
  ball_y_direction = random.choice(["DOWN", "UP"])
  running = True

  while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (player_x, player_y))
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(cpu, (cpu_x, cpu_y))
    pygame.display.flip()

    if ball_y <= 0:
      ball_y_direction = "DOWN"
    elif ball_y >= 600:
      ball_y_direction = "UP"

    if player_x <= ball_x <= player_x + 25 and player_y <= ball_y <= player_y + 160:
      ball_x_direction = "RIGHT"
    elif cpu_x <= ball_x <= cpu_x + 25 and cpu_y <= ball_y <= cpu_y + 160:
      ball_x_direction = "LEFT"

    if player_direction == "UP" and player_y >= 15:
      player_y -= PLAYER_SPEED
    elif player_direction == "DOWN" and player_y <= 425:
      player_y += PLAYER_SPEED

    if ball_y < (cpu_y + 80) and cpu_y >= 15:
      cpu_y -= CPU_SPEED
    elif ball_y > (cpu_y + 80) and cpu_y <= 425:
      cpu_y += CPU_SPEED

    if ball_y_direction == "UP":
      ball_y -= BALL_SPEED
    else:
      ball_y += BALL_SPEED

    if ball_x_direction == "LEFT":
      ball_x -= BALL_SPEED
    else:
      ball_x += BALL_SPEED

    if ball_x <= 0 or ball_x >= 800:
      if ball_x <= 0:
        text_surface = my_font.render( "CPU Wins!", False, (255, 255, 255))
      else:
        text_surface = my_font.render( "Player Wins!", False, (255, 255, 255))
      screen.blit(text_surface, (BALL_START_X - 75, BALL_START_Y - 50))
      pygame.display.flip()
      running = False

    player_direction = process_player_input(player_direction)
    fps_clock.tick(FPS)

  time.sleep(3)

if __name__ == "__main__":
  main()
