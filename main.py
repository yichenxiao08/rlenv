from train import train_loop
from agent.buffer import Buffer as buffer
from modules.gridworld.environment import Environment as gridworld
from modules.snake.environment import Environment as snake
from agent.dgn import Agent as dgn

state_size = 11
action_size = 3

environment = snake()
agent = dgn(state_size, action_size)
replay_buffer = buffer()
epsilon = 0.9999
for episode in range(5000):
  epsilon, total_reward = train_loop(environment, agent, replay_buffer, epsilon, action_size, 0.9999)
  print(f"Episode {episode} done, epsilon: {epsilon:.3f}, reward: {total_reward:.3f}")
