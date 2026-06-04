import random
import torch
from torch import nn
from torch import optim
from agent.network import Network

class Agent:
  def __init__(self):
    self.training_network = Network()
    self.frozen_network = Network()
    self.loss = nn.MSELoss()
    self.optimizer = optim.Adam(self.training_network.parameters(), lr=0.001)
    self.frozen_network.load_state_dict(self.training_network.state_dict())
  
  def select_action(self, epsilon, state):
    r = random.random()
    if(r < epsilon):
      action = random.randint(0,3)
      return action
    else:
      state_tensor = torch.tensor(state, dtype=torch.float32)
      output = self.training_network(state_tensor)
      return torch.argmax(output).item()
  
  def sync_networks(self):
    self.frozen_network.load_state_dict(self.training_network.state_dict())
    
  def train(self, batch, gamma):
    states, actions, rewards, state_primes, dones = zip(*batch)
    states = torch.tensor(states, dtype=torch.float32)
    actions = torch.tensor(actions, dtype=torch.long)
    rewards = torch.tensor(rewards, dtype=torch.float32)
    state_primes = torch.tensor(state_primes, dtype=torch.float32)
    dones = torch.tensor(dones, dtype=torch.float32)
    
    with torch.no_grad():
      q_primes = self.frozen_network(state_primes).max(dim=1).values
      
    target = rewards + gamma * q_primes * (1 - dones)
    predictions = self.training_network(states)
    actions = actions.unsqueeze(1)
    predictions = torch.gather(predictions, 1, actions).squeeze(1)
    output = self.loss(predictions, target)
    
    self.optimizer.zero_grad()
    output.backward()
    self.optimizer.step()

    