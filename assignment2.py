
import socket

class Assignment2:
    def __init__(self, age):
        self.age = age

    def sayWelcome(self, name):
        self.name = name
        print(f'Welcome to the assignment, {self.name}!Haven\'t seen you for {self.age} years!')


    def doubleList(self, list):
        fill = ''
        oFill = ''
        temp = 0
        newList = []

        for word in list:
            fill = word + word
            newList.append(fill)

        for word in list:
                temp = temp + 1
                if ((temp % 2) != 0):
                    newList.append(word)

        for word in list:
            temp = temp + 1
            if ((temp % 2) == 0):
               newList.append(word)
            

        return newList

    def modifyString(self, name):
        place = 0
        res = name
        for chara in name:
            place += 1
            if place % 3 == 0:
                res = res[:place - 1] + res[place - 1].upper() + res[place:]
            if place % 4 == 0 and place % 3 != 0:
                 res = res[:place - 1] + res[place - 1].lower() + res[place:]
            if place % 5 == 0 and place % 3 != 0 and place % 4 != 0:
                res = res[:place - 1] + ' ' + res[place:]

        return res

    @staticmethod
    def isGoodPassword(password):
        upperCount =0
        lowerCount = 0
        digitCount=0
        specialCount=0

        for x in password:
            if x.isupper():
                upperCount += 1
            if x.islower():
                lowerCount += 1
            if x.isdigit():
                digitCount += 1
            if '.' in x or '(' in x or ',' in x or '#' in x:
                specialCount +=1
        if len(password) < 9:
            return False
        if upperCount < 3 and lowerCount < 2:
            return False
        if specialCount < 2 and digitCount < 1:
            return False
        else:
            return True


    def connectTcp(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        try:
            sock.connect((host, port))

            return True
        except:
            return False

