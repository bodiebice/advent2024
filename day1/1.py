def find_distance_between_lists(l1,l2):
  distance = 0
  for x in range(len(l1)):
    temp = l1[x] - l2[x]
    if temp < 0:
      temp = temp * -1
    distance += temp
  return distance

def find_similarity_between_lists(l1,l2):
  similarity = 0
  dict = {}
  for x in l1:
    # we care about looking for the number of times a number in l1 appears in l2, we're gonna memoize to help 
    # reduce the time complexity. This should run somewhere b
    if x not in dict:
      count = 0
      for y in l2:
        if y == x:
          count += 1
        if y > x:
          # the lists are sorted, so if y is greater than x, we can stop looking for x in l2.
          break
      dict[x] = count
      similarity = similarity + (dict[x] * x )
    else:
      similarity = similarity + (dict[x] * x)
  return similarity

def process_inputs(file):
  with open(file, 'r') as inputfile:
    # Read each line in the file
    l1 = []
    l2 = []
    for line in inputfile:
        # we have to strip the numbers, due to the uneven spacing in the txt file. I could've had an llm fix the spacing of the txt file
        # but was too lazy to.
        words = line.strip()
        number1 = words[0:5]
        number2 = words[8:13]
        
        l1.append(int(number1))
        l2.append(int(number2))
    return (l1, l2)
if __name__ == "__main__":
  l1, l2 = process_inputs("1.txt")
  # below are the test strings 
  #l1 = [3,4,2,1,3,3]
  #l2 = [4,3,5,3,9,3]
  l1.sort()
  l2.sort()
  print(find_distance_between_lists(l1,l2))
  print(find_similarity_between_lists(l1,l2))