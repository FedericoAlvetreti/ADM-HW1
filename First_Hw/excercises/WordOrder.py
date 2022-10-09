from collections import Counter

n=int(input())
word_list=[]
for i in range(n):
    word_list+=[input()]
word_list=Counter(word_list)
print(len(word_list))
for i in word_list:
    print(word_list[i],end=" ")
