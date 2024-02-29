def count_Vowels(sentence):
    vowels = 'aeiouAEIOU'
    count =0
    for char in sentence:
          if char in vowels:
               count+=1
    return count
sentence = "Happy, Learning!"
print("Number of vowels in the sentence:", count_Vowels(sentence))