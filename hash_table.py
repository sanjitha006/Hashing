from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        pass
    
    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        pass
    
    def get_load(self):
        pass
    
    def __str__(self):
        pass
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    

    
class HashSet(HashTable):
    def __init__(self, collision_type, params):#params as a list
        self.collision_type=collision_type
        self.params=params
        self.occupied_count=0
        if(self.collision_type=="Chain"):
            self.hash_set=[[] for i in range(params[-1])]
        else:
            self.hash_set=[-1 for i in range(params[-1])]

    def insert(self, key):
        found=0
        set=0
        if(self.collision_type=="Linear"):
            if(False):
                pass
                

            else:
                s=self.get_slot(key)
                t=self.params[-1]
                if(self.hash_set[s]==-1):
                    self.hash_set[s]=key
                    self.occupied_count+=1
                    set=1
                elif(self.hash_set[s]==key):
                    found=1
                    pass
                else:
                    a=(s+1)%t
                    while(a!=s):
                        if(self.hash_set[a]==key):
                            found=1
                            break
                        elif(self.hash_set[a]==-1):
                            self.hash_set[a]=key#exception raising add at last if table size not enough
                            self.occupied_count+=1
                            set=1
                            break
                        a=(a+1)%t
                if(found==0 and set==0):
                    raise Exception("table is full")

        elif(self.collision_type=="Double"):
            if(False):
                pass

            else:
                
                s=self.get_slot(key)
                t=self.params[-1]
                if(self.hash_set[s]==-1):
                    self.hash_set[s]=key
                    self.occupied_count+=1
                    set=1
                elif(self.hash_set[s]==key):
                    found=1
                    pass
                else:
                    h2=self.hash2(key)
                    a=(s+h2)%t
                    while(a!=s):
                        if(self.hash_set[a]==key):
                            found=1
                            break
                        elif(self.hash_set[a]==-1):
                            self.hash_set[a]=key
                            self.occupied_count+=1
                            set=1
                            break
                        a=(a+h2)%t
                if(found==0  and set==0):
                    raise Exception("table is full")
        else:

            s=self.get_slot(key)
            if(key not in self.hash_set[s]):
                self.hash_set[s].append(key)
                self.occupied_count+=1
                
            



    
    def find(self, key):
        if(self.collision_type=="Linear"):
            s=self.get_slot(key)
            t=self.params[-1]
            if(self.hash_set[s]==key):return True
            a=(s+1)%t
            while(a!=s and self.hash_set[a]!=-1):
                if(self.hash_set[a]==key):return True
                a=(a+1)%t
            return False
        elif(self.collision_type=="Double"):
            s=self.get_slot(key)
            t=self.params[-1]
            if(self.hash_set[s]==key):return True
            h2=self.hash2(key)
            a=(s+h2)%t
            while(a!=s and self.hash_set[a]!=-1):
                if(self.hash_set[a]==key):return True
                a=(a+h2)%t
            return False
        else:
            s=self.get_slot(key)
            for i in self.hash_set[s]:
                if(i==key):
                    return True
            return False
    def distict_items_list(self):
        res=[]
        if(self.collision_type!="Chain"):
            for i in self.hash_set:
                if(i!=-1):
                    res.append(i)
        else:
            for i in self.hash_set:
                for j in i:
                    res.append(j)
        return res
    def distinct_print(self):

        t=" "
   
        for i in self.distict_items_list():
            t=t+i+" | "
        t=t.rstrip(" | ")
      
        print(t)
        


        
    def get_slot(self, key):
        temp=1
        z=self.params[0]
        t=self.params[-1]
        res=0
        for i in range(len(key)):
            if(ord(key[i])>=97):
                p=ord(key[i])-97
            else:
                p=ord(key[i])-39
            res=((res+p*temp)%(t))
            temp=temp*z
        res=res%t
        return res

    
    def get_load(self):
        res=(self.occupied_count/self.params[-1])#how ro calculate for chaining
        return res
        
    
    def __str__(self):
        res=""
        if(self.collision_type!="Chain"):
            for i in self.hash_set:
                if(i==-1):
                    res+="<EMPTY> | "
                    
                else:
                    res+=i
                    res+=" | "
            res=res.rstrip(" | ")

        else:
            for i in self.hash_set:
                if (len(i)==0):
                    res+="<EMPTY> | "
                else:
                    for j in i:
                        res+=j
                        res+=" ; "
                    res=res.rstrip(" ; ")
                    res+=" | "
            
            res=res.rstrip(" | ")
        return res
            


    def hash2(self,key):
        z2=self.params[1]
        c2=self.params[2]
        t=self.params[-1]
        res=0
        temp=1
        for i in range(len(key)):
            if(ord(key[i])>=97):
                p=ord(key[i])-97
            else:
                p=ord(key[i])-39
            res=((res+p*temp)%(c2))
            temp=temp*z2
        res=res%c2
        res=(c2-(res))
        return res




    
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        self.collision_type=collision_type
        self.params=params
        self.occupied_count=0
        if(self.collision_type=="Chain"):
            self.hash_map=[[] for i in range(params[-1])]
        else:
            self.hash_map=[(-1,-1) for i in range(params[-1])]



    def insert(self, x):
        # x = (key, value)
        found=0
        set=0
        key=x[0]
        if(self.collision_type=="Linear"):
            if(False):pass

            else:
                s=self.get_slot(key)
                t=self.params[-1]
                if(self.hash_map[s][0]==key):
                    found=1
                    pass
                elif(self.hash_map[s][0]==-1):
                    self.hash_map[s]=x
                    self.occupied_count+=1
                    set=1
                
                else:
                    a=(s+1)%t
                    while(a!=s):
                        if(self.hash_map[a][0]==x[0]):
                            found=1
                            break
                        elif(self.hash_map[a][0]==-1):
                            self.hash_map[a]=x#exception raising add at last if table size not enough
                            self.occupied_count+=1
                            set=1
                            break
                        a=(a+1)%t
                if(found==0 and set==0):
                    raise Exception("table is full")
        elif(self.collision_type=="Double"):
            if(False):
                pass

            else:
                s=self.get_slot(key)
                t=self.params[-1]
                if(self.hash_map[s][0]==key):
                    found=1
                    pass
                elif(self.hash_map[s][0]==-1):
                    self.hash_map[s]=x
                    self.occupied_count+=1
                    set=1
                
                else:
                    h2=self.hash2(key)
                    a=(s+h2)%t
                    while(a!=s):
                        if(self.hash_map[a][0]==key):
                            found=1
                            break
                        elif(self.hash_map[a][0]==-1):
                            self.hash_map[a]=x
                            self.occupied_count+=1
                            set=1
                            break
                        a=(a+h2)%t
                if(found==0 and set==0):
                    raise Exception("table is full")
        else:
            s=self.get_slot(key)
            found=0
            for i in self.hash_map[s]:
                if(i[0]==key):
                    found=1
                    break
            if(found==0):
                self.hash_map[s].append(x)
                self.occupied_count+=1
    
    def find(self, key):
        if(self.collision_type=="Linear"):
            s=self.get_slot(key)
            t=self.params[-1]
      
            if(self.hash_map[s][0]==key):return self.hash_map[s][1]
            a=(s+1)%t
            while(a!=s and self.hash_map[a]!=-1):
                if(self.hash_map[a][0]==key):return self.hash_map[a][1]
                a=(a+1)%t
            return None
        elif(self.collision_type=="Double"):
            s=self.get_slot(key)
            t=self.params[-1]
            if(self.hash_map[s][0]==key):return self.hash_map[s][1]
            h2=self.hash2(key)
            a=(s+h2)%t
            while(a!=s and self.hash_map[a]!=-1):
                if(self.hash_map[a][0]==key):return self.hash_map[a][1]
                a=(a+h2)%t
            return None
        else:
            s=self.get_slot(key)
            for i in self.hash_map[s]:
                if(i[0]==key):
                    return i[1]
            return None
    
    def get_slot(self, key):
        temp=1
        z=self.params[0]
        t=self.params[-1]
        res=0
        for i in range(len(key)):
            if(ord(key[i])>=97):
                p=ord(key[i])-97
            else:
                p=ord(key[i])-39
            res=((res+p*temp)%(t))
            temp=temp*z
        res=res%t
        return res
    
    def get_load(self):
        res=(self.occupied_count/self.params[-1])#how ro calculate for chaining
        return res
    
    def __str__(self):
        res=""
        if(self.collision_type!="Chain"):
            for i in self.hash_map:
                if(i==-1):
                    res+="<EMPTY> | "
                    
                else:
                    res+=str(i)
                    res+=" | "
            res=res.rstrip(" | ")

        else:
            for i in self.hash_map:
                if (len(i)==0):
                    res+="<EMPTY> | "
                else:
                    for j in i:
                        res+=str(j)
                        res+=" ; "
                    res=res.rstrip(" ; ")
                    res+=" | "
            
            res=res.rstrip(" | ")
        return res

    def hash2(self,key):
        z2=self.params[1]
        c2=self.params[2]
        t=self.params[-1]
        res=0
        temp=1
        for i in range(len(key)):
            if(ord(key[i])>=97):
                p=ord(key[i])-97
            else:
                p=ord(key[i])-39
            res=((res+p*temp)%(c2))
            temp=temp*z2
        res=res%c2
        res=(c2-(res))
        return res
    





