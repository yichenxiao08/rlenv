from train import train_loop
from agent.buffer import Buffer as buffer
from agent.environment import Environment as env
from agent.dgn import Agent as dgn

environment = env()
agent = dgn()
replay_buffer = buffer()
epsilon = 0.999
for episode in range(1000):
  epsilon, total_reward = train_loop(environment, agent, replay_buffer, epsilon)
  print(f"Episode {episode} done, epsilon: {epsilon:.3f}, reward: {total_reward:.3f}")
