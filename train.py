from agent.environment import Environment as env
from agent.buffer import Buffer as buffer
import random
import agent.dgn as dgn

def train_loop():
  env.__init__()
  state = env.reset()
  done = False
  epsilon = 0.99
  while not done:
    action = dgn.select_action(epsilon, state)
    state_prime, reward, done = env.step(action)
    buffer.add_entry(state, action, reward, state_prime)
    
    if(len(buffer) > 32):
      batch = buffer.select_random()
      dgn.train(batch)
    
  