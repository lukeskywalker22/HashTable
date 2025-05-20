## Hash Table Practice

A Hash Table is implemented with a fixed-size array.

**Reminder:** A hash table **does NOT do a linear search** to locate the item! If you are looking to implement a linear search algorithm within the hash table, **think twice**!

With reference to the **algorithm** given in the [notes](https://docs.google.com/document/d/18-ROQl3yrCsoCzIDRKCvKqx82IprpE5UoxTVyPfw8bo/edit?tab=t.0#heading=h.n8aq0nk6ho4p), you are required to Implement a **Hash Table** class (in the **hashtable.py file**)  

with the attributes:  
- `size` - size of the hash table
- `values` - a Python list spanning the size of the hash table, pre-filled with the **None** placeholder

and the following methods:  
- `repr()` - returns a formatted string containing the values in the hash table
- `_hash(key)`
    - takes in a `string` argument `key`
    - returns a hashed `integer` value denoting the `location` (to be used by the other methods for insertion/update/retrieval/deletion) using a hash function. A sample hash function, using the rolling polynomial algorithm is shown below:  
      (Further reading: https://cp-algorithms.com/string/string-hashing.html)  
        
      $`hash(key) = (key[0] + key[1].p + key[2].p^2 + ... + key[n-1].p^{n-1})\ mod\ m = (\sum_{i=0}^{n-1} key[i].p^i)\ mod\ m`$  
      where
      - `key` - each key segment is a string. It needs to be converted to its integer ASCII value 
      - `p` - a small prime number (if the input is composed of only lowercase letters of the English alphabet,  
        $p = 31$  is a good choice. If the input may contain both uppercase and lowercase letters, then  
        $p = 53$  is a possible choice.)
      - `m` - a large prime number (we will use $`10^9+9`$ for this implementation)

    - You can use the following sample in `pseudocode`, of calculating the hash of a string 
    $s$ , which contains only lowercase letters. We convert each character of  
    $s$  to an integer. Here we use the conversion  
    $a \rightarrow 1$ ,  
    $b \rightarrow 2$ ,  
    $\dots$ ,  
    $z \rightarrow 26$ . Converting  
    $a \rightarrow 0$  is not a good idea, because then the hashes of the strings  
    $a$ ,  
    $aa$ ,  
    $aaa$ ,  
    $\dots$  all evaluate to  
    $0$ .
    ```code
    FUNCTION ComputeHash(key : STRING) RETURNS INTEGER
        DECLARE p : INTEGER
        DECLARE m : INTEGER
        DECLARE hashValue : INTEGER
        DECLARE pPow : INTEGER
        DECLARE i : INTEGER
        DECLARE charValue : INTEGER

        p ← 31
        m ← 1000000009
        hashValue ← 0
        pPow ← 1

        FOR i ← 1 TO LENGTH(key)
            charValue ← ASCII(key[i]) - ASCII('a') + 1
            hashValue ← (hashValue + charValue * pPow) MOD m
            pPow ← (pPow * p) MOD m
        NEXT i

        RETURN hashValue MOD SIZE_OF_HASHTABLE
    END FUNCTION
    ```
    `NOTE:` The largest location value to be returned should be less than the size of hash table, hence the need to mod the hashValue with the size of the hash table. 
    
- `setitem(key, item)`
    - adds/updates an item in the hash table
    - displays the following strings:
        - `Data successfully added!` if the destination is empty or
        - `Data successfully updated!` otherwise
- `getitem(key)` - returns the following:
    - returns an item within the hash table or
    - displays the string `Destination is empty!` and returns the value `None` otherwise
- `delitem(key)`
    - removes the item at the destination
    - displays the following strings:
        - `Unable to remove. Destination is empty!` if there is no item at the destination or
        - `Data successfully removed` otherwise

## Task 1.1
Implement the `_hash(key)` method such that:
- it accepts a string `key` as parameter
- uses the hashing algorithm mentioned above
- and returns a integer value denoting the location of an item in the hash table

## Task 1.2
Implement the rest of the methods for the Hash Table.

**NOTE: Remember to include the docstrings for your methods**
