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

SOLUTIONS = {
    "solution from hell": lambda args: Solution1.suggestedProducts(*args),
}