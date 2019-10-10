f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

# Keyword - 

# Dictionary - words are nodes
# shortest - BFS
# Transformation sequence - Path

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def get_neighbors(word):
    neighbors = []
    string_word = list(word) # turns each word into an array of characters
    
    for i in range(len(string_word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            # loop through string_word and change each letter to letter and check if
            # it's a word in the provided file
            temp_word = list(string_word) # we need to make a copy b/c this is the one we will mutate
            temp_word[i] = letter
            w = ''.join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors

# Run our search
def find_word_ladder(beginWord, endWord):
    visited = set()
    q = Queue()
    q.enqueue([beginWord])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)            
            if v == endWord:
                return path            
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

print(find_word_ladder('boat', 'hail'))



# Make our graph
# Run BFS
# Parse the result in a way that matches the problem and return it.

# Given two words (beginWord and endWord), and a dictionary's word list, 
# return the shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.