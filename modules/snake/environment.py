import random as random
import numpy as np
from collections import deque
class Environment:
  grid_size = 17
  dir_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  def __init__(self):
    self.head = (random.randint(3, 15), random.randint(0, 16))
    head_x, head_y = self.head
    
    # self.heading_north = False
    # self.heading_east = True
    # self.heading_south = False
    # self.heading_west = False
    self.direction = 1
    
    self.steps_since_apple = 0
    
    self.snake_coordinates = deque([self.head, (self.head[0] - 1, self.head[1]), (self.head[0] - 2, self.head[1])])
    self.apple = self.generate_apple()     
    apple_x, apple_y = self.apple
    
    self.wall_north = 16 - head_y
    self.wall_east = 16 - head_x
    self.wall_south = head_y
    self.wall_west = head_x
    
    self.body_north = self.body_east = self.body_south = self.body_west = 0
    
    for bx, by in self.snake_coordinates:
      if bx == head_x:
        dy = by - head_y
        if dy > 0:
          self.body_north = max(self.body_north, 1.0 / dy)
        elif dy < 0:
          self.body_south = max(self.body_south, 1.0 / -dy)
      elif by == head_y:
        dx = bx - head_x
        if dx > 0:
          self.body_east = max(self.body_east, 1.0 / dx)
        elif dx < 0:
          self.body_west = max(self.body_west, 1.0 / -dx)
          
    self.apple_north = self.apple_east = self.apple_south = self.apple_west = 0
    
    if apple_x == head_x:
      dy = apple_y - head_y
      if dy > 0: self.apple_north = 1.0 / dy
      elif dy < 0: self.apple_south = 1.0 / -dy
    
    if apple_y == head_y:
      dx = apple_x - head_x
      if dx > 0: self.apple_east = 1.0 / dx
      elif dx < 0: self.apple_west = 1.0 / -dx
    
  def generate_apple(self):
    location = (random.randint(0, 16), random.randint(0, 16))
    while(location in self.snake_coordinates):
      location = (random.randint(0, 16), random.randint(0, 16))
    return location
  def reset(self):
    self.head = (random.randint(3, 15), random.randint(0, 16))
    self.steps_since_apple = 0
    # self.heading_north = False
    # self.heading_east = True
    # self.heading_south = False
    # self.heading_west = False
    self.direction = 1
    
    # self.danger_forward = False
    # self.danger_left = False
    # self.danger_right = False
    
    self.apple = self.generate_apple()
    
    self.snake_coordinates = deque([self.head, (self.head[0] - 1, self.head[1]), (self.head[0] - 2, self.head[1])])
    
    return self.get_state()
  
  def step(self, action):
    if(action == 1):
      self.direction = (self.direction - 1) % 4
    elif(action == 2):
      self.direction = (self.direction + 1) % 4
      
    # self.heading_north = (self.direction == 0)
    # self.heading_east = (self.direction == 1)
    # self.heading_south = (self.direction == 2)
    # self.heading_west = (self.direction == 3)
    old_dist = abs(self.head[0] - self.apple[0]) + abs(self.head[1] - self.apple[1])
    next_head = (self.head[0] + self.dir_vectors[self.direction][0], self.head[1] + self.dir_vectors[self.direction][1])
    
    hit_body = next_head in self.snake_coordinates
    if(hit_body and next_head == self.snake_coordinates[-1]):
      hit_body = False
        
    if(hit_body or not 0 <= next_head[0] <= 16 or not 0 <= next_head[1] <= 16 or self.steps_since_apple >= 200):
      state = self.get_state()
      return(state, -100, True)
    self.head = next_head
    self.snake_coordinates.appendleft(self.head)
    if(self.head == self.apple):
      self.apple = self.generate_apple()
      self.steps_since_apple = 0
      state = self.get_state()
      return(state, 10, False)
    else:
      self.snake_coordinates.pop()
      self.steps_since_apple += 1
      state = self.get_state()
      
      new_dist = abs(self.head[0] - self.apple[0]) + abs(self.head[1] - self.apple[1])
      if new_dist < old_dist:
        return (state, 0.2, False)
      else:
        return (state, -1.5, False)
      
      # if(self.direction == 0 and self.apple_north or self.direction == 1 and self.apple_east or self.direction == 2 and self.apple_south or self.direction == 3 and self.apple_west):
      #   return(state, 1, False)
      # return(state, -1, False)
  def get_state(self):
    # dir_left = (self.direction - 1) % 4
    # dir_right = (self.direction + 1) % 4
    
    # coordinate_front = (self.head[0] + self.dir_vectors[self.direction][0], self.head[1] + self.dir_vectors[self.direction][1])
    # coordinate_left = (self.head[0] + self.dir_vectors[dir_left][0], self.head[1] + self.dir_vectors[dir_left][1])
    # coordinate_right = (self.head[0] + self.dir_vectors[dir_right][0], self.head[1] + self.dir_vectors[dir_right][1])
    
    # self.danger_forward = coordinate_front in self.snake_coordinates or not 0 <= coordinate_front[0] <= 16 or not 0 <= coordinate_front[1] <= 16
    # self.danger_left = coordinate_left in self.snake_coordinates or not 0 <= coordinate_left[0] <= 16 or not 0 <= coordinate_left[1] <= 16
    # self.danger_right = coordinate_right in self.snake_coordinates or not 0 <= coordinate_right[0] <= 16 or not 0 <= coordinate_right[1] <= 16
    
    # distance_x = self.apple[0] - self.head[0]
    # distance_y = self.apple[1] - self.head[1]
    
    # self.apple_north = distance_y > 0
    # self.apple_south = distance_y < 0
    # self.apple_east = distance_x > 0
    # self.apple_west = distance_x < 0
    
    apple_x, apple_y = self.apple
    head_x, head_y = self.head

    self.wall_north = 16 - head_y
    self.wall_east = 16 - head_x
    self.wall_south = head_y
    self.wall_west = head_x
    
    self.body_north = self.body_east = self.body_south = self.body_west = 0
    
    for bx, by in self.snake_coordinates:
      if bx == head_x:
        dy = by - head_y
        if dy > 0:
          self.body_north = max(self.body_north, 1.0 / dy)
        elif dy < 0:
          self.body_south = max(self.body_south, 1.0 / -dy)
      elif by == head_y:
        dx = bx - head_x
        if dx > 0:
          self.body_east = max(self.body_east, 1.0 / dx)
        elif dx < 0:
          self.body_west = max(self.body_west, 1.0 / -dx)
          
    self.apple_north = self.apple_east = self.apple_south = self.apple_west = 0
    
    if apple_x == head_x:
      dy = apple_y - head_y
      if dy > 0: self.apple_north = 1.0 / dy
      elif dy < 0: self.apple_south = 1.0 / -dy
    
    if apple_y == head_y:
      dx = apple_x - head_x
      if dx > 0: self.apple_east = 1.0 / dx
      elif dx < 0: self.apple_west = 1.0 / -dx
      
    # return (self.heading_north, self.heading_east, self.heading_south, self.heading_west, self.danger_forward, self.danger_left, self.danger_right, self.apple_north, self.apple_east, self.apple_south, self.apple_west)
    return np.array([1.0 / self.wall_north if self.wall_north > 0 else 1.0, self.body_north, self.apple_north,
                     1.0 / self.wall_east if self.wall_east > 0 else 1.0, self.body_east, self.apple_east,
                     1.0 / self.wall_south if self.wall_south > 0 else 1.0, self.body_south, self.apple_south,
                     1.0 / self.wall_west if self.wall_west > 0 else 1.0, self.body_west, self.apple_west])