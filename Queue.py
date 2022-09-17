print('Задание 1')
class Queue:
    __symbol = list()
    __size = 0
    __capacity = 7


    def __int__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity


#Проверка очереди на пустоту
    def isEmpty(self):
        if self.__size < 0:
            return f'Пусто'
        else:
           return f'В очереди {self.__size} элементов'

#Проверка очереди на заполнение
    def isFull(self):
        if self.__size > self.__capacity:
            return f'Переполнено'
        else:
            return f'Вы можете добавить еще элементы'

#Добавление элемента в очередь
    def enqueue(self, element: str):
        if self.__size < self.__capacity:
            self.__symbol.append(element)
            self.__size += 1
        else:
            print('Переполнено')


#Удаление элемента в очередь
    def dequeue(self):
        if self.__size > 0:
            popping = self.__symbol.pop(0)
            self.__size -= 1
            return popping
        else:
            return f'Пусто'

#Отображение всех элементов очереди на экран
    def show(self):
        return self.__symbol

    def get_size(self):
        return self.__size

    def get_capacity(self):
        return self.__capacity

    def get_symbol(self):
        return self.__symbol

q = Queue()
while True:
    menu = ('Проверка очереди на пустоту',
            'Проверка очереди на заполнение',
            'Добавление элемента в очередь',
            'Удаление элемента в очередь',
            'Отображение всех элементов очереди на экран',
            'Выход')
    count = 0
    print('-------------------------------------------------------------------------------')
    for i in menu:
        count += 1
        print(count, " - ", i)
    print('-------------------------------------------------------------------------------')
    x = int(input('Выберите действие которое вы хотите выполнить: '))
    print()
    if x == 1:
        print(q.isEmpty())
    if x == 2:
        print(q.isFull())
    if x == 3:
        y = input('Введите символ, который Вы хотите добавить: ')
        q.enqueue(y)
        print(q.get_symbol())
    if x == 4:
        print(f'Вы удалили символ: {q.dequeue()}')
    if x == 5:
        print(q.show())
    if x == 6:
        break



# q.enqueue('*')
# q.enqueue('@')
# q.enqueue('&')
# q.enqueue('-')
# q.enqueue('+')
# q.enqueue('=')
# q.enqueue('^')
# print(q.enqueue('/'))
# print(q.get_size())
# print(q.get_capacity())
# print(q.show())
# print(q.dequeue())
# print(q.show())
# print(q.isFull())


print('Задание 2')

class Queue_priority:
    __symbol = list()
    __priority = list()
    __size = 0
    __capacity = 0

    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    # Проверка очереди на пустоту
    def IsEmpty(self):
        if self.__size < 0:
            return f'Пусто'
        else:
            return f'В очереди {self.__size} элементов'


     # Проверка очереди на заполнение
    def isFull(self):
        if self.__size > self.__capacity:
            return f'Переполнено'
        else:
            return f'Вы можете добавить еще элементы'

    #Добавление элемента c приоритетом в очередь
    def InsertWithPriority(self, element: any, priority: int):
        if self.__size < self.__capacity:
            self.__symbol.append(element)
            self.__priority.append(priority)
            self.__size += 1
        else:
            return None

    #удаление элемента с самым высоким приоритетом из очереди
    def PullHighestPriorityElement(self):
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            popping = self.__symbol.pop(index_max_priority)
            self.__priority.pop(index_max_priority)
            self.__size -= 1
            return popping
        else:
            return None

    # возврат самого большого по приоритету элемента
    def Peek(self):
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            peek = self.__symbol[index_max_priority]
            print(self.__symbol)
            return f'Символ: {peek} - приоритет: {max_priority}'

    #отображение всех элементов очереди на экран
    def Show(self):
        if self.__size > 0:
            symbol_priority = dict(zip(self.__symbol, self.__priority))
            return symbol_priority
        else:
            return f'В очереди нет элементов'


    def get_size(self):
        return self.__size

    def get_capacity(self):
        return self.__capacity

    def get_symbol(self):
        return self.__symbol

    def get_priority(self):
        return self.__priority

qp = Queue_priority(7)
while True:
    menu = ('Проверка очереди на пустоту',
            'Проверка очереди на заполнение',
            'Добавление элемента c приоритетом в очередь',
            'Удаление элемента с самым высоким приоритетом из очереди',
            'Отображение всех элементов очереди на экран',
            'Выход')
    count = 0
    print('-------------------------------------------------------------------------------')
    for i in menu:
        count += 1
        print(count, " - ", i)
    print('-------------------------------------------------------------------------------')
    x = int(input('Выберите действие которое вы хотите выполнить: '))
    print()
    if x == 1:
        print(qp.IsEmpty())
    if x == 2:
        print(qp.isFull())
    if x == 3:
        symbol = input('Введите символ, который Вы хотите добавить: ')
        priority = int(input('Введите приоритет символа от 1 -10: '))
        qp.InsertWithPriority(symbol, priority)
        print(qp.get_symbol())
        print(qp.get_priority())
    if x == 4:
        print(f'Вы удалили символ: {qp.PullHighestPriorityElement()}')
    if x == 5:
        print(qp.Show())
    if x == 6:
        break
