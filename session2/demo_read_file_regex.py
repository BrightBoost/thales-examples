import re

with open("lyrics.txt") as file:
  for line in file:
    result = re.search("we", line)
    print(result)