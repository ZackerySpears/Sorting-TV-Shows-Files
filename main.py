# Open files and reads it in line
with open('file1.txt','r') as f:
    data = f.readlines()

#Creates a empty dictionary to store the file
dict_info = {}

# Loops over the file
for i in range(0, len(data) - 1, 2):
    # Get the season as the value in the dictionary
    season = int(data[i].strip())
    name = data[i + 1].strip()
    if season in dict_info:
        dict_info[season].append(name)
    else:
        dict_info[season] = [name]

# Takes the keys and puts the information in a list
keys = list(dict_info.keys())

# Sorts them in Order
keys.sort()

# Write a new file for the keys
with open("output_keys.txt", "w") as f:
    # Loop overs tthe keys and formats the how it written
    for key in keys:
        names = "; ".join(dict_info[key])
        f.write(str(key) + ": " + names + "\n")

# Empty list for the names
names = []

# Loop over and adds the name in our dictionary and adds them to our names list
for item in dict_info:
    for name in dict_info[item]:
        names.append(name)

# Sorts them in Order
names.sort()

# Write a new file for the Names
with open("output_titles.txt", "w") as f:
    # Loops over each and formats it
    for name in names:
        f.write(name + "\n")