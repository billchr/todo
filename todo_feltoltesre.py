mylist = [0,]
while True:
    print ('''Please specify a command (type the number): \n1.list\n2.add\n3.mark\n4.archive''')
    command = int(input())

    if command == 2:
        thing = input('Add task to do: ')
        mylist.append('[ ]' + thing)

    elif command == 1:
        print(*mylist[1:], sep='\n')

    elif command == 3:
        print(*mylist[1:], sep='\n')
        mark = int(input('Enter index of task to mark done: '))
        mylist.append(mylist.pop(mark).replace('[ ]', '[X]'))


    elif command == 4:
        print(*mylist[1:], sep='\n')
        mark = int(input('Enter index of task to archive: '))
        mylist.append(mylist.pop(mark).replace('[ ]', '\n[A]'))
