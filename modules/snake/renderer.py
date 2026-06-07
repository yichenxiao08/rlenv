import pygame, sys

class Renderer:
  def __init__(self, grid_size, cell_size):
    pygame.init()
    
    self.grid_size = grid_size
    self.cell_size = cell_size
    self.window_size = self.grid_size * self.cell_size
    self.screen = pygame.display.set_mode((self.window_size, self.window_size))
    pygame.display.set_caption("Modular RL Environment")
    self.clock = pygame.time.Clock()
    
  def render_frame(self, env, speed = 15):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    
    
    self.screen.fill((18, 18, 24)) 
    
    for i in range(self.grid_size + 1):
      pygame.draw.line(self.screen, (28, 28, 36), (i * self.cell_size, 0), (i * self.cell_size, self.window_size))
      pygame.draw.line(self.screen, (28, 28, 36), (0, i * self.cell_size), (self.window_size, i * self.cell_size))
        
    body_segments = list(env["body"])[1:]
    for segment in body_segments:
      rect = pygame.Rect(segment[0] * self.cell_size, (self.grid_size - segment[1] - 1) * self.cell_size, self.cell_size, self.cell_size)
      pygame.draw.rect(self.screen, (34, 139, 34), rect)
      pygame.draw.rect(self.screen, (20, 80, 20), rect, 1)

    head_rect = pygame.Rect(env["head"][0] * self.cell_size, (self.grid_size - env["head"][1] - 1) * self.cell_size, self.cell_size, self.cell_size)
    pygame.draw.rect(self.screen, (46, 232, 126), head_rect)

    apple_rect = pygame.Rect(env["apple"][0] * self.cell_size, (self.grid_size - env["apple"][1] - 1) * self.cell_size, self.cell_size, self.cell_size)
    pygame.draw.rect(self.screen, (225, 40, 70), apple_rect)

    pygame.display.flip()
    self.clock.tick(speed)
  def close(self):
    pygame.quit()
    
    