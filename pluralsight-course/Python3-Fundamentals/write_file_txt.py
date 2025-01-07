def find_astronaut(file_name):
    look_up = input("Which astronaut do you want to find?\n")

    found = False
    count = 0
    
    try:
        with open(file_name) as file:
            result = file.readlines()
            for line in result:
                if look_up in line:
                    count += 1
                    print(count,".", line)
                    found = True
                    
            print("Number The astronaut found: ", count)
    except:
        print('File not found')
        
    if not found:
        print("The astronaut does not exist")
        
def add_astronaut(file_name):
    text = input('Please input some text you want to add to file:\n')
    with open(file_name, 'a') as file:
        file.write('\n' + text)
    print('.... Added done!')
        
def main():
    file_name = 'astronaut.txt'
    choice = input('Do you want to find(F) or Add(A) a astronaut?')
    if choice == 'F':
        find_astronaut(file_name)
    elif choice == 'A':
        add_astronaut(file_name)
    else:
        print('You have chosen incorrectly, you must choose find(F) or Add(A)')

main()