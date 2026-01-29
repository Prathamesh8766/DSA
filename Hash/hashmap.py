class Hashmaps:
    def _init_(self, capacity):
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
    
    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def rehash(self, old_hash_value):
        return (old_hash_value + 1) % self.capacity     # Linear probing to avoid collision
    
    def insert(self, key, value):
        hash_value = self.hash_function(key)
        initial_index = hash_value
        
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.values[hash_value] = value
        
        else:
            if self.slots[hash_value] == key:
                self.values[hash_value] = value
                return
            else:
                new_hash_value = self.rehash(hash_value)
                while self.slots[new_hash_value] is not None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)
                    
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.values[new_hash_value] = value
                else:
                    self.values[new_hash_value] = value


                            