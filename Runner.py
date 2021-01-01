import code as x 

filename = input("Enter the file name\n")

x.load(filename)

while True:
	choice = input("Enter your choice...\n1.Create\n2.Read\n3.Delete\n")

	if (choice == '1'):
		key = input("Enter the key here...")
		value = input("Enter the corresponding value...")
		ttlChoice = input("Do you want to enter time-to-live? (yes/no)")
		if ttlChoice.lower() == 'yes':
			ttl = int(input("Enter ttl, in seconds, here..."))
			x.create(key, value, ttl)
		else:
			x.create(key, value)

	elif (choice=="2"):
		key = input("Enter the key here...")
		x.read(key)

	elif (choice == "3"):
		key = input("Enter the key you want to delete...")
		x.delete(key)

	choice = input("Do you want to continue?(yes/no)")
	if choice.lower()=='no':
		break
