from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import tkinter as tk
from tkinter import filedialog



def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Выбранный файл:', filename, "\n")
    f = open(filename) # Открываем файл
    line = f.readline() # Читаем строку

    all_check = 0 #инициализируем переменные счетчика
    good = 0
    bad = 0
    #my_file = open("log.txt")
    good_file = open("log.txt", "w") #создаем лог файл куда будут записываться сайты на которые удалось зайти
    while line: # Пока файл не пуст крутим цикл
        all_check +=1
        print (line.replace(' ', ''))
        req = Request(line.replace(' ', ''))
        try:
            response = urlopen(req)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Ошибка: ', e.code)
        except URLError as e:
            print("--------Невозможно подключиться к серверу!!!---------\n")
            bad += 1
            #print('Reason: ', e.reason)
        except Exception:
            print("Глупец это не URL")
        else:
            print ("--------Вебсайт работает!--------\n")
            good += 1
            
            #lines = str(line)
            good_file.write(line + "\n")
        
            
        
         

        
        line = f.readline()
    good_file.close() 


        ####
        #Проверка сайта на доступность
        #gets = urllib.request.urlopen(line).getcode()
        #print(gets)
    print ("\t\t\t\t\t--------Отчет--------\n")
    print('\t\tВсего проверено: %d Не удалось подключиться: %d Удалось подключиться: %d'%(all_check,bad,good) )
    print('\tОтчет по сайтам к которым удалось подключиться находится в текущей директории в файле log.txt ')
    f.close()

root = tk.Tk()
root.title("Checker")
root.geometry('250x100')
button = tk.Button(root, text='Открыть файл',bg="white", fg="Red", command=UploadAction)
button.pack()


root.mainloop()