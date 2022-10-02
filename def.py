def gman():
    number = int(input('длина страки '))
    if number % 2 == 0 :
        list1 = [i for i in range(number)]
        print(list1)
        print(garri(list1))
        print(garri2(list1))
        print(garri3(list1))
    else:
        print('длина должна быть четной ')
        gman()
def garri(some_list):
    result = []
    k =int(len(some_list)/2)
    for i in range(k):
        result.append((some_list[i * 2],some_list[i * 2 + 1]))
        return result
def garri2(some_list):
    result = []
    k = int(len(some_list) / 2)
    for i in range(k):
        result.append((some_list[i], some_list[i + k]))
        return result
def garri3(some_list):
    result = []
    k = int(len(some_list) / 2)
    for i in range(k):
        result.append((some_list[i], some_list[k*2 -1 - i]))
        return result




gman()