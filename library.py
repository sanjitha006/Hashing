import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary():
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        
        def merge(arr,l,m,r):
            temp=[]
            i=l
            j=m
            while(i<m and j<r):
                if(arr[i]<arr[j]):
                    temp.append(arr[i])
                    i+=1
                elif(arr[i]>arr[j]):
                    temp.append(arr[j])
                    j+=1
                else:
                    temp.append(arr[i])
                    temp.append(arr[j])
                    i+=1
                    j+=1
            while(i<m):
                temp.append(arr[i])
                i+=1
            while(j<r):
                temp.append(arr[j])
                j+=1
        
            arr[l:r]=temp
                
          
        def merge_sort(arr,l,r):
            if(r>l+1):
                m=l+(r-l)//2
                merge_sort(arr,l,m)
                merge_sort(arr,m,r)
                merge(arr,l,m,r)
            
      
        book_texts = [[book_titles[i], texts[i]] for i in range(len(book_titles))]
        #book_texts = [[book_titles[i], texts[i] if isinstance(texts[i], list) else [texts[i]]] for i in range(len(book_titles))]

        merge_sort(book_texts, 0, len(book_texts))
    
        self.book_texts = []
        for i in range(len(book_texts)):
            sorted_texts=book_texts[i][1].copy()
            merge_sort(sorted_texts,0,len(sorted_texts))
        
            unique_texts = []
            if sorted_texts:
                unique_texts.append(sorted_texts[0])

                for j in range(1, len(sorted_texts)):
                    if sorted_texts[j] != sorted_texts[j - 1]: 
                        unique_texts.append(sorted_texts[j])
            
            self.book_texts.append([book_texts[i][0], unique_texts])  

    def b_s2(self, x, arr, l, h):
        if l >= h:
            if arr[l] == x:
                return l
            else:
                return -1
        m = l + (h - l) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x:
            return self.b_s2(x, arr, l, m - 1)
        else:
            return self.b_s2(x, arr, m + 1, h)


    def b_s1(self,x,arr,l,h):
        if(l>=h):
            if(arr[l][0]==x):
                return l
            else:
                return -1
        m=l+(h-l)//2
        if(arr[m][0]==x):
            return m
        elif(arr[m][0]>x):
            return(self.b_s1(x,arr,l,m-1))
        else:
            return(self.b_s1(x,arr,m+1,h))
        
    def distinct_words(self, book_title):
        #write binary search function outside so that can be used by all methods. 
        x=self.b_s1(book_title,self.book_texts,0,len(self.book_texts)-1)
        if(x==-1):
            return []#check is to raise exception of book not present or just return empty list
        else:
            #print(self.book_texts[x][1])
            return(self.book_texts[x][1])

    def count_distinct_words(self, book_title):
        x=self.b_s1(book_title,self.book_texts,0,len(self.book_texts)-1)
        if(x==-1):
            return 0 #check if book not preesnt error or 0
        else:
            return(len(self.book_texts[x][1]))
        
    
    def search_keyword(self, keyword):
        res=[]
        for i in self.book_texts:
   
            if((self.b_s2(keyword,i[1],0,len(i[1])-1))!=-1):
                res.append(i[0])
        return res
    
    def print_books(self):
        
        for i in self.book_texts:
            res=""
            res+=(i[0]+":"+" ")
            res+=(i[1][0]+" ")
            for j in range(1,len(i[1])):
                res+=("|"+" ")
                res+=(i[1][j]+" ")
            res=res.rstrip(" ")
            print(res)   
        



class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.params=params
        if(name=="Jobs"):
            self.c_type="Chain"
            self.book_texts=ht.HashMap("Chain",params)
        elif(name=="Gates"):
            self.c_type="Linear"
            self.book_texts=ht.HashMap("Linear",params)
        elif(name=="Bezos"):
            self.c_type="Double"
            self.book_texts=ht.HashMap("Double",params)
        
    
    def add_book(self, book_title, text):
        y=ht.HashSet(self.c_type,self.params)
        for i in text:
            y.insert(i)

        self.book_texts.insert((book_title,y))
  
    def distinct_words(self, book_title):
        text_of_the_book=self.book_texts.find(book_title)
        if(text_of_the_book==None):return []
        return(text_of_the_book.distict_items_list())
    

    
    def count_distinct_words(self, book_title):
        text_of_the_book=self.book_texts.find(book_title)
        return(text_of_the_book.occupied_count)
    
    def search_keyword(self, keyword):
        res=[]
        if(self.c_type!="Chain"):
            for i in self.book_texts.hash_map:
               
                if(i[0]!=-1):
                    if(i[1].find(keyword)):
                        res.append(i[0])
        else:
            for i in self.book_texts.hash_map:
                for j in i:
                    if(j[1].find(keyword)):
                        res.append(j[0])
        return res

    
    def print_books(self):
        if(self.c_type!="Chain"):
            for i in self.book_texts.hash_map:
                if(i[0]!=-1):
                    print(i[0]+":",end=" ")
                    print(i[1])
        else:
            for i in self.book_texts.hash_map:
                for j in i:
                    print(j[0]+":",end=" ")
                    print(j[1])
                        
