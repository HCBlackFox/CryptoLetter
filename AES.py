from Crypto.Cipher import PKCS1_OAEP
from win10toast import ToastNotifier
from Crypto.PublicKey import RSA
from pyautogui import hotkey
import keyboard


import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
import sys, time, threading, os
import binascii, hashlib
import TUI as tui

global DIR, name, stop, toaster, c1, c2, c3, c4, c5

stop = False
toaster = ToastNotifier()
DIR = "Dialogues/"
name =  "1"
c1 = "http://hcbf.000webhostapp.com/RSA/pubrecord.php"
c2 = "http://hcbf.000webhostapp.com/RSA/"
c3 = "http://hcbf.000webhostapp.com/RSA/message.php"
c4 = "http://hcbf.000webhostapp.com/RSA/keyexchange.php"
c5 = None
end ='\n|--:>                                 |\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
b1 ='\b\b\b\b\b\b\b|'
b2 ='                                     |\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
inp = '|--:>                                 |\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'


#___________________________________________

#Key/Crypt/Decrypt

def keygen():
        privatekey = RSA.generate(2048)

        f = open('privatekey.txt','wb')
        f.write(bytes(privatekey.exportKey('PEM'))); f.close()

        publickey = privatekey.publickey()

        f = open('publickey.txt','wb')
        f.write(bytes(publickey.exportKey('PEM'))); f.close()

        print("Keypair generate succesfuly :)")
        pass


def receivepub(renick):



        data = {"user" : renick}

        encoded_data = urllib.parse.urlencode(data).encode("utf-8")
        content = urllib.request.urlopen(c4,
                encoded_data)

        pubsite = urllib.request.urlopen(c2 + renick + "/publickey.txt")
        pubkey = pubsite.read()

        f = open(DIR + str(renick) + "\\xpublickey.txt" , 'wb')
        f.write(bytes(pubkey)); f.close();
        pass


def sendpub(nick,password):
    h = hashlib.sha1(password.encode('utf-8'))
    mypub = open('publickey.txt','rb')
    data = {"pub" : mypub.read(), "nick" : nick, "pass" : h.hexdigest()}

    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    content = urllib.request.urlopen(c1,
            encoded_data)
    pass


def crypt(data,renick):
        publickey = RSA.importKey(open("Dialogues\\"+ renick + "\\xpublickey.txt",'rb').read())
        cipherrsa = PKCS1_OAEP.new(publickey)
        secdata = cipherrsa.encrypt(data.encode("utf-8"))
        return secdata


def decrypt(secdata):
        privatekey = RSA.importKey(open('privatekey.txt','rb').read())
        cipherrsa = PKCS1_OAEP.new(privatekey)
        decdata = cipherrsa.decrypt(secdata)
        return decdata

#-----------------

#Messages

def chatid(renick,nick):
    x = 0
    y = 0
    for i in renick:
        x = ord(i) + x
    for i in nick:
        y = ord(i) + y
    return x * y


def startmes(renick,nick):
        secdata = crypt("Hey I`m online!",str(renick))

        data = {"message" : secdata , "nick" : nick, "chatid" : str(chatid(renick,nick)) }

        encoded_data = urllib.parse.urlencode(data).encode("utf-8")
        content = urllib.request.urlopen(c3,
                encoded_data)


def wait(renick,nick):
        global stop, c5
        try:
            h = 1

            while True:
                        if stop == True:
                            UI(nick)

                        mes = urllib.request.urlopen(c5)
                        h2 = urllib.request.urlopen(c5).read()

                        if h != h2:
                            decmes = decrypt(mes.read()).decode()
                            print (b1 + b2 + renick + ":" + decmes ,end= end ,flush=True)
                            h = h2
        except urllib.error.URLError:
            wait(renick,nick)


def sendmessage(nick,renick):
                global stop
                while True:
                        if stop == True:
                                UI(nick)

                        secdata = crypt( input(EUI.input(33,34)),str(renick))
                        data = {"message" : secdata , "nick" : nick , "chatid" : str(chatid(renick,nick)) }

                        encoded_data = urllib.parse.urlencode(data).encode("utf-8")
                        content = urllib.request.urlopen(c3,
                                encoded_data)






#-------------------

#Notifications

def check(renick,nick):
    receivepub(renick)
    try:
        sc = "http://hcbf.000webhostapp.com/RSA/" + renick + "/message" + str(chatid(renick,nick)) + ".txt"
        h = 1
        h2 = 1

        while True:
            h2 = urllib.request.urlopen(sc).read()
            if h != h2:
                try:
                    mes = urllib.request.urlopen(sc)
                    toaster.show_toast("New message from:" + renick,
                                decrypt(mes.read()).decode(),
                                icon_path="python.ico",
                                duration=10)
                    while toaster.notification_active(): time.sleep(0.1)
                except:
                    print('ERROR: ' + renick)
                h = h2;
    except:
        print('ERROR: ' + renick)


def notifi(nick):
    global DIR
    o = os.listdir(DIR)
    x = 0
    e = 0
    while e < len(o):
        i = o[e]
        print(i)
        x = threading.Thread(target=check, args=(i, nick, ))
        x.start()
        e = e + 1
    pass



class history():
    global DIR
    def write(self,data,renick):
        fp = open(DIR + str(renick) + 'history.txt','a')
        fp.write()


        pass


    def read(self,data,renick):
        return data



#-------------

#TUI

def ProcRun(nick,renick):
        stop = False
        receivepub(renick)
        startmes(renick,nick)

        t1 = threading.Thread(target=sendmessage, args=(nick,renick ))
        t2 = threading.Thread(target=wait, args=(renick,nick ))

        t1.start()
        t2.start()

        pass




def execute():
        global stop
        os.system('cls')
        stop = True
        hotkey('enter')




class EUI:
    x = 0
    y = 0

    def input(x,y):
        return str('|--:>' + ' ' * x + '|' + '\b' * y)
    def printVer(x,y):
        return str('_' * x)
    def printHor(x,y):
        return str('|' + ' ' * x + '|')

def UI(nick):
        global c5
        index , i = tui.dialogs()


        if int(index) in range(0,i):

                renick = os.listdir(DIR)[(int(index)-1)]
                c5 = tui.dialog(renick,nick)
                ProcRun(nick,renick)

        elif index == '99':

            renick = str(tui.createchat())
            os.mkdir(DIR + str(renick))
            c5 = tui.dialog(renick,nick)

            if nick in os.listdir(DIR):
                    ProcRun(nick,renick)

            else:
                    ProcRun(nick,renick)


#--------------


if __name__ == "__main__":

        nick,password = tui.login()
        print('|Please wait, we generate a pair of RSA keys|')
        keyboard.add_hotkey('Esc', execute)
        keygen()
        sendpub(nick,password)

        notifica = threading.Thread(target=notifi, args=(nick, ))
        notifica.start()
        UI(nick)
