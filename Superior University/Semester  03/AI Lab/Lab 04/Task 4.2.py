punctuation ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
user_input=input("Enter a string:")
no_punct = ""
for i in user_input:
    if i not in punctuation:
        no_punct += i
print("String without punctuations:",no_punct)