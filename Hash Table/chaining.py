class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [[] for i in range(self.size)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size
    
    def add(self,key,value):
        h = self.get_hash(key)
        found = False
        for index,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def get(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] ==  key:
                return element[1]
    
    def delete(self,key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if index[0] == key:
                del self.arr[h][index]
        
    def display(self):
        return [value for value in self.arr if value is not None]
    

h = HashTable()
h.add('Pranav',26)
h.add('ranavP',45)
h.add('Neeraj',25)
h.get('Pranav')
record = h.display()
print(record)
