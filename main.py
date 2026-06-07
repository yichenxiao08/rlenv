from train import train_loop
from agent.buffer import Buffer
from modules.snake.environment import Environment as snake
from modules.snake.telemetry import TelemetryRecorder as recorder
from modules.snake.renderer import Renderer
from agent.dqn import Agent as dqn
from collections import deque
import threading, time

def training(environment, agent, replay_buffer, telemetry):
  action_size = 3
  epsilon = 0.9999
  max_apples = 0
  N = 0
  for episode in range(5000):
    N, epsilon, total_reward, total_apples = train_loop(environment, agent, replay_buffer, epsilon, action_size, N, telemetry)
    epsilon = max(0.995 * epsilon, 0.01)
    max_apples = max(max_apples, total_apples)
    print(f"Episode {episode} done, epsilon: {epsilon:.3f}, reward: {total_reward:.3f}")
  print(f"Max apples: {max_apples:.3f}")

def main():
  VISUALIZE = True
  
  action_size = 3
  environment = snake()
  agent = dqn(11, action_size)
  replay_buffer = Buffer()

  if VISUALIZE:
    renderer_ready = {"ready": True}
    mutex = threading.Lock()
    
    renderer = Renderer(17, 20)
    playback_queue = deque()
    telemetry = recorder(playback_queue, renderer_ready, mutex)
    
    training_thread = threading.Thread(target=training, args=(environment, agent, replay_buffer, telemetry), daemon=True)
    training_thread.start()
    
    while True:
      if playback_queue:
        with mutex:
          renderer_ready["ready"] = False
        recorded_episode = playback_queue.popleft()
        for frame in recorded_episode:
          renderer.render_frame(frame)
        with mutex:
          renderer_ready["ready"] = True
      else:
        time.sleep(0.01)
  else:
    print("Visualization disabled. Training running at maximum hardware capacity...")
    epsilon = 0.9999
    
    for episode in range(5000): 
      N = 0
      epsilon, total_reward = train_loop(environment, agent, replay_buffer, epsilon, action_size, N, recorder=None)
      epsilon *= 0.99
      print(f"Episode {episode} done, epsilon: {epsilon:.3f}, reward: {total_reward:.3f}")

if __name__ == "__main__":
  main()