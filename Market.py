import random as ram
import time

END = 0
cash = 250
popul = 2
coof = 0
Concur = 1
Days = 0
bcost = 150
bcol = 0
ocost = 125
opt = 5
value = 0


print('Добро пожаловать в симулятор рынка! \nНапишите любое сообщение снизу чтобы начать!')
STARTING = input()

print('Выберите сложность\n 1 = Простая\n 2 = Средняя\n 3 = Тяжёлая')
DIFF = int(input())
if DIFF == 1:
    coof = 1.25
elif DIFF == 2:
    coof = 1.2
elif DIFF == 3:
    coof = 1

def SkipDay():
    global cash
    global popul
    global coof
    global Concur
    global Days
    global bcol
    global opt
    global END
    time.sleep(1)
    popul += 1 * Concur + bcol + ram.randint(0,1)
    if popul < 0:
        popul = 0
    if opt<popul:
            opt += 5
    if cash > 10 * opt:
        cash -= 10 * opt
    else:
        print("\nВы проиграли! У вас не осталось денег!")
        exit()
    cash += 11 * coof * popul
    if Days == 3:
        Concur -= 1
        Days = 0

    Days += 1
    print('\nДень прошел.')
    print('Вы получили:')
    print(11 * coof * popul)
    print('Вы потратили:')
    print(10 * opt)
    print('Конкурентов:')
    print((Concur-1) * -1)
    print('Ваш баланс:')
    print(cash)
    print('Ваши покупатели:')
    print(popul)
def MinusCon():
    global cash
    global coof
    global Concur
    if cash > 100 / coof * (Concur-1) * -1:
        time.sleep(1)
        cash -= 100 / coof * (Concur-1) * -1
        print('\nВы избавились от конкурентов с помощью DDoS атак. Вам обошлось это в:')
        print(100 /coof * (Concur-1) * -1)
        print('Ваш баланс:')
        print(cash)
        Concur = 1
    else:
        print('\nВам не хватило денег')

def banner():
    global cash
    global popul
    global bcost
    global bcol
    if cash > bcost:
        time.sleep(1)
        bcol += 1 
        cash -= bcost
        bcost *= 1.5
        print('Ваш баланс:')
        print(cash)
    else:
        print('Вам не хватило денег')

def offer():
    global cash
    global popul
    global ocost
    global opt
    if cash > ocost:
        time.sleep(1)
        popul += 3 
        cash -= ocost
        ocost *= 1.5
        print('Ваш баланс:')
        print(cash)
    else:
        print('Вам не хватило денег')
def contract():
    global cash
    global Concur
    global coof
    time.sleep(1)
    Concur -= 1
    cash += 100*coof
    print('Договор заключён!')
    print('Ваш баланс:')
    print(cash)

SkipDay()
while END == 0:
    print('\nЧто делать?\n 1 = Пропустить день  \n 2 = Купить рекламу(+1 каждый день)  \n 3 = Устранить Конкурентов\n 4 = Устроить акционный день (+3),\n 5 = Заключить договор с конкуренцией (+ деньги, + конкуренты)')
    print('За 1 день можно сделать только 3 действия!')

    a = int(input())
    
    if a == 1:
        SkipDay()
        value = 0
        continue
    elif a == 2:
        print('\nКупить рекламу за:')
        print(bcost)
        print('[Y/N]')
        if input() == 'Y':
            banner()
            value += 1
        
    elif a == 3:
        print('\nна устранение 1 конкурента требуется 100$. Устранить?')
        print('[Y/N]')
        if input() == 'Y':
            MinusCon()
            value += 1
    elif a == 4:
        print('\nОрганизовать акцию за:')
        print(ocost)
        print('[Y/N]')
        if input() == 'Y':
            offer()
            value += 1
    elif a == 5:
        print('\nЗаключить договор?')
        print('+ ±100, + 1 конкурент')
        print('[Y/N]')
        if input() == 'Y':
            contract()
            value += 1
    if value >= 3:
        print('\n')
        SkipDay()
        value = 0