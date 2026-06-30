class SumTree:
  def __init__(self, size):
    self.size = size
    self.tree = [0] * (2 * size - 1)
    self.data = [None] * size
    self.write_ptr = 0
    self.length = 0
  def add(self, priority, data):
    index = self.write_ptr + self.size - 1
    self.data[self.write_ptr] = data
    self.update(index, priority)
    self.write_ptr = (self.write_ptr + 1) % self.size
    self.length = min(self.length + 1, self.size)
  def update(self, index, priority):
    change = priority - self.tree[index]
    self.tree[index] = priority
    while index != 0:
      index = (index - 1) // 2
      self.tree[index] += change
  def get_leaf(self, v):
    parent_index = 0
    leaf_index = 0
    while True:
      left_child = 2 * parent_index + 1
      right_child = left_child + 1
      if left_child >= len(self.tree):
        leaf_index = parent_index
        break
      if v <= self.tree[left_child]:
        parent_index = left_child
      else:
        v -= self.tree[left_child]
        parent_index = right_child
    data_index = leaf_index - self.size + 1
    return data_index, self.tree[leaf_index], self.data[data_index]
  def get_total(self):
    return self.tree[0]
  def __len__(self):
    return self.length  