class Environment:
  goal_x = 4
  goal_y = 4
  grid_size = 5
  walls = [(1,1), (1,2), (2,2)]
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.step_count = 0
  def update(self, action):
    new_x = self.x
    new_y = self.y
    if(action == 0):
      new_y += 1
    elif(action == 1):
      new_x += 1
    elif(action == 2):
      new_y -= 1
    elif(action == 3):
      new_x -= 1
    self.step_count += 1
    if(new_x >= 0 and new_x < self.grid_size and new_y >= 0 and new_y < self.grid_size and (new_x, new_y) not in self.walls):
      self.x = new_x
      self.y = new_y
    if(self.x == self.goal_x and self.y == self.goal_y):
      return((self.x, self.y), 0, True)
    if(self.step_count == 30):
      return((self.x, self.y), -1, True)
    else:
      return((self.x, self.y), -1, False)
    
  
  