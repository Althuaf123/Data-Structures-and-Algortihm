class Hash:
    def __init__(self,size):
        self.size = size
        self.table = [None]*self.size

    def _hashing(self,key):
        return sum(ord(c) for c in key)%self.size
    
    def insert(self,key,value):
        h = self._hashing(key)
        if self.table[h] is None:
            self.table[h]=key,value
        
    def search(self,key):
        h = self._hashing(key)
        print(self.table[h][1])
    def remove(self,key):
        h = self._hashing(key)
        self.table[h]=None

    def display(self):
        return [value for value in self.table if value is not None]
    
hash = Hash(4)
hash.insert("hello",990)
hash.search("hello")
print(hash.display())