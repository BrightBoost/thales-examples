# break
i = 0
while True:
    i += 1
    if i == 10:
        break
    print(i)
print("done")

# wat ik mooier vind (zonder break)
i = 0
not_found = True
while not_found:
    i += 1
    if i == 10:
        not_found = False
    else:
        print(i)
print("done")

# continue
i = 0
while i < 1000:
  i += 1
  if i % 2 == 0:
    continue
  print(i)

# zonder continue
i = 0
while i < 1000:
  i += 1
  if i % 2 != 0:
    print(i)

# noodzakelijke toepassing
lijstje = range(0, 10000, 100)
for i in lijstje:
  if i == 3400:
    break
  print(i)

