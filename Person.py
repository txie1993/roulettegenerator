class Person:
  def __init__(self, name, history, is_treasurer=False):
    self.name = name
    self.history = history
    self.is_treasurer = is_treasurer

  def add_history(self, name, times=1):
    if not self.history.get(name):
      self.history[name] = times
      return self.history[name]
    self.history[name] += times
    return self.history[name]