# print(qp.isFull())
# print(qp.IsEmpty())
# qp.InsertWithPriority('/', 4)
# qp.InsertWithPriority('*', 10)
# qp.InsertWithPriority('-', 8)
# print(qp.Peek())
# print(qp.IsEmpty())
# print(qp.Show())


print('Задание 3')

class Storage:
    __user = list()
    __log = list()
    __pin = list()
    __size = 0
    __capacity = 0


    def __init__(self, capacity: int):
        if capacity > 0:
            self.__capacity = capacity

    #Добавить нового пользователя
    def add(self, user: str, log: any, pin: any):
        if self.__size < self.__capacity:
            self.__user.append(user)
            self.__log.append(log)
            self.__pin.append(pin)
            self.__size += 1
        else:
            print('Переполнено')
    #Удалить существующего пользователя
    def pop(self, element: any):
        if self.__size > 0:
            if element in self.__user:
                index_element = self.__user.index(element)
                popping_user = self.__user.pop(index_element)
                popping_log = self.__log.pop(index_element)
                popping_pin = self.__pin.pop(index_element)
                self.__size -= 1
                return f'Вы удалили - user :{popping_user}  log : {popping_log}  pin : {popping_pin}'
        else:
            print('Пусто')

    #Проверить существует ли пользователь
    def check(self, person: any):
        if self.__size > 0:
            if person in self.__user:
                print('Пользователь существует')
            else:
                print('Такого пользователя не существует')
        else:
            return None

    #Изменить логин существующего пользователя
    def change_log(self, element: any, change_log: any):
        if self.__size > 0:
            if element in self.__user:
                index_element = self.__user.index(element)
                self.__log[index_element] = change_log
                return f'{self.__user[index_element]}: новый логин :{change_log}'
        else:
            return None

    #Изменить пароль существующего пользователя
    def change_pin(self, element: any, change_pin: any):
        if self.__size > 0:
            if element in self.__user:
                index_element = self.__user.index(element)
                self.__log[index_element] = change_pin
                return f'{self.__user[index_element]}: новый пароль :{change_pin}'
        else:
            return None


    def get_size(self):
        return self.__size

    def get_capacity(self):
        return self.__capacity

    def get_user(self):
        return self.__user

    def get_log(self):
        return self.__log

    def get_pin(self):
        return self.__pin



s = Storage(10)

while True:
    menu = ('Добавить нового пользователя',
            'Удалить существующего пользователя',
            'Проверить существует ли пользователь',
            'Изменить логин существующего пользователя',
            'Изменить пароль существующего пользователя',
            'Выход')
    count = 0
    print('-------------------------------------------------------------------------------')
    for i in menu:
        count += 1
        print(count, " - ", i)
    print('-------------------------------------------------------------------------------')
    x = int(input('Выберите действие которое вы хотите выполнить: '))
    print()
    if x == 1:
        user = input('Введите имя пользователя: ')
        log = input('Введите логин пользователя: ')
        pin = input('Введите парроль пользователя: ')
        s.add(user, log, pin)
        print(s.get_user())
        print(s.get_log())
        print(s.get_pin())

    if x == 2:
        element = input('Введите имя пользователя, которого Вы хотите удалить: ')
        s.pop(element)
        print(s.get_user())
        print(s.get_log())
        print(s.get_pin())

    if x == 3:
        person = input('Введите имя пользователя: ')
        s.check(person)

    if x == 4:
        element = input('Введите имя пользователя, у которого Вы хотите поменять логин: ')
        change_log = input('Введите новый логин: ')
        s.change_log(element, change_log)
        print(s.get_user())
        print(s.get_log())
        print(s.get_pin())

    if x == 5:
        element = input('Введите имя пользователя, у которого Вы хотите поменять пароль: ')
        change_pin = input('Введите новый пароль: ')
        s.change_pin(element, change_pin)
        print(s.get_user())
        print(s.get_log())
        print(s.get_pin())

    if x == 6:
        break



# s.add('aaaaaa', 'dkfljgsdfjh', '2115746*')
# s.add('bbb', 'rghjh@FGH', '41iiiDLKF')
# print(s.get_size())
# print(s.get_user())
# print(s.pop('bbb'))
# print(s.get_size())
# s.check('fdkjg')
# s.add('qqqqqq', 'sdkjfgk@gmail.com', 'sdkgkgh5!')
# print(s.change_log('qqqqqq', '123244@i.ua'))
# print(s.get_log())
# print(s.change_pin('qqqqqq', '123456****'))