from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque() #Проводиться ініціалізація черги

    def add_item(self, item):
        if isinstance(item, str):
            self.queue.append(item) #Якщо передані користувачем данні це строка, тоді вона додається в чергу, інакше 
            #додавання не проводиться
            return True
        raise Exception("TypeError")
    
    def pop(self):
        if self.queue:
            self.queue.popleft()#Видалення елемента черги

    def view_list(self):
        return list(self.queue)#Вивід черги на екран як список