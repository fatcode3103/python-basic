# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict["year"])
# print(thisdict.keys())
# print(thisdict.values())


# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# thisdict.update({"year": 2020})
# thisdict.pop("model")
# print(thisdict.values())

### loop

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

for x in thisdict:
  print(thisdict[x])
