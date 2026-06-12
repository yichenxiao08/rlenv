import pygame, sys
class Renderer:
  def __init__(self, grid_width, grid_height):
    pygame.init()
    self.width = grid_width
    self.height = grid_height
    self.screen = pygame.display.set_mode(self.width, self.height)
    pygame.display.set_caption("Modular RL Environment - Flappy Bird")
    self.clock = pygame.time.Clock()
  def close():
    pygame.quit()
  def render_frame(self, env):
    for event in pygame.event.get():
      if event == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    self.screen.fill((135, 206, 235))
    x, y = env["bird"]
    obstacles = env["obstacles"]
    obstacle_width = env["obstacle_width"]
    obstacle_gap = env["obstacle_gap"]
    
    rect = pygame.Rect(x - 8, self.height - y - 8, 16, 16)
    pygame.draw.rect(self.screen, (255, 255, 0), rect)
    pygame.draw.rect(self.screen, (20, 80, 20), rect, 1)
    
    for obstacle in obstacles:
      obstacle_x = obstacle[0]
      obstacle_y = obstacle[1]
      rect_bottom = pygame.Rect(obstacle_x, self.height - obstacle_y, obstacle_width, self.height - obstacle_y)
      rect_top = pygame.Rect(obstacle_x, 0, obstacle_width, self.height - obstacle_y - obstacle_gap)
      pygame.draw.rect(self.screen, (0, 255, 0), rect_bottom)
      pygame.draw.rect(self.screen, (0, 255, 0), rect_top)