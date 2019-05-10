import socket
import pickle

#from Task import task


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost', 80)) # nawiazanie polaczenia
#message =input("->")
data = []





while True:
    print("Wybierz opcje:")
    print("1. Wyświetl liste zadań")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyświetl liste zadań z danym priorytetem")
    print("5. Zakończ działanie")


    choice = input('Enter your choice [1-5] : ')

    choice = int(choice)

    if choice == 1:
        message = str(choice)
        s.send(message.encode())
        table = s.recv(4096)
        data = pickle.loads(table)
        z = 0
        for task in data:      
            print("\tid : " + str(task.id), "opis : " + str(task.description),"\tpriorytet : " + str(task.priority))
            z+=1


    elif choice == 2:
        message = str(choice)
        s.send(message.encode())
        print("wyk. zadanie 2")
        description = input("podaj opis zadania : ")
        priority = input("podaj priorytet zadania [1-10] : ")
        s.send(description.encode())
        s.send(priority.encode())
        print(s.recv(1024).decode())


    elif choice == 3:
        message = str(choice)
        s.send(message.encode())
        print("wyk. zadanie 3\n")
        choice = input("podaj id do usuniecia : ")
        s.send(choice.encode())
        print(s.recv(1024).decode())


    elif choice == 4:
        message = str(choice)
        s.send(message.encode())
        print("wyk. zadanie 4\n")
        priority = input("podaj priorytet zadan do wyswietlenia : ")
        s.send(priority.encode())
        tmp_list = s.recv(4096)
        data = pickle.loads(tmp_list)
        z = 0
        for task in data:
           
            print("\tid : " + str(task.id), "opis : " + str(task.description),"\tpriorytet : " + str(task.priority))
          
            z += 1
    elif choice == 5:
        s.close()
        break
        
    
    else:
        print("podano złą wartość, spróbuj jeszcze raz!!")
        continue
