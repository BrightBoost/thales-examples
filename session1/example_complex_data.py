# Maak een lijst van bedrijven
# Een bedrijf is een dictionary met de volgende key-value pairs:
# - naam
# - telefoonnummer
# - dictionary van adressen, key is het type adres, bezoekadres, postadres, etc, en adres is een dictionary
# - adres is een dictionary, met key value pairs
# - lijst met activiteiten, bijv code schrijven, consultancy, etc

companies = [{
    "name": "company1",
    "phone": "0123456789",
    "addresses": {"postal address": {
        "streetname": "main road",
        "nr": "4"
    }, "visiting address": {
        "streetname": "main road",
        "nr": "4a"
    }},
    "activities": ["consultancy", "software development"]
  },
  {
    "name": "company2",
    "phone": "0123456783",
    "addresses": {"postal address": {
        "streetname": "rainbow road",
        "nr": "42"
    }, "visiting address": {
        "streetname": "blabla road",
        "nr": "24a"
    }},
    "activities": ["training", "software testing"]
}]

print(companies[1]["addresses"]["visiting address"]["streetname"])
print(companies[0]["activities"][0])
for kv in companies[0]["addresses"].items():
  if str(kv).find("visit") != -1:
    print(kv)