from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        p=get_next_size()
        if self.collision_type=="Linear":
            new_set=[-1 for i in range(p)]
            c=(self.params[0],self.params[1],p)
            self.params=c
            for key in self.hash_set:
                if(key!=-1):
                    s=self.get_slot(key)
                    t=p
                    if(new_set[s]==-1):
                        new_set[s]=key
                  
                    elif(new_set[s]==key):
                        
                        pass
                    else:
                        a=(s+1)%t
                        while(a!=s):
                            if(new_set[a]==key):
                              
                                break
                            elif(new_set[a]==-1):
                                new_set[a]=key#exception raising add at last if table size not enough
                             
                                break
                            a=(a+1)%t
            self.hash_set=new_set
            
        elif self.collision_type=="Double":
            new_set=[-1 for i in range(p)]
            c=(self.params[0],self.params[1],self.params[2],p)
            self.params=c
            for key in self.hash_set:
                if(key!=-1):
                    s=self.get_slot(key)
                    t=self.params[-1]
                    if(new_set[s]==-1):
                        new_set[s]=key
                      
                      
                    elif(new_set[s]==key):
                        
                        pass
                    else:
                        h2=self.hash2(key)
                        a=(s+h2)%t
                        while(a!=s):
                            if(new_set[a]==key):
                             
                                break
                            elif(new_set[a]==-1):
                                new_set[a]=key
                    
                                break
                            a=(a+h2)%t
            self.hash_set=new_set
            
        elif (self.collision_type=="Chain"):
            new_set=[[] for i in range(p)]
            c=(self.params[0],self.params[1],p)
            self.params=c
            for i in self.hash_set:
                for key in i:
                    s=self.get_slot(key)
            
                    new_set[s].append(key)
            self.hash_set=new_set
        
                
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            





class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        p=get_next_size()
        if(self.collision_type=="Linear"):
            new_map=[(-1,-1) for i in range(p)]
            c=(self.params[0],self.params[1],p)
            self.params=c
            for x in self.hash_map:
                key=x[0]
                if(key!=-1):

                    s=self.get_slot(key)
                    t=self.params[-1]
                    if(new_map[s][0]==key):
                        
                        pass
                    elif(new_map[s][0]==-1):
                        new_map[s]=x
                        
                    
                    else:
                        a=(s+1)%t
                        while(a!=s):
                            if(new_map[a][0]==x[0]):
                             
                                break
                            elif(new_map[a][0]==-1):
                                new_map[a]=x#exception raising add at last if table size not enough
                              
                                break
                            a=(a+1)%t
            self.hash_map=new_map
        elif self.collision_type=="Double":
            new_map=[(-1,-1) for i in range(p)]
            c=(self.params[0],self.params[1],self.params[2],p)
            self.params=c
            for x in self.hash_map:
                key=x[0]
                if(key!=-1):
                    s=self.get_slot(key)
                    t=self.params[-1]
                    if([s][0]==key):
                        
                        pass
                    elif(new_map[s][0]==-1):
                        new_map[s]=x
                        
                    
                    else:
                        h2=self.hash2(key)
                        a=(s+h2)%t
                        while(a!=s):
                            if(new_map[a][0]==key):
                             
                                break
                            elif(new_map[a][0]==-1):
                                new_map[a]=x
                               
                                break
                            a=(a+h2)%t
            self.hash_map=new_map
        elif (self.collision_type=="Chain"):
            new_map=[[] for i in range(p)]
            c=(self.params[0],self.params[1],p)
            self.params=c
            for i in self.hash_map:
                
                for j in i:
                    key=j[0]
                    s=self.get_slot(key)
            
                    new_map[s].append(j)
            self.hash_map=new_map

        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()