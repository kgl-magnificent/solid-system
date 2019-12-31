class Tv(object):
    def __init__(self, nomer_chan = 1, nomer_zvuck =1):
        self.nomer_chan = nomer_chan
        self.nomer_zvuck = nomer_zvuck
    def sound(self, value):
        self.nomer_zvuck = value
    def channel(self, number):
        self.nomer_chan = number
    def talk(self):
        print("Номер канала", self.nomer_chan, "уровень звука", self.nomer_zvuck)

def main():
    m = input("ВВедите номер канала")
    number = int(m)
    if number > 10 or number < 1:
        print("Неправильный ввод")
    k = input("Введите уровень звука")
    value = int(k)
    if value > 10 or value < 1:
        print("Неправильный ввод")
    tv = Tv()
    tv.sound(value)
    tv.channel(number)
    tv.talk()
    input("для выхода нажмите enter")
main()
