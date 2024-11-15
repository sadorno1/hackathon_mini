def printMenu():
    title = 'Checklist Main Menu'
    print(title.center(50,'-'))
    print('1) Add Item\n2) Edit Item\n3) Cross out Item\n4) Delete Item\n5) Item History\n6) Print Checklist\n7) Exit')

def main():
    value = 0
    list = []
    while value != 7:
        printMenu()
        value = int(input('Enter an option:'))
        if value  ==1:
            item = input('Enter Item: ')
            list.append(item)
        elif value ==2:
            index = int(input('Enter item number you want to edit: '))
            item = input('Enter new item: ')
            list[index-1] = item
        elif value ==3:
            pass
        elif value ==4:
            index = int(input('Enter item number you want to delete: '))
            list.pop(index-1)
        elif value ==5:
            pass
        elif value ==6:
            print()
            print('CHECK LIST'.center(50, '♥'))
            for i,x in enumerate(list):
                print(i+1, x)
            print()




        


main()
