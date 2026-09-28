
class Queue:
  def __init__(self, cap=5):
      self._a = [None for _ in range(cap)]
      self._front = 0
      self._rare = -1
      self._c = 0

  def peek(self):
      if self._c == 0:
        return "No elements"
      return self._a[self._front]

  def enqueue(self, data):
    if self.isfull():

      print('over flow')
      return
    self._a[self._c] = data
    self._c += 1

  def rare(self):
    if self.isempty():
      return "No elements"
    return self._a[self._c-1]
  def dequeue(self):
    if self.isempty():
      return "No elements"
    temp=self._a[self._front]
    for i in range(1,self._c):
      self._a[i-1]=self._a[i]
    self._a[self._c-1]=None
    self._c-=1
    return temp
  def isempty(self):
    return self._c==0
  def isfull(self):
    return self._c==len(self._a)
  
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())
print(queue.rare())
