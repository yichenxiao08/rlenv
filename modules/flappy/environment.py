import random as random
class Environment:
  grid_width = 400
  grid_height = 600
  accel = -9.8
  jump_velocity = 5
  obstacle_velocity = -5
  obstacle_width = 50
  gap_size = 100
  dt = 1.0 / 60.0
  def __init__(self):
    self.velocity = 0
    self.x = 100
    self.y = 200
    self.obstacles = []
  def reset(self):
    self.velocity = 0
    self.y = 200
    self.obstacles = [] 
    self.generate_obstacle(200)
    self.generate_obstacle(350)
    self.generate_obstacle(500)
  def generate_obstacle(self, x= grid_height - obstacle_width):
    height = random.randint(50, self.grid_height - self.gap_size - 50)
    self.obstacles.append(x, height) 
  def step(self, action):
    if action == 1:
      self.velocity = self.jump_velocity
    else:
      self.velocity = self.velocity + self.accel * self.dt
    self.y += self.velocity * self.dt
    self.y = max(0, self.y)
    self.y = min(self.y, self.grid_height)
    
    for obstacle in self.obstacles[:]:
      obstacle[0] = obstacle[0] + self.obstacle_velocity * self.dt
      if obstacle[0] + self.obstacle_width <= 0:
        self.obstacles.remove(obstacle)
        self.generate_obstacle(self.grid_width)
      if obstacle[0] <= self.x <= obstacle[0] + 50 and not obstacle[1] <= self.y <= obstacle[1] + self.gap_size:
        state = self.get_state()
        return(state, -100, True)
    
    if self.y == 0:
      state = self.get_state()
      return(state, -100, True)
    state = self.get_state()
    return(state, 0.5, False)
  def get_state(self):
    
    for obstacle in self.obstacles:
      if obstacle[0] + self.obstacle_width > self.x:
        next_obstacle_x = obstacle[0]
        next_obstacle_height = obstacle[1]
        break
    normalized_x = self.x / self.grid_width
    normalized_y = self.y / self.grid_height
    normalized_obstacle_x = (max(next_obstacle_x - self.x, 0.0)) / self.grid_width
    normalized_obstacle_y = next_obstacle_height / self.grid_height
    return(normalized_x, normalized_y, normalized_obstacle_x, normalized_obstacle_y)
