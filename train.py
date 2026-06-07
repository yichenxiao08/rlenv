
def train_loop(env, dqn, buffer, epsilon, action_size, N, recorder=None):
  state = env.reset()
  done = False
  total_reward = 0
  total_apples = 0
  
  VISUALIZE = recorder is not None
  
  if VISUALIZE:
    recorder.check_status()
  
  while not done:
    if VISUALIZE:
      recorder.capture(env)     
    action = dqn.select_action(epsilon, state, action_size)
    state_prime, reward, done, apples = env.step(action)
    total_apples += apples
    buffer.add_entry(state, action, reward, state_prime, done)
    total_reward += reward
    
    if(len(buffer) > 32):
      batch = buffer.select_random()
      dqn.train(batch, 0.99)
    N += 1
    if(N >= 1000):
      dqn.sync_networks()
      N = 0
    state = state_prime
  if VISUALIZE:
    recorder.dispatch()
  return N, epsilon, total_reward, total_apples
  