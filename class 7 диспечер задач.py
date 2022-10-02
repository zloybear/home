class Steck(list):
    def return_last(self):
        if len(self.keys()) > 0:
            if len(self[max(self.keys())]) > 1:
                return self[max(self.keys())].return_last()
            else:
                return self.pop(max(self.keys())).return_last()
        else:
            return 'нет задач'

class work(self):
    while True:
        do = input('что делает (1 - записавает задачу 2 - спрашиваем задачу)')
        if do == '1':
            self.get_task()
        

class Disp(dict):
    def get_task(self):
        task = input('задача: ')
        priority = int(input('приворитет: '))
        if priority in self.keys():
            self[priority].append(task)
        else:
            self[priority] = Steck()
            self[priority].append(task)

    def return_task(self):
        return self[max(self.keys())].return_last

disp1 = Disp
disp1.get_task()
print(disp1.return_task)