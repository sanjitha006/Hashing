# Hashing
This project implements a custom hash table in Python, showcasing various techniques for collision handling, including chaining and open addressing. It provides efficient data insertion, deletion, and retrieval operations.

details:
This project aims to develop a system to handle the digitization of books in a library. The system enables efficient management and searching of distinct words in books. It consists of several methods for handling word storage and retrieval, including sorting and hashing techniques, depending on the strategy chosen by the developers. The goal is to implement a solution that can provide distinct words in each book, count those words, and efficiently search books based on keywords.

Key Features:
Mergesort (Musk’s Method): The system sorts words lexicographically and extracts unique words from the sorted list.
Hashing Methods (Jobs, Gates, Bezos): Various collision handling techniques are implemented, including:
Chaining (Jobs): Uses linked lists to handle collisions.
Linear Probing (Gates): Resolves collisions by linearly probing for the next available slot.
Double Hashing (Bezos): Uses a second hash function for step-size probing to resolve collisions.
Dynamic Resizing: The hash table dynamically resizes when the load factor exceeds a given threshold, improving memory efficiency.
Search and Count Operations: The library can search for a keyword and return relevant books, count distinct words, and print books along with their distinct words.
Data Structures:
HashSet and HashMap: Custom implementations of hash tables are used to store and retrieve the words in the books. The HashSet stores just the words, while the HashMap stores words as key-value pairs (word: count).
Dynamic Hashing: The project includes dynamic resizing of hash tables to optimize space utilization and performance.
Hash Function:
Polynomial Accumulation Hash: A hash function is used for efficient indexing of words into the hash table.
Dynamic Hash Function (Double Hashing): For resolving collisions, a second hash function is applied, offering more robust collision handling.
Operations:
Insert: Adds a new word or key-value pair to the hash table.
Find: Retrieves whether a word exists in the hash table or returns the value associated with it.
Get Slot: Determines the hash table index for a given word.
Distinct Words: Returns a list of distinct words for a given book, sorted lexicographically for Musk's method or by their hash order for Jobs/Gates/Bezos.
Search Keyword: Searches for books containing a specific keyword.
Performance:
Time Complexity:
MuskLibrary: 
𝑂
(
𝑘
𝑊
log
⁡
𝑊
+
𝑘
log
⁡
𝑘
)
O(kWlogW+klogk) for initialization, where k is the number of books and W is the number of words per book.
JGBLibrary: 
𝑂
(
𝑊
+
table size
)
O(W+table size) for adding a book, with 
𝑂
(
1
)
O(1) for finding distinct words and counting them.
