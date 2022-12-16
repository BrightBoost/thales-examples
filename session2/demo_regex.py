import re

text = "blabla hoi iets"
print(re.search("hoi", text))
print(re.search("^bla", text))


text = "I'm kidding. Hahahaha."
result2 = re.findall("(ha)+", text)

print(result2)
