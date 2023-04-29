class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [None for i in range(self.size)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size
    
    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = key,value

    def get(self,key):
        h = self.get_hash(key)
        print(self.arr[h])
    
    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    
    def display(self):
        return [value for value in self.arr if value is not None]
    

h = HashTable()
h.add('Pranav',26)
h.add('Neeraj',25)
h.get('Pranav')
record = h.display()
print(record)
