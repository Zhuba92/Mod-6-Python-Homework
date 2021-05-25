# Part One

items = []
response = ""

while response != "NA":
  response = input("Enter an item (NA to end): ")
  if response == "NA":
    break;
  items.append(response)

items.reverse()

print(items)


# Part Two

participants = ["Bob", "Sue", "Craig", "Eric", "Lisa", "Jennifer"]

name = input("Please enter a name: ")

if name in participants:
  print(f"{name} is a participant")
else:
  print(f"{name} is not a participant")
