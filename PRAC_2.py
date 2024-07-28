sentence = str(input("Enter a sentence: "))
arr=[]
word_lengh=0
for i in sentence:
    word_lengh = word_lengh+1
    if i == " ":
        arr.append(word_lengh-1)
        word_lengh=0
    sentence.replace(i,"")
arr.append(word_lengh)
length = max(arr)
print(length,"longest word length")