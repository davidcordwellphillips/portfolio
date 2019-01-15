list = [9, 10, 12, 14, 15, 16, 18]
length = len(list)
high = length
low = 0
found = False
search = int(input())
      
while low <= high and found == False:
  middle = ((low + high) // 2 )
  if list[middle] == search:
    found = True
    
  elif list[middle] < search:
    low = middle + 1
    found = False

  else:
    high = middle - 1
    found = False

print(found)
