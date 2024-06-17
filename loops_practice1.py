# Learning basics of loops beginning with for loops.

flavors = ["chocolate", "vanilla", "strawberry", "pistachio"]
toppings = ["sprinkles", "chocolate syrup", "whipped cream", "cherry"]

""""
for flavor in flavors:
    print("Mmm....I just sampled " + flavor + "!")
 """   

for i in range(4):
    print("Trying out flavor number " + str(i +1) + ": " + flavors[i])


#ice_cream_flavors = ["chocolate", "vanilla", "strawberry", "mint chocolate chip", "pistachio"]   

"""
for flavor in ice_cream_flavors:
    if flavor == "mint chocolate chip":
        print("My favorite! No need to taste further.")
        break
    print("Trying " + flavor + "flavor")
"""    
"""
for flavor in ice_cream_flavors:
    if flavor == "pistachio":
        continue
    print("Enjoying a scoop of " + flavor + "!")
    
for flavor in ice_cream_flavors:
    if flavor == "rocky road":
        pass
    print("Sampling " + flavor + " now.")
"""