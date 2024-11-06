class circularQueue:
    def __init__(self, capacity):
         if capacity < 0:
             raise Exception ("A queue of size should not be negative!")
         self.capacity = capacity
         self.first = self.last = -1
         self.queue = [None] * self.capacity
         self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capactiy

    def clear_queue(self):
        self.first = self.last = -1

    def enqueue(self, item):
        if self.is_full():
         raise Exception ("Queue is full!")
        elif self.is_empty():
            self.first = self.last = 0
        elif self.last == self.capacity-1:
            self.last = 0
        else:
           self.last += 1
        self.queue[self.last] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is full!')

        data = self.queue[self.first]
        if self.first == self.last:
            self.first =  self.last = -1
            return data

        self.first = (self.first + 1) % self.capacity
        self.count -= 1
        return data

    def display(self):
        if self.is_empty():
            print("Empty")
            return
        elif self.last > self.first:
            print(self.queue[self.first: self.last+1])
            return
        else:
            print(self.queue[self.first: self.capacity] + self.queue[0:self.last+1])


