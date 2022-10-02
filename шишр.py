
def is_simple(sec):
    prist = True
    for i in range(2, sec):
        if sec % i == 0:
            prist = False
    return prist

def choose_simple(some_list):
    result = []
    for i,k in enumerate(some_list):
        if is_simple(i):
            result.append(k)
    return  result

#def fibonati(sec):
    #fi = (1,1)
    #for i in range(3):

list1 = [i+5 for i in range(5)]
print(choose_simple(list1))

