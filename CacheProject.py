#Cache Project
########################################
#                                      
# Name: Francesca Ansell 
# Collaboration Statement: Assignment created by Proffessor Conejo-Lopez
#
########################################

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
        #Puts content into CacheList
        #Uses lruEvict and mruEvict to evict list items until the new item can be inserted
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
        #Completes a Most Recently Used cache algorithm by removing the head
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
        #Completes a Least Recently Used cache algorithm by removing the tail
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
        #Clears the cache list and resets the size and number of items
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

    def __init__(self):
        self.hierarchy = [CacheList(200) for _ in range(3)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__

    def hashFunc(self, contentHeader):
        #Finds the hash index based on the contentheader
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
    
    def insert(self, content, evictionPolicy):
        #Inserts content into the cash list using put
        content_  = ContentNode(content)
        index = self.hashFunc(content.header) 
        i = self.hierarchy[index].put(content_, evictionPolicy)
        if i == True:
            return f'INSERTED: {content}'
        else:
            return f'Insertion not allowed. Content size is too large.'
        

    def retrieveContent(self, content):
        #Retrieves content by finding the its index using the hashFunction and cache lists find function
        find = self.hierarchy[self.hashFunc(content.header)].find(content.cid)
        return(find)
