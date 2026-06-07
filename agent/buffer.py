from collections import deque
import random

class Buffer:
  memory = deque()
  def __init__(self):
    self.memory = deque(maxlen=50000)
  def add_entry(self, s_t, a_t, r_t, s_t1, done):
    self.memory.append((s_t, a_t, r_t, s_t1, done))
  def select_random(self):
    r = random.sample(self.memory, min(len(self.memory), 32))
    return r
  def __len__(self):
    return len(self.memory)