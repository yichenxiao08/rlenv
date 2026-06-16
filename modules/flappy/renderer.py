import pygame, sys
class Renderer:
  def __init__(self, grid_width, grid_height):
    pygame.init()
    self.width = grid_width
    self.height = grid_height
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption("Modular RL Environment - Flappy Bird")
    self.clock = pygame.time.Clock()
  def close():
    pygame.quit()
  def render_frame(self, env, speed = 60):
    for event in pygame.event.get():
      if event == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    self.screen.fill((135, 206, 235))
    x, y = env["bird"]
    obstacles = env["obstacles"]
    obstacle_width = env["obstacle_width"]
    obstacle_gap = env["obstacle_gap"]
    bird_size = env["bird_size"]
    
    rect = pygame.Rect(x - bird_size/2, self.height - y - bird_size/2, bird_size, bird_size)
    pygame.draw.rect(self.screen, (255, 255, 0), rect)
    pygame.draw.rect(self.screen, (20, 80, 20), rect, 1)
    
    for obstacle in obstacles:
      obstacle_x = obstacle[0]
      obstacle_y = obstacle[1]
      rect_bottom = pygame.Rect(obstacle_x, self.height - obstacle_y, obstacle_width, obstacle_y)
      rect_top = pygame.Rect(obstacle_x, 0, obstacle_width, self.height - obstacle_y - obstacle_gap)
      pygame.draw.rect(self.screen, (0, 255, 0), rect_bottom)
      pygame.draw.rect(self.screen, (0, 255, 0), rect_top)
    
    pygame.display.flip()
    self.clock.tick(speed)