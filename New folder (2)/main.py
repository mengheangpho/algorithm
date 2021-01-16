#
#word=str(input("The word:"))
#index=" "
#nbofa=0
#for n in range (len(word)):
#  index=word[n]
#  if index=="a"  or index=="A" :
#    nbofa+=1
#print(nbofa)
#
word=str(input("The word:"))
index=" "
nbofa=0
nbofb=0
for n in range (len(word)):
  index=word[n]
  if index=="a" or index== "A":
    nbofa+=1
  if index=="B" or index=="b":
    nbofb+=1
if nbofa==2 and nbofb==2:
  print("WELL DONE")
else:
  print("LOST")