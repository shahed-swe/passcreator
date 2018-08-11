while(1):
	password = input("Enter a password:")
	print("Enter E to make easy type password")
	print("Enter N to make normal type password")
	print("Enter H to make hard type password")
	choise = input()
	if choise == 'E' or choise == 'e':
		password = list(password.split())
		password.append("123__")
		password = password[::-1]
		password.append("__345")
		password = ''.join(password)
		print(password)
		print("Do you want to try again?(y/n)")
		tr = input()
		if tr == 'Y' or tr == 'y':
			continue;
		else:
			break;
	elif choise == 'N' or choise == 'n':
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
		print("Do you want to try again?(y/n)")
		tr = input()
		if tr == 'Y' or tr == 'y':
			continue;
		else:
			break;
	elif choise == 'H' or choise == 'h':
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
		print("Do you want to try again?(y/n)")
		tr = input()
		if tr == 'Y' or tr == 'y':
			continue;
		else:
			break;
	else:
		print("Please Choose an option!!!!")

