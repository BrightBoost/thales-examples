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
