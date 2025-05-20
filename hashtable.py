class HashTable:
    def __init__(self, size):
        """
        Initialises the HashTable class with the properties self.size and self.values, with self.values being calculated
        by initialising a list of None objects with length self.size
        """
        self.size = size
        self.values = []
        for i in range(size):
            self.values.append(None)

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """
        Return a hashed location using the rolling polynomial algorithm.
        Further reading: https://cp-algorithms.com/string/string-hashing.html

        Note: 
        - The largest value to be returned will be less than size.   
        Remember to compress the return value to fit the table size.
       
        Parameters
        ---------
        - key: str
          The key to be hashed
        """

        p = 31
        m = 1000000009
        hashValue = 0
        pPow = 1

        for char in key:
            charValue = ord(char) - ord('a') + 1
            hashValue = (hashValue + charValue + pPow) % m
            pPow = (p * pPow) % m
        
        return hashValue % self.size

    def setitem(self, key: str, value: dict) -> None:
        """
        Hashes the key of the data and sets the corresponding index in the self.values list to value
        If corresponding index is empty prints "Data successfully added!" and prints "Data successfully
        updated!" if index was not previously empty.
        """
        if self.values[self._hash(key)] is None:
            print("Data successfully added!")
        else:
            print("Data successfully updated!")
        self.values[self._hash(key)] = value

    def getitem(self, key: str) -> 'dict | None':
        """
        Hashes given key and returns the value stored at list position of hash, if value is empty prints
        "Destination is empty!" and returns None
        """
        if self.values[self._hash(key)] is None:
            print("Destination is empty!")
            return None
        return self.values[self._hash(key)]
        
    def delitem(self, key: str) -> None:
        """
        Hashes given key and sets value of list at hash index position to None, if destination is already None
        prints "Unable to remove, destination is empty!"
        """
        if self.values[self._hash(key)] is None:
            print("Unable to remove, destination is empty!")
        else:
            self.values[self._hash(key)] = None
