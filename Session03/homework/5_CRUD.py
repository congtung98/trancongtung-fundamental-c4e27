items = ['T-Shirt','Sweater']
while True:
    choice = input('Welcome to our shop, what do you want (C, R, U, D)? ')
    if choice == 'R':
        print('Our items:',items)
    elif choice == 'C':
        new_item = input('Enter new item: ')
        items.append(new_item)
        print('Our items:',items)
    elif choice == 'U':
        up_pos = int(input('Update position? '))
        update_item = input('New item? ')
        if up_pos <= len(items):
            items[up_pos-1] = update_item
        else: 
            print('Your position not exist!')
        print('Our items:',items)
    elif choice == 'D':
        del_pos = int(input('Delete position? '))
        if del_pos <= len(items):            
            items.remove(items[del_pos-1])
        else:
            print('Your position not exist!')
        print('Our items:',items)
    elif choice == 'Q':
        print('Thank you for shopping!')
        break
    else:
        print('Please enter right characters (only upper case allowed) or press Q to quit ')
