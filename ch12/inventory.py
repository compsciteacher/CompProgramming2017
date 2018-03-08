
def starter_inventory():
    inventory={'apples':15,'cherries':20,'pears':30,'oranges':20}
    inventory['apples']+=10
    print(inventory['apples'])
    inventorychanges(inventory)
def inventorychanges(inventory):
    while True: #start a loop that will continue until the person enters valid dictionary key
        choice=input('Item: ')
        if choice in inventory.keys():
            break #once choice is a dictionary key, break loop
    numberlost=int(input('Number sold: '))
    inventory[choice]-=numberlost #change value based on entry
    print("You now have %i %s"%(inventory[choice],choice))

starter_inventory()