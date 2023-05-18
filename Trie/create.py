class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

print(trie.search("apple"))  
print(trie.search("banana"))  
print(trie.search("orange"))  
print(trie.search("grape"))  

print(trie.starts_with("app")) 
print(trie.starts_with("ban"))
print(trie.starts_with("or")) 
print(trie.starts_with("gr"))
