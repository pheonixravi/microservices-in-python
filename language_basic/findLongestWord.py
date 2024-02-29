def findLongestWord(words):
    longest=''
    for word in words:
        if len(word) > len(longest):
            longest=word
    return longest

word_list = ["apple", "banana", "kiwi", "strawberry"]
print("Longest word in the list:", findLongestWord(word_list))