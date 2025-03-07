def sort_word(list):
    words=list.split()
    n = len(words)
    for i in range(n):
        for j in range(0,n - i - 1):
            if words[j] > words[j+1]:
                words[j],words[ j+1 ]=words[j+1],words[j]
    sort_word=" ".join(words)
    return sort_word
user_input=input("Enter a sentence: ")
sorted_result=sort_word(user_input)
print("Sorted words in alphabetical order:",sorted_result)
