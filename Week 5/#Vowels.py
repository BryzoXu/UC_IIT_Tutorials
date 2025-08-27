#Vowels

phrase = "Less is more."

vowels = "aeiouAEIOU"

counter = 0
for i in range(len(phrase)):
    if phrase[i] in vowels:
        counter +=1
        
        
print(counter)
