sentence="my name is manasi my company name is google"
count={}

words=sentence.lower().split()
for word in words:
    count[word]=count.get(word,0)+1
print(count)
