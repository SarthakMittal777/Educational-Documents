inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory["pocket"]=['seashell', 'strange berry', 'lint']
print(inventory)
for i,j in inventory.items():
j.sort()
j,discard


#Add a key to inventory called 'pocket'.
#Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
#.sort()the items in the list stored under the 'backpack' key.
#Then .remove('dagger') from the list of items stored under the 'backpack' key.
#Add 50 to the number stored under the 'gold' key.