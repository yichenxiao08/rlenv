from train import train_loop
from agent.buffer import Buffer as buffer
from environments.gridworld import Environment as gridworld
from agent.dgn import Agent as dgn

state_size = 2
action_size = 4

environment = gridworld()
agent = dgn(state_size, action_size)
replay_buffer = buffer()
epsilon = 0.999
for episode in range(1000):
  epsilon, total_reward = train_loop(environment, agent, replay_buffer, epsilon, action_size)
  print(f"Episode {episode} done, epsilon: {epsilon:.3f}, reward: {total_reward:.3f}")
