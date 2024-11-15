u_list = []
item_hist = open("item_history.txt", "a+")
item_histo = []

def printMenu():
    title = 'Checklist Main Menu'
    print(title.center(50, '-'))
    print('1) Add Item\n2) Edit Item\n3) Cross out Item\n4) Delete Item\n5) Item History\n6) Print Checklist\n7) Exit')

def cross_item():
    c_item = int(input("Cross Out Item Number: ")) - 1    
    first_let = u_list[c_item][0]
    last_let = u_list[c_item][-1]
    dash = "-"
    for letter in range(len(u_list[c_item]) - 2):
        dash += "-"
    crossed = first_let + dash + last_let
    u_list.insert(c_item + 1, crossed)
    u_list.pop(c_item)
    return

def delete_item():
    del_item = int(input("Delete Item Number: ")) - 1
    item_hist.write(f'{del_item + 1}) {u_list[del_item]}\n')
    item_histo.append(f'{del_item + 1}) {u_list[del_item]}')
    u_list.pop(del_item)
    return

def item_history():
    title = "Deleted Item History"
    print(title.center(20, "-"))
    for item in item_histo:
        print(item)
    return

def main():
    value = 0
    while value != 7:
        printMenu()
        value = int(input('Enter an option: '))
        if value == 1:
            item = input('Enter Item: ')
            u_list.append(item)
        elif value == 2:
            index = int(input('Enter item number you want to edit: '))
            item = input('Enter new item: ')
            u_list[index - 1] = item
        elif value == 3:
            cross_item()
        elif value == 4:
            delete_item()
        elif value == 5:
            item_history()
        elif value == 6:
            print()
            print('CHECKLIST'.center(50, '♥'))
            for i, x in enumerate(u_list):
                print(f'{i + 1}) {x}')
            print()
    
    item_hist.close()

main()

