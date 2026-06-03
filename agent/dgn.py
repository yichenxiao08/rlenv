import random
import torch
import numpy as np
from network import Network

training_network = Network()
frozen_network = Network()

def select_action(epsilon, state):
  r = random.random()
  if(r < epsilon):
    action = random.randint(0,3)
    return action
  else:
    output = training_network(state)
    return np.argmax(output)
  
def train(batch):
  states, actions, rewards, state_primes, dones = zip(*batch)
  states = torch.tensor(states, dtype=torch.float32)
  actions = torch.tensor(actions, dtype=torch.long)
  rewards = torch.tensor(rewards, dtype=torch.float32)
  state_primes = torch.tensor(state_primes, dtype=torch.float32)
  dones = torch.tensor(dones, dtype=torch.float32)