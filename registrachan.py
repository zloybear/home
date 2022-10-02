with open('register_good.txt', 'w') as f1:
    with open('register_bad.txt', 'w') as f2:
        with open('register_base.txt') as registration:
            for record in registration:
                try:
                    line = record.split()
                    if len(line) != 3:
                        raise EOFError
                    if not line[0].isalpha():
                        raise EnvironmentError
                    if '@' not in line[1] or '.' not in line[1]:
                        raise AttributeError
                    if not line[2].isalnum() or int(line[2]) < 14 or int(line[2]) > 99:
                            raise ArithmeticError
                except EOFError:
                    f2.write(f'{record[:-1]} до пиши \n')
                except EnvironmentError:
                    f2.write(f'{record[:-1]} ошибка имени \n')
                except AttributeError:
                    f2.write(f'{record[:-1]} ошибка почта \n')
                except ArithmeticError:
                    f2.write(f'{record[:-1]} ошибка возраста \n')
                except ValueError:
                    f2.write(f'{record[:-1]} ошибка возраста \n')
                else:
                    f1.write(record)