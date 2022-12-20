import os 

# indexError
languages = ["python", "rust", "js"]
index = 3
if index >= len(languages):
  print("nope")
else:
  print(languages[3])

# typeError
languages = ["python", "rust", "js"]
index = 2

if type(index) is int:
  print(languages[index])
else:
  print("cant do this")

#IOError

try:
  file = open("blabla.txt", "r")
  file.read()
except FileNotFoundError:
  print("whoops, the file is not found:")
except IOError:
  print("Some io problems")

print(issubclass(FileNotFoundError, IOError))

if os.path.exists("blabla.txt"):
  with open("blabla.txt") as file:
    file.read()
else:
  print("I would love to read it, but I don't have the file")


raise IOError