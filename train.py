def train_loop(env, dgn, buffer, epsilon):
  env.reset()
  state = env.reset()
  done = False
  N = 0
  total_reward = 0
  while not done:
    action = dgn.select_action(epsilon, state)
    state_prime, reward, done = env.step(action)
    buffer.add_entry(state, action, reward, state_prime, done)
    total_reward += reward
    if(len(buffer) > 32):
      batch = buffer.select_random()
      dgn.train(batch, 0.9)
    N += 1
    if(N == 1000):
      dgn.sync_networks()
      N = 0
    state = state_prime
    if len(buffer) >= 100:
      epsilon = max(0.01, epsilon * 0.999)
  return epsilon, total_reward
  