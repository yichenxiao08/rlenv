import pygame, sys

class Renderer:
  def __init__(self, grid_size, cell_size):
    pygame.init()
    
    self.grid_size = grid_size
    self.cell_size = cell_size
    self.window_size = self.grid_size * self.cell_size
    self.screen = pygame.display.set_mode((self.window_size, self.window_size))
    pygame.display.set_caption("Modular RL Environment")
    
  def render_frame(self):
    self.screen.fill(WHITE)
    
    
    