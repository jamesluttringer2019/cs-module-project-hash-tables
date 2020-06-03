class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value, nxt=None):
        self.key = key
        self.value = value
        self.next = nxt
        self.prev = None

class LinkedList:
    def __init__(self, head):
        self.head = head

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.table = [None]*capacity
        self.items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        h = 5381
        for c in key:
            h = (h*33) + ord(c)
        return h


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        ind = self.hash_index(key)
        if self.table[ind]==None:
            self.table[ind] = LinkedList(HashTableEntry(key, value))
            self.items += 1
        else:
            if self.get(key):
                cur = self.table[ind].head
                while cur:
                    if cur.key == key:
                        cur.value = value
                    cur = cur.next
            else:
                self.table[ind].head.prev = HashTableEntry(key,value, self.table[ind].head)
                self.table[ind].head = self.table[ind].head.prev
                self.items += 1
        if self.get_load_factor() > .7:
            self.resize(self.capacity*2)
                    
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        ind = self.hash_index(key)
        if self.table[ind]:
            cur = self.table[ind].head
            while cur:
                if cur.key == key:
                    if cur.next and cur.prev:
                        cur.next.prev = cur.prev
                        cur.prev.next = cur.next
                    elif cur.next:
                        self.table[ind].head = cur.next
                    else:
                        self.table[ind] = None
                    self.items -= 1
                elif cur.next==None:
                    print('Key not found')
                cur = cur.next
                
        else:
            print('Key not found')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        ind = self.hash_index(key)
        if self.table[ind]:
            cur = self.table[ind].head
            while cur:
                if cur.key == key:
                    return cur.value
                cur = cur.next
                if not cur:
                    return None
        else:
            return None 


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        old = self.table
        self.table = [None] * new_capacity
        for i in old:
            if i:
                cur = i.head
                while cur:
                    self.put(cur.key, cur.value)
                    cur = cur.next
            else:
                pass
            
        


###### increment count when insert/delete items to track load (num items stored/num slots)

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
