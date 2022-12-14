watchlist = ["blacklist", "avatar", "the grinch"]
watchlist.append("dexter")
watchlist.append("teletubbies")
watchlist.remove("teletubbies")

nr_of_options = len(watchlist)

print(watchlist, "contains", nr_of_options, "options.")
watchlist.sort()
print(watchlist)
watchlist.reverse()
print(watchlist)
watchlist.clear()
print(watchlist)

# extend en plus voorbeeld
l1 = [1]
l2 = [2]

l3 = l1 + l2

watchlist.extend(l1)
watchlist.extend(l2)
