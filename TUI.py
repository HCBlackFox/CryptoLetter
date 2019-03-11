import os
from time import localtime, strftime





						     


def chatid(renick,nick):
	x = 0
	y = 0
	z = 0
	for i in renick:
		x = ord(i) + x
	for i in nick:
		y = ord(i) + y
	z = x * y
	return z


def dialog(renick,nick):
	renick = str(renick)
	c6 = "http://hcbf.000webhostapp.com/RSA/" + renick + "/message" + str(chatid(renick,nick)) + ".txt"

	os.system('cls')
	print(' ________________________ \n|' + '            |Local Date:|_______\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + renick)
	
	print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾|	      |\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b‾|‾'''  + strftime(" %Y-%m-%d %H:%M:%S|", localtime()))
	print('''|‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾_‾|''')
	return c6





	

def dialogs():
		os.system('cls')
		print('''|— Chats ——————|————―''')
		DIR = 'Dialogues/'
		i = 1
		a = len(os.listdir(DIR))
		for name in os.listdir(DIR):
			print('|' + '              |\b\b\b\b\b\b\b\b\b\b\b\b\b\b' + str(i) + '.' + name )
			if i == a:
				print('|______________|______________\n' + '|---Press 99 to create a chat.|\n|-----:>',end='')
			i = i + 1
		index = input('')
		return index,i

def login():
    os.system('cls')
    print('''
_____________________________________
|				    |
|  _                                |
| /_/ _  _  .  __/_ _  _            |
|/ \ /_'/_// _\ /  /_'/             |
|       _/                          |
|              _                    |
|             /_/ _  _  _     _ _/_ |
|            / / /_ /_ /_//_// //   |
|___________________________________|                                     	
_____________________________________                         ''')
    username = input('''|Username:                          |\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b''')
    password = input('''|Password:                          |\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b''')
    print('|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|')

    print('''|Register Successfully)             |_______''')
    return username , password


def createchat():
                renick = input("|What is your recipient's nickname  |\n|>                                  |\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b") 
                return renick

                                       
