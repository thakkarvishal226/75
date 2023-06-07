class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        currNode = self.root

        for c in word:
            index =  ord(c)-ord('a')
            if not currNode.children[index]:
                currNode.children[index] = TrieNode()
            currNode = currNode.children[index]
        currNode.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        currNode = self.root
        for c in word:
            index = ord(c)-ord('a')
            if not currNode.children[index]:
                return False
            currNode = currNode.children[index]
        return True if currNode.isEndOfWord else False

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for c in prefix:
            index = ord(c)-ord('a')
            if not currNode.children[index]:
                return False
            currNode = currNode.children[index]
        return True
        


if __name__ == "__main__":
# Your Trie object will be instantiated and called as such:
    word = 'a'
    prefix = 'a'
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search('a')
    param_3 = obj.startsWith(prefix)
    print(param_2)
    print(param_3)