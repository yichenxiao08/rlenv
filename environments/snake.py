import random as random
from collections import deque
class Environment:
  grid_size = 17
  dir_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  def __init__(self):
    self.head = (random.randint(3, 15), random.randint(0, 16))
    
    self.heading_north = False
    self.heading_east = True
    self.heading_south = False
    self.heading_west = False
    self.direction = 1
    
    self.danger_forward = False
    self.danger_left = False
    self.danger_right = False
    
    self.apple = (random.randint(0, 16), random.randint(0, 16))
    
    self.snake_coordinates = deque([self.head, (self.head[0] - 1, self.head[1]), (self.head[0] - 2, self.head[1])])
    
    distance_x = self.head[0] - self.apple[0]
    distance_y = self.head[1] - self.apple[1]
    
    self.apple_north = True if distance_y > 0 else False
    self.apple_south = True if distance_y < 0 else False
    self.apple_east = True if distance_x > 0 else False
    self.apple_west = True if distance_x < 0 else False
    
  def reset(self):
    self.head = (random.randint(3, 15), random.randint(0, 16))
    
    self.heading_north = False
    self.heading_east = True
    self.heading_south = False
    self.heading_west = False
    self.direction = 1
    
    self.danger_forward = False
    self.danger_left = False
    self.danger_right = False
    
    self.apple = (random.randint(0, 16), random.randint(0, 16))
    
    self.snake_coordinates = [self.head, (self.head[0] - 1, self.head[1]), (self.head[0] - 2, self.head[1])]
    
    distance_x = self.head[0] - self.apple[0]
    distance_y = self.head[1] - self.apple[1]
    
    self.apple_north = True if distance_y > 0 else False
    self.apple_south = True if distance_y < 0 else False
    self.apple_east = True if distance_x > 0 else False
    self.apple_west = True if distance_x < 0 else False
  def step(self, action):
    
    if(action == 1):
      self.direction -= 1
      if(self.direction < 0):
        self.direction = 3
    if(action == 2):
      self.direction += 1
      if(self.direction > 3):
        self.direction = 0
      
    if(self.direction == 0):
      self.heading_north = True
      self.heading_east = False
      self.heading_south = False
      self.heading_west = False
      self.head[1] += 1
      self.snake_coordinates.appendleft((self.head[0], self.head[1]))
      self.snake_coordinates.pop()
      
      distance_y = self.head[1] - self.apple[1]
      
      self.apple_north = True if distance_y > 0 else False
      self.apple_south = True if distance_y < 0 else False
      
    if(self.direction == 1):
      self.heading_north = False
      self.heading_east = True
      self.heading_south = False
      self.heading_west = False
      self.head[0] += 1
      self.snake_coordinates.appendleft((self.head[0], self.head[1]))
      self.snake_coordinates.pop()
      
      distance_x = self.head[0] - self.apple[0]
      
      self.apple_east = True if distance_x > 0 else False
      self.apple_west = True if distance_x < 0 else False
      
    if(self.direction == 2):
      self.heading_north = False
      self.heading_east = False
      self.heading_south = True
      self.heading_west = False
      self.head[1] -= 1
      self.snake_coordinates.appendleft((self.head[0], self.head[1]))
      self.snake_coordinates.pop()
      
      distance_y = self.head[1] - self.apple[1]
      
      self.apple_north = True if distance_y > 0 else False
      self.apple_south = True if distance_y < 0 else False
    
    if(self.direction == 3):
      self.heading_north = False
      self.heading_east = False
      self.heading_south = False
      self.heading_west = True
      self.head[0] -= 1
      self.snake_coordinates.appendleft((self.head[0], self.head[1]))
      self.snake_coordinates.pop()

      distance_x = self.head[0] - self.apple[0]
      
      self.apple_east = True if distance_x > 0 else False
      self.apple_west = True if distance_x < 0 else False
    
    dir_left = self.direction - 1
    if(dir_left < 0):
      dir_left = 3
    dir_right = self.direction - 1
    if(dir_right > 3):
      dir_right = 0
    
    coordinate_front = (self.head[0] + self.dir_vectors[self.direction][0], self.head[1] + self.dir_vectors[self.direction][1])
    coordinate_left = (self.head[0] + self.dir_vectors[dir_left][0], self.head[1] + self.dir_vectors[dir_left][1])
    coordinate_right = (self.head[0] + self.dir_vectors[dir_right][0], self.head[1] + self.dir_vectors[dir_right][1])
    
    if(coordinate_front in self.snake_coordinates or not 0 <= coordinate_front[0] <= 16 or not 0 <= coordinate_front[1] <= 16):
      self.danger_forward = True
    if(coordinate_left in self.snake_coordinates or not 0 <= coordinate_left[0] <= 16 or not 0 <= coordinate_left[1] <= 16):
      self.danger_left = True
    if(coordinate_right in self.snake_coordinates or not 0 <= coordinate_right[0] <= 16 or not 0 <= coordinate_right[1] <= 16):
      self.danger_right = True
    
    