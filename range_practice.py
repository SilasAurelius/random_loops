flavors = ['chocolate', 'vanilla', 'strawberry', 'mint chocolatechip']
toppings = ['cherry', 'sprinkles', 'chocolate syrup', 'whipped cream']

"""for i in range(4):
    print("Trying out flavor number " + str(i+1) + ": " + flavors[i])
"""
    
for flavor in flavors:
    for topping in toppings:
        print(f"I had " + flavor + " with some " + topping)
        
        
for flavor in flavors:
    if flavor == "mint chocolatechip":
        print("My favorite! No need for further tasting.")
        break
    print("Trying " + flavor + " flavor.")