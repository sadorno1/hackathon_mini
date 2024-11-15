


list=[]#assumiendo q la lista se llama u_list
item_hist=open("item_history.txt","a+")

def cross_item():
    c_item=int(input("Cross Out Item Number:    ")-1)
    first_let=list[c_item][0]
    last_let=list[c_item][-1]
    dash=" "
    for letter in range(len(list[c_item])-2):
        dash+="-"
    crossed=(first_let+dash+last_let)
    list.insert(c_item+1,crossed)
    list.pop(c_item)
    return

def delete_item():
    del_item=int(input("Delete Item Number: ")-1)
    item_hist.write(f'{del_item+1}) {list[del_item]}')
    list.pop[del_item]
    return

def item_history():
    title="Deleted Item History"
    print(title.center(20,"-"))
    print(item_hist)
    return