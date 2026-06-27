import random as random
class Environment:
  grid_width = 600
  grid_height = 600
  accel = -400
  jump_velocity = 80
  obstacle_velocity = -150
  obstacle_width = 50
  gap_size = 150
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
    self.generate_obstacle(1000)
    self.generate_obstacle(500)
    self.generate_obstacle(750)
    state, _ = self.get_state()
    return state
  def generate_obstacle(self, x=None):
    if x is None:
      if self.obstacles:
        x = max(obs[0] for obs in self.obstacles) + 250
      else:
        x = self.grid_width
    height = random.randint(50, self.grid_height - self.gap_size - 50)
    self.obstacles.append([x, height, False])
  def step(self, action, frame_skip=6):
    total_reward = 0
    final_state = None
    done = False
    for _ in range(frame_skip):
        state, reward, done = self._step_single(action)
        total_reward += reward
        final_state = state
        if done:
            break
    return final_state, total_reward, done

  def _step_single(self, action):
    bonus = 0
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
        self.generate_obstacle()
        continue
      if (bird_right >= obstacle[0] and bird_left <= obstacle[0] + self.obstacle_width) and (not bird_top <= obstacle[1] + self.gap_size or not bird_bottom >= obstacle[1]):
        state, _ = self.get_state()
        return(state, -1.0, True)
      if obstacle[0] + self.obstacle_width < bird_left and not obstacle[2]:
        obstacle[2] = True
        bonus = 1
    if bird_bottom <= 0:
      state, _ = self.get_state()
      return(state, -1.0, True)
    state, distance = self.get_state()
    distance = 1 - min(distance, 1.0)
    return (state, 0.1 + bonus + distance * 0.1, False)
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
    normalized_obstacle_y = (next_obstacle_height + self.gap_size / 2) / self.grid_height
    
    return (normalized_y, normalized_velocity, normalized_obstacle_x, normalized_obstacle_y), abs(normalized_obstacle_y - normalized_y)
