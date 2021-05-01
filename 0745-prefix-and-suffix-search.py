from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        # Key is the starting letter and ending letter
        # Value is the word and the corresponding index
        self.data = {}

        for i in range(len(words)):
            word = words[i]
            key = (word[0], word[-1])
            value = (word, i)

            if key in self.data:
                self.data[key].append(value)
            else:
                self.data[key] = [value]

        # print(self.data)
        
    def f(self, prefix: str, suffix: str) -> int:
        # Get the first and last letter
        first_letter = prefix[0]
        last_letter = suffix[-1]

        # Get the possible words
        possible_words = self.data.get((first_letter, last_letter))

        # Check from the last item in the list
        if possible_words != None:
            for i in range(len(possible_words) - 1, -1, -1):
                word = possible_words[i][0]
                index = possible_words[i][1]
                
                if word.startswith(prefix) and word.endswith(suffix):
                    return index

        return -1

def get_result(words, prefix, suffix):
    return WordFilter(words).f(prefix, suffix)

def test_empty_words():
    assert get_result([], "a", "b") == -1

def test_case_1():
    assert get_result(["apple"], "a", "e") == 0

def test_case_2():
    assert get_result(["apple", "banana"], "b", "a") == 1

def test_multiple_matches():
    assert get_result(["apple", "apple", "able"], "a", "e") == 2

def test_not_found():
    assert get_result(["apple", "banana"], "a", "d") == -1