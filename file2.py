#запуск фукции:
# *название функции* (*значение*)
#например message('привет') или sq(2)

def message (x):
    return ("message: " + x + ' !')
#типо тебе сообщение отправили

def sq(x):
	return x**2
# возводит в квадрат

def q(x):
    return (x+'q')
z = ['w','r','t','s']
y = list(map(q,z))
#прибавляет ко всему 'q'


def one(x):
    if x % 2 != 0:
        x = x + 1
    else:
        pass
    return(x)
k = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c = list(map(one,k))
#уничтожает нечетные числа в списке

def up(x):
    return(str.upper(x))
bu = ['hi','then','hello','daniel','kurban']
t = list(map(up,bu))
#все буквы в списке становятся большими



def ot(x):
    return x >= 30000
money = [12332,45433,23441,41351,68943,12345,34565,14145,62454,14345,4612,]
f = list(filter(ot,money))
#ищет значение больше 30000


tr = lambda money: money > 30000
g = list(filter(tr,money))
#ищет значение больше 30000, но через лямбду

