menu = {'Americano': 3000, 'Ice Americano': 3500, 'Chapucino':4500}
for key in menu:
    print("{:20s}Price: {:,}".format(key,(menu[key])))

choice = input("Enter the the drink:    ")

if choice in menu.keys():
    print("{} is {}. Please make a Payment".format(choice,menu[choice]))
else:
    print("Sorry. {} is not in the menu".format(choice))