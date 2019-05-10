import json
import socket
import pickle


from Task import task

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('', 80))  
s.listen(5)     

id = 0
list_with_task = []

clientsocket, address = s.accept()


with open('list_of_tasks.json', 'w') as outfile:
    json.dump(list_with_task,outfile)

while True:

    print("connection from user"+str(address))
    message = clientsocket.recv(1024).decode()  
    print("otrzymano wiadomosc : "+message)
    choice = (message)

    if choice == str(1):
        print("wyk. zadanie 1\n")
        data = pickle.dumps(list_with_task)
        clientsocket.send(data)



    elif choice == str(2):
        print("wyk. zadanie 2\n")
        description = clientsocket.recv(1024).decode()
        priority = clientsocket.recv(1024).decode()
        tmp_task = task(description,priority)
        list_with_task.append(tmp_task)
        print("dodano zadanie do tablicy \n\n\n")
        tmp = "dodano zadanie!\n"
        clientsocket.send(tmp.encode())

        json_list = []              
        for item in list_with_task:
            json_list.append(item.to_dictonary())

        with open('list_of_tasks.json', 'w') as outfile:
            json.dump(json_list, outfile)


    elif choice == str(3):
        print("wyk. zadanie 3\n")
        choice = clientsocket.recv(1024).decode()
        i = 0
        for task in list_with_task:
            tmp = task.get_id()
            if(tmp == int(choice)):
                list_with_task.pop(i)
                print("usunięto element!\n")
                tmp = "usunieto element!"
                clientsocket.send(tmp.encode())
            i+=1

        json_list = []                     
        for item in list_with_task:
            json_list.append(item.to_dictonary())

        with open('list_of_tasks.json', 'w') as outfile:
            json.dump(json_list, outfile)

    elif choice == str(4):
        print("wyk. zadanie 4\n")
        priority = clientsocket.recv(1024).decode()
        tmp_list = []
        for task in list_with_task:
            if(int(task.priority) == int(priority)):
                print("wybrano!")
                tmp_list.append(task)

        data = pickle.dumps(tmp_list)
        clientsocket.send(data)
    elif choice == str(5):
        break



clientsocket.close()
