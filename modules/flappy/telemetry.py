class TelemetryRecorder:
  def __init__(self, playback_queue, renderer_ready, data_lock):
    self.queue = playback_queue
    self.signal = renderer_ready
    self.mutex = data_lock
    self.record = False
    self.current_episode = []
  def check_status(self):
    with self.mutex:
      self.record = self.signal["ready"]
      if self.record:
        self.signal["ready"] = False
    self.current_episode = []
  def capture(self, env):
    if not self.record:
      return

    snapshot = {
      "bird": tuple((env.x, env.y)),
      "obstacles": list(env.obstacles)
    }
    self.current_episode.append(snapshot)
    
  def dispatch(self):
    if self.record and self.current_episode:
      self.queue.append(self.current_episode)
    self.record = False