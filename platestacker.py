''''
Python Project: Plate Stacker
Written by: Jonathan Goon
1/12/2024

This is a simple plate stacker that showcases the usage of Stack. Originally the stack was written backwards. Those components were commented out. 

Notes: I try to minimize the usage of comments in function definitions in order to keep the code clear and consise.
The program originally arrange the plates from smallest to largest by appending and removing from the beginning of the list.
That is revised in this sample.
'''
plate_stack = []

def read_required_string(str):
    recieved_string = False
    while not recieved_string:
        value = input(str)
        if value.strip():
            recieved_string = True
            return value

def menu():
    #Prints a menu.
    print('''
    Menu
    ====
    0. [Exit]
    1. Add a plate
    2. Print plates
    3. Remove plates
          ''')
    
    while True:
        selector = read_required_string('Select [0-3]:')
        
        try:
            selector =int(selector)
            if selector in range(0,4):
                break
            else:
                print('Invalid selection, please enter a valid selection between 0-3')
        except ValueError:
            print ('Invalid selection, enter a valid number.')
    
    match selector:
        case 0:
            #Exit
            print('Goodbye!')
            return False
        case 1:
            #Add a plate
            print ('Case 1: Add a plate')
            add_plate()
        case 2:
            #Print plates
            print ('Case 2: Print plates')
            print_plates()
        case 3:
            #Remove plates
            print ('Case 3: Remove plates')
            remove_plates()
    return True #Returns True to continue loop
            
def add_plate():
    #Adds a plate to the stack.
    plate_size = read_required_string('How big is the plate in inches?[1-16]: ')
    try:
        plate_size =int(plate_size)
        if plate_size in range(1,17):
            if not plate_stack or plate_stack[-1] >= plate_size:
                #stack originally sorted from lowest to highest on index, revised per project requirements.
                #plate_stack.insert(0, plate_size)
                plate_stack.append(plate_size)
                print(f'Added a {plate_size} inch plate to the stack.')
            else:
                print('Invalid entry, the plate is too big.')
        else:
            print('Invalid entry, the plate sizes can be between [1-16].')
    except ValueError:
        print ('Invalid selection, enter a valid number.')
    

def print_plates():
    #Prints our stack of plates.
    if not plate_stack or len(plate_stack) == 0:
        print( "No plates are currently in the stack.")
    else:
        print( "Here are your current stack of plates...")
        print('-'*20)
        #print originally sorted from lowest to highest on index, revised per project requirements.
        #for plate_size in plate_stack:
        for plate_size in reversed(plate_stack):
            plate_holder = '#' * plate_size
            print(f'{plate_holder:^16}')
        print('-'*20)
    
def remove_plates():
    #Removes a number of plates from the top of the stack.
    if not plate_stack:
        print('There are no plates to remove.')
        return
    
    num_of_plates = read_required_string('How many plates do you want to remove?: ')
    try:
        num_of_plates = int(num_of_plates)
        
        if num_of_plates > 0:
            if num_of_plates > len(plate_stack):
                print(f'Cannot remove more than {num_of_plates} of plates.\n Current stack size: {len(plate_stack)}')
            else:
                for _ in range(num_of_plates):
                    #originaly stacked backwards, revised based on project requirements.
                    #plate_stack.pop(0)
                    plate_stack.pop()
                    
                print(f'Removed {num_of_plates} from the stack.')
        else:
            print('Invalid entry, the number of plates to remove must be greater than 0.')
    except ValueError:
        print('Invalid selection, please enter a valid number.')


if __name__ == "__main__":
    #While loop used to display menu until user exits the program.
    while menu():
        pass
        