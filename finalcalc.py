


grade = float(raw_input("What is your current grade?: "))
target = float(raw_input("What do you hope to get in the class?: "))
worth = (float(raw_input("What percentage is the final worth?: "))/100)
print "You need a " + str((target - grade * (1 - worth))/worth)