
def train_loop(env, dqn, buffer, epsilon, action_size, N, recorder=None):
  state = env.reset()
  done = False
  total_reward = 0
  
  VISUALIZE = recorder is not None
  
  if VISUALIZE:
    recorder.check_status()
  
  while not done:
    if VISUALIZE:
      recorder.capture(env)     
    action = dqn.select_action(epsilon, state, action_size)
    state_prime, reward, done = env.step(action)
    buffer.add_entry(state, action, reward, state_prime, done)
    total_reward += reward
    
    if(len(buffer) > 32):
      indices, batch, weights = buffer.select_random(32)
      td_errors = dqn.train(batch, weights, 0.99)
      buffer.update_priorities(indices, td_errors.detach().numpy())
      buffer.step_beta()
      
    N += 1
    if(N >= 5000):
      dqn.sync_networks()
      N = 0
    state = state_prime
  score = env.score
  if VISUALIZE:
    recorder.capture(env)
    recorder.dispatch()
  return N, epsilon, total_reward, score
  