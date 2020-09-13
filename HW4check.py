#HW4
#Due Date: 12/01/2019, 11:59PM 
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################
""" 
ord(c) = 89

put (insert) 

MRU (add remove from head)
remove content in order to add new content if cache = 200

LRU remove least used item (tail)
move through whole list 

evication policy is either MRU or LRU


"""


class ContentItem():
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return ('CONTENT ID: {} SIZE: {} HEADER: {} CONTENT: {}'.format(self.cid, self.size, self.header, self.content))

    __repr__=__str__


class ContentNode():
    def __init__(self, content, nextNode = None):
        self.value = content
        self.next = nextNode

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__

class CacheList():
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.maxSize = size
        self.remainingSize = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return ('REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}\n'.format(self.remainingSize, self.numItems, listString))     

    __repr__=__str__
    
    def put(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        #insert function
        #need edge cases (1) dont insert somthing greater than the size of the cache list 
        #(2) if the number of items is 0 and cahce is less than size you can insert
        #(3) other case where you dont have to evict anything is when the remain space is enough then you can add it (add it to the head or the tail)
        #cases for LRU and MRU where you keep calling the evict function until you can insert (while loops calling MRU or LRU)
        if self.maxSize < content.value.size:
            return False
        else:
            if self.remainingSize > content.value.size:
                if self.head == None:
                    self.head = content
                    self.tail = content
                    self.remainingSize = self.remainingSize - content.value.size
                    self.numItems = self.numItems + 1 
                    return True
                else:
                    current = self.tail
                    current.next = content 
                    self.tail = content 
                    self.remainingSize = self.remainingSize - content.value.size
                    self.numItems = self.numItems + 1
                    return True
            else:
                if evictionPolicy == 'mru':
                    while self.remainingSize < content.value.size: 
                        
                        self.mruEvict()
                elif evictionPolicy == 'lru':
                    while self.remainingSize < content.value.size:
                        
                        self.lruEvict()
            return True
       







    def find(self, cid):
        temp = self.head
        if temp.value.cid == cid:
            return temp.value 
        while temp.next != None:
            if temp.value.cid == cid:
                return temp.value
            else:
                temp = temp.next

        return 'Cache miss!'
        

    def mruEvict(self):
        #dont return anything dont insert anything /////////// removes head
        #Start 2
        temp = self.head
        if temp.next == None:
            self.remainingSize = self.remainingSize + temp.value.size
            temp = None
            return

        temp.next = self.head
        self.remainingSize = self.remainingSize + temp.value.size
        temp = None


        return

    
    def lruEvict(self):
        #dont return anything dont insert anything ////// removes tail
        #Start 2
        temp= self.head
        if temp.next == None:
            self.remainingSize = self.remainingSize + temp.value.size
            temp = None
            self.tail = None
            
            return 

        elif temp.next.next == None:
            temp.next = None
            self.tail = temp
            return

        else:


            temp = self.head
        
            #starts at second element interates till 2nd to last element
            while temp.next.next != None:
                temp = temp.next

            self.remainingSize = self.remainingSize + self.temp.value.size


            temp.next = None
            self.tail = temp

        
        return
    
    def clear(self):
        current = self.head
        while current.next != None:
            current.next = None

        current = None
        self.head = None
        self.tail = None
        self.remainingSize = self.maxSize
        self.numItems = 0 
        return 'Cleared cache!'


        

class Cache():
    """
        >>> cache = Cache()
        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1003, 13, "Content-Type: 0", "0xD")
        >>> content3 = ContentItem(1008, 242, "Content-Type: 0", "0xF2")
        >>> content4 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content5 = ContentItem(1001, 51, "Content-Type: 1", "110011")
        >>> content6 = ContentItem(1007, 155, "Content-Type: 1", "10011011")
        >>> content7 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content8 = ContentItem(1002, 14, "Content-Type: 2", "<html><h2>'PSU'</h2></html>")
        >>> content9 = ContentItem(1006, 170, "Content-Type: 2", "<html><button>'Click Me'</button></html>")
        >>> cache.insert(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> cache.insert(content2, 'mru')
        'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
        >>> cache.retrieveContent(content1)
        CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA
        >>> cache.retrieveContent(content2)
        CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD
        >>> cache.retrieveContent(content3)
        'Cache miss!'
        >>> cache.insert(content5, 'mru')
        'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
        >>> cache.insert(content6, 'mru')
        'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'
        >>> cache.insert(content4, 'mru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> cache.insert(content7, 'mru')
        "INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
        >>> cache.insert(content8, 'mru')
        "INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>"
        >>> cache.insert(content9, 'mru')
        "INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>"
        >>> cache
        L1 CACHE:
        REMAINING SPACE:177
        ITEMS:2
        LIST:
        [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        <BLANKLINE>
        L2 CACHE:
        REMAINING SPACE:150
        ITEMS:1
        LIST:
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        <BLANKLINE>
        <BLANKLINE>
        L3 CACHE:
        REMAINING SPACE:12
        ITEMS:2
        LIST:
        [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
        [CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>]
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
    """
    def __init__(self):
        self.hierarchy = [CacheList(200) for _ in range(3)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__

    def hashFunc(self, contentHeader):
        #Start 1
        #take your content header and turn it into an index
        ascii_ = ord(contentHeader[len(contentHeader)-1])

        index = ascii_ % 200
        
        
        if index == 48:
            return 0
        elif index == 49:
            return 1
        elif index == 50:
            return 2
        else:
            return 'not sure'



        # YOUR CODE STARTS HERE
    
    def insert(self, content, evictionPolicy):
        #Start 1
        #make it a node
        #take in a content object 
        #send the content objects header to the hash function
        #index our hierachy and call that cachelist's PUT function
        #the work of insetion is in PUT

        content_  = ContentNode(content)

        index = self.hashFunc(content.header) 
        i = self.hierarchy[index].put(content_, evictionPolicy)
        if i == True:
            return f'INSERTED: {content}'
        else:
            return f'Insertion not allowed. Content size is too large.'
        

    def retrieveContent(self, content):
        #find the index (use hashFunc) use that cach lists find function
        find = self.hierarchy[self.hashFunc(content.header)].find(content.cid)
        
        return(find)
