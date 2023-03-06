import json

# Open the JSON file and load its contents
with open('../topics.json') as f:
    data = json.load(f)

# Initialize a count variable to keep track of the number of items
count = 0

# Loop through the items in the JSON data
for item in data:
    # Do something with each item, e.g. print it
    # Increment the count variable
    count += 1

# Print the total number of items
print(f'Total number of items: {count}')
