import random as random
class Environment:
  grid_width = 600
  grid_height = 600
  accel = -500
  jump_velocity = 150
  obstacle_velocity = -150
  obstacle_width = 50
  gap_size = 100
  bird_size = 20
  dt = 1.0 / 60.0
  def __init__(self):
    self.velocity = 0
    self.x = 50
    self.y = 300
    self.obstacles = []
  def reset(self):
    self.velocity = 0
    self.y = 300
    self.obstacles = [] 
    self.generate_obstacle(200)
    self.generate_obstacle(400)
    self.generate_obstacle(600)
    state = self.get_state()
    return state
  def generate_obstacle(self, x=grid_width - obstacle_width):
    height = random.randint(50, self.grid_height - self.gap_size - 50)
    self.obstacles.append([x, height]) 
  def step(self, action):
    if action == 1:
      self.velocity = self.jump_velocity
    else:
      self.velocity = self.velocity + self.accel * self.dt
    self.y += self.velocity * self.dt
    self.y = max(0, self.y)
    self.y = min(self.y, self.grid_height)
    
    bird_left = self.x - self.bird_size / 2
    bird_right = self.x + self.bird_size / 2
    bird_top = self.y + self.bird_size / 2
    bird_bottom = self.y - self.bird_size / 2
    
    for obstacle in self.obstacles[:]:
      obstacle[0] = obstacle[0] + self.obstacle_velocity * self.dt
      if obstacle[0] + self.obstacle_width <= 0:
        self.obstacles.remove(obstacle)
        self.generate_obstacle(self.grid_width)
        continue
      if (bird_right >= obstacle[0] and bird_left <= obstacle[0] + self.obstacle_width) and (not bird_top <= obstacle[1] + self.gap_size or not bird_bottom >= obstacle[1]):
        state = self.get_state()
        return(state, -100, True)
    
    if self.y == 0:
      state = self.get_state()
      return(state, -100, True)
    state = self.get_state()
    return(state, 0.5, False)
  def get_state(self):
    next_obstacle_x = float(self.grid_width)
    next_obstacle_height = float(self.grid_height / 2)
    
    for obstacle in self.obstacles:
      if obstacle[0] + self.obstacle_width > self.x:
        next_obstacle_x = obstacle[0]
        next_obstacle_height = obstacle[1]
        break
    normalized_y = self.y / self.grid_height
    normalized_velocity = (self.velocity + 500) / 1000
    normalized_obstacle_x = max(next_obstacle_x - self.x, 0.0) / float(self.grid_width - self.x)
    normalized_obstacle_y = next_obstacle_height / self.grid_height
    
    return (normalized_y, normalized_velocity, normalized_obstacle_x, normalized_obstacle_y)
