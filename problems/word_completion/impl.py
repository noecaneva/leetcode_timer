from typing import List, Tuple

class node1:
    def __init__(self, letter: str|None = None, eow: bool = False):
        self.letter = letter
        self.next_list = []
        self.end_of_word = eow

class triatree1:
    def __init__(self):
        self.root = node1()
    
    def add_str(self, word : str):
        curr_node = self.root
        counter = 0
        for lett in word:
            counter += 1
            next_node_letters = [next_node.letter for next_node in curr_node.next_list]
            if lett not in next_node_letters:
                n = node1(lett)
                curr_node.next_list.append(n)
                curr_node = n
            else:
                curr_node = curr_node.next_list[next_node_letters.index(lett)]
        # to make sure the last entry has eow=True
        curr_node.end_of_word=True

    def find_subpaths(self, n: node1|None) -> List[List[str]]:
        curr_node = n
        return_lett_list = [[curr_node]]
        curr_node.next_list.sort(key = lambda n : n.letter)
        if curr_node.next_list:
            return_lett_list = []
            curr_node_prefix = [curr_node] if curr_node != self.root else []
            for next_n in curr_node.next_list:
                subpaths =  self.find_subpaths(next_n)
                for path in subpaths:
                    return_lett_list.append(curr_node_prefix + path)
        return return_lett_list

class Solution1:
    @staticmethod
    def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
        suggestion_tree = triatree1()
        suggestion_tree_root = suggestion_tree.root

        for product in products:
            suggestion_tree.add_str(product)

        return_suggested_words = []
        node_iter = suggestion_tree_root
        prefix = []
        suggested_words_list = []
        
        for counter, char_sw in enumerate(searchWord):
            next_list_letters = [n.letter for n in node_iter.next_list]
            try:
                new_root_node = node_iter.next_list[next_list_letters.index(char_sw)]
                suggested_words_list_temp = suggestion_tree.find_subpaths(new_root_node)
                words_per_prefix = []
                for path in suggested_words_list_temp:
                    letter_list = [n.letter for n in path]
                    eow_bool = [n.end_of_word for n in path]
                    for idx, bool_flag in enumerate(eow_bool):
                        if bool_flag:
                            suffix_char_list = letter_list[:(idx+1)]
                            if len(words_per_prefix) < 3:
                                words_per_prefix.append(''.join(prefix + suffix_char_list))
                            else:
                                break
                    
                    if len(words_per_prefix) >= 3:
                        break
                                     
                return_suggested_words.append(words_per_prefix)
                prefix.append(new_root_node.letter)
                node_iter = new_root_node
            except ValueError:
                for _ in range(counter, len(searchWord)):
                    return_suggested_words.append([])
                break

        return return_suggested_words

class node_str:
    def __init__(self, stringValue: str|None = None, endOfWord: bool = False):
        self.stringValue = stringValue
        self.endOfWord = endOfWord
        self.nextNodes = []

class suggestion_word_trie:
    def __init__(self):
        self.root = node_str()
    
    def addWord(self, wordToAdd: str):
        currNode = self.root
        for idx, charWord in enumerate(wordToAdd):
            currValue = wordToAdd[:(idx+1)]
            nextStringsList = [n.stringValue for n in currNode.nextNodes]
            if currValue not in nextStringsList:
                newNode = node_str(currValue)
                currNode.nextNodes.append(newNode)
                currNode = newNode
            else:
                currNode = currNode.nextNodes[nextStringsList.index(currValue)]
        
        # make sure that last node has eow=true
        currNode.endOfWord = True
    
    # Order is useless if the products are put in in lexicongrafic order
    def order(self, node: node_str):
        interNode = node
        iterNode.nextNodes.sort(key = lambda n: n.stringValue)
        for n in iterNode.nextNodes:
            self.order(n)

    def find_three_words(self, node: node_str) -> List[str]:
        wordList = []
        iterNode = node
        if node.endOfWord:
            wordList.append(node.stringValue)
        
        for n in iterNode.nextNodes:
            subWords = self.find_three_words(n)
            for subWord in subWords:
                wordList.append(subWord)
                if len(wordList) >= 3:
                    return wordList

        return wordList
    
    # Takes a from_node and a value and returns the node of the next.list 
    # with that value
    def return_node_from_node_with_val(self, from_node: node_str,  value: str) -> node_str:
        for to_node in from_node.nextNodes:
            if to_node.stringValue == value:
                return to_node
        return None

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = suggestion_word_trie()

        # Add all the words to the trie
        for product in products:
            trie.addWord(product)

        # Go through the trie, at each node (or tipped character)
        # suggest 3 possible completions
        # if no completion possible return []
        node_iter = trie.root
        suggested_word_per_char = [[] for _ in range(len(searchWord))]
        for idx, charWord in enumerate(searchWord):
            currValue = searchWord[:(idx+1)]
            node_iter = trie.return_node_from_node_with_val(node_iter, currValue)
            if node_iter is not None:
                suggested_word_per_char[idx] = trie.find_three_words(node_iter)
            else:
                return suggested_word_per_char
        
        return suggested_word_per_char

SOLUTIONS = {
    "solution from hell": lambda args: Solution1.suggestedProducts(*args),
    "optimized solution": lambda args: Solution().suggestedProducts(*args),
}