import system
import os


def main():
	while(1):
		print("Enter E to make easy type password")
		print("Enter N to make normal type password")
		print("Enter H to make hard type password")
		print("To close the program press C")
		choise = input("Enter your choise:")
		if choise == 'E' or choise == 'e':
			easy()
		elif choise == 'N' or choise == 'n':
			norm()
		elif choise == 'H' or choise == 'h':
			hard()
		elif choise == 'C' or choise == 'c':
			break;
		else:
			print("Wrong choise")
			os.system("cls")

def easy():
	password = input("Enter your password:")
	password = list(password.split())
	password.append("123__")
	password = password[::-1]
	password.append("__345")
	password = ''.join(password)
	print(password)
	main()

def norm():
	password = input("Enter your password:")
	length = int(len(password) / 2)
	pass1 = password[:length:]
	pass2 = password[length::]
	password = [pass1,pass2]
	password.append("$%&")
	temp = password[1]
	password[1] = password[2]
	password[2] = temp
	password = ''.join(password)
	password = list(password.split())
	password.append("$%&*?")
	password = password[::-1]
	password.append("?*&%$")
	password = ''.join(password)
	print(password)
	main()


def hard():
	password = input("Enter your password:")
	password = list(password)
	password = '?'.join(password)
	password = password[::-1]
	password = list(password)
	password = '#'.join(password)
	password = password[::-1]
	password = list(password)
	password = '%'.join(password)
	password = password[::-1]
	print(password)
	main()

if __name__ == '__main__':
	main()
