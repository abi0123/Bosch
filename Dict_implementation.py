class Hashmap:
    def __init__(slef,size=10):
        self.size=size
        self.table=[[] for _in range(size)]

    def _hash(self,key):
        return hash(key)% self.__sizeof__
    
    def put(self,key,value):
        index = self._hash(key)
        chain self.table[index]

        for pair in chain:
            if pair[o]==key:
                pair[1]=value
                return
            chain.append([key,value])

        def get(self,key):
            index = self._hash(key)
            chain= self.table[index]

            for pair in chain:
                if pair[0]== key:
                return pair[1]
            return None
        
        def remove(self,key):
            index= self._hash(key)
            chain = self.table[index]

        
           for i, pair in enumerate(chain):
            if pair[0]==key:
                del chain[i]
                return True
            return False
        
    def _str_(self):
        return str(self.table)
    
    hmap=Hashmap()
    hmap.put("apple",10)
    hmap.put("orange",11)
    hmap.put("banana",12)
    hmap.remove("banana")

    print("Hashmap",hmap)
   
        