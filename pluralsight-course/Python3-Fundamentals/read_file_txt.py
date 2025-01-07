look_up = input("Which astronaut do you want to find?\n")

found = False
count = 0
with open('acronyms.txt') as file:
    result = file.readlines()
    for line in result:
        if look_up in line:
            count += 1
            print(count,".", line)
            found = True
            
    print("Number The astronaut found: ", count)
if not found:
    print("The astronaut does not exist")
    
