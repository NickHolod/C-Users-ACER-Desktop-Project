from phonebook import PhoneBook
import tinker as tk

print('Hello world')
newie = PhoneBook()
while True:
	user_name = input('Enter your name: ')

	print(f'Hello {user_name}, I want to show you my program')
	print('You can choose one of the functions')

	print('add - 1\ninfo - 2\nsave - 3\nchange_email - 4\nchange_number - 5\nread - 6\ndelete - 7')

	decision = input('choose one of them: ')
	if decision == '1':
		print('you can add one peson into your PhoneBook')
		new_name = input('Enter name ')
		new_email = input('Enter email ')
		new_number = input('Enter number ')
		newie.add(new_name, new_email, new_number)
		print(newie.info())
	if decision == '2':
		print(newie.info())

	if decision == '3':
		print('if you want to upload contacts, enter directory of the file(path)')
		path = input('Enter path: ')
		newie.save(path)

	if decision == '4':
		email_to_change = input('Enter email you want to change')
		newie.change_email(email_to_change)

	if decision == '5':
		number_to_change = input('Enter new number')
		newie.change_number(number_to_change)

	if decision == '6':
		path_for_read = input('Enter path of the file')
		newie.read(path_for_read)

	if decision == '7':
		needless = input('Enter the name of the contact that you need to delete')
		newie.delete(needless)
