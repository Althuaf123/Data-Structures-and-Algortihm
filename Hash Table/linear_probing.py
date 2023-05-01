class Hash_table:
    def __init__(self,size):
        self.size = size
        self.bucket = [[] for i in range(self.size)]
    
    def hash_value(self,key):
        hash = 0
        for i in key:
            hash +=ord(i)
        return hash % self.size
    
    def insert(self,key,value):
        
        index = self.hash_value(key)
        if self.bucket[index] == []:
            self.bucket[index].append([key,value])
        else:
            temp_hash = (index+1)%self.size
            
            while self.bucket[temp_hash]!=[] and temp_hash !=index:
                temp_hash = (temp_hash+1)%self.size
            if self.bucket[temp_hash] == []:
                self.bucket[temp_hash].append([key,value])
            else:
                print("Hash table is full")
    def get(self,key):
        index = self.hash_value(key)
        if self.bucket[index][0] == key:
            print(self.bucket[index][0][0])
        else:
            temp_hash = (index+1)%self.size
            
            while self.bucket[temp_hash][0][0]!=key and temp_hash !=index:
                temp_hash = (temp_hash+1)%self.size
            if self.bucket[temp_hash][0][0] == key :
                print(self.bucket[temp_hash][0][1])
            else:
                print("Key not found")
        
    def remove(self,key):
        index = self.hash_value(key)
        if self.bucket[index][0][0] == key:
            del self.bucket[index]
            return print("deleted the index ",index)
        else:
            temp_hash = (index +1)%self.size 
            while self.bucket[temp_hash][0][0]!= key and temp_hash != index:
                temp_hash = (temp_hash+1)%self.size
            if self.bucket[temp_hash][0][0] == key :
                del self.bucket[temp_hash]
            else:
                print("Key not found")
        return    
              
                                    
    def display(self):
        print( [value for value in self.bucket if value is not None] )

h = Hash_table(10)
h.insert('Aravind',32)
h.insert('Aravidn',88)
h.insert('kiran',26)
h.insert('kirna',29)
h.get('kirna')
h.remove('Aravidn')
h.display()