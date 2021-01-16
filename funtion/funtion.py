# def getmax(n1,n2):
#   max=0
#   if n1>n2:
#     max=n1
#   else:
#     max=n2
#   return max
# def getmin(n1,n2):
#   min=0
#   if n1>n2:
#     min=n2
#   else:
#     min=n1
#   return min
# print("max: "+str(getmax(100,200)))
# print("min: "+str(getmin(100,200)))
#----------------------  How to find max and min in funtion?----------------------#
string=str(input()).upper()
condition=False
for n in range(len(string)):
  if string[n]=="A":
    condition=True
if condition:
  print("HAS A")
else:
  print("HAS NO A")