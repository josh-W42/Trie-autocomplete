## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if current_node:
                current_node = current_node.children.get(char)
            else:
                break
        
        return current_node

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if self.children.get(char) is None:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix= ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        output = []
        children = None

        if suffix == '':
            children = self.children
        else:
            if suffix.is_word:
                # if the suffix is a word, add it to the output
                output.append('')

            children = suffix.children
        
        for char in children.keys():
            suffixes = self.suffixes(children[char])

            if type(suffixes) == list:
                for word_ending in suffixes:
                    output.append(char + word_ending)
            else:
                output.append(char + suffixes)

        return output


# TESTS BELOW
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')