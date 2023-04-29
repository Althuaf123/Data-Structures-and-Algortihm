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
        print(index)
        if self.bucket[index] == []:
            self.bucket[index].append((key,value))
        else:
            temp_hash = (index+1)%self.size
            
            while self.bucket[temp_hash]!=[] and temp_hash !=index:
                temp_hash = (temp_hash+1)%self.size
            if self.bucket[temp_hash] == []:
                self.bucket[temp_hash].append((key,value))
            else:
                print("Hash table is full")
    def get(self,key):
        index = self.hash_value(key)
        if self.bucket[index][0] == key:
            print(self.bucket[index][0])
        else:
            temp_hash = (index+1)%self.size
            
            while self.bucket[temp_hash][0]!=key and temp_hash !=index:
                temp_hash = (temp_hash+1)%self.size
            if self.bucket[temp_hash][0] == key :
                print(self.bucket[temp_hash][1])
            else:
                print("Hash table has noe such key")
        
    def remove(self,key):
        index = self.hash_value(key)
        if self.bucket[index][0] == key:
            del self.bucket[index]
            return print("deleted the index ",index)
        else:
            temp_hash = (index +1)%self.size 
            while self.bucket[temp_hash][0]!= key and temp_hash != index:
                temp_hash = (temp_hash+1)%self.size
            if self.bucket[temp_hash][0] == key :
                del self.bucket[temp_hash]
            else:
                print("Hash table has no such key")
        return    
              
                                    
    def display(self):
        # for i in self.bucket:
        #     print(i)
        print( [value for value in self.bucket if value is not None] )

h = Hash_table(10)
h.insert('Aravind',32)
h.insert('Aravind',88)
h.insert('kiran',26)
h.insert('kiran',29)
h.display()