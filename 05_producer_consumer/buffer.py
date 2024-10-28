class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.producer_index = 0
        self.consumer_index = 0

    def add(self, value):
        if self.is_full():
            raise Exception("Buffer is full")
        
        self.buffer[self.producer_index] = value
        self.producer_index = (self.producer_index + 1) % self.capacity
        self.size += 1

    def delete(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        
        value = self.buffer[self.consumer_index]
        self.buffer[self.consumer_index] = None
        self.consumer_index = (self.consumer_index + 1) % self.capacity
        self.size -= 1
        return value
    
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0