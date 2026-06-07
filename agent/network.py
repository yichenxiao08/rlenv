import torch
import torch.nn as nn

class Network(nn.Module):
  def __init__(self, state_size, action_size):
    super(Network, self).__init__()
    self.hidden_1 = nn.Linear(state_size,64)
    self.hidden_2 = nn.Linear(64,64)
    
    self.value = nn.Linear(64,1)
    self.advantage = nn.Linear(64, action_size)
  def forward(self, x):
    x = torch.relu(self.hidden_1(x))
    x = torch.relu(self.hidden_2(x))
    
    values = self.value(x)
    advantages = self.advantage(x)
    
    q_values = values + (advantages - advantages.mean(dim=1, keepdim=True))
    
    return q_values

