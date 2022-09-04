import tkinter as tk
from phonebook import PhoneBook
from tkinter import ttk

newie = PhoneBook()
window = tk.Tk()

def information():
	windowinf = tk.Toplevel()
	windowinf.geometry('500x500')

	new_one_columns = tk.Entry(windowinf, width = 100)
	new_one_columns.pack()
	s = 'Name		Mail			Number'
	p = '		'
	new_one_columns.insert(0, s)
	for i in range(len(newie.info())):
		new_one = tk.Entry(windowinf, width = 100)
		new_one.pack()
		new_one.insert(0, newie.info().iloc[i]['number']) 
		new_one.insert(0, p)
		new_one.insert(0, newie.info().iloc[i]['email'])
		new_one.insert(0, p)
		new_one.insert(0, newie.info().iloc[i]['name'])
		print(i)
def adding():
	def button_adding():
		name = widget_entry_name.get()
		email = widget_entry_email.get()
		number = widget_entry_number.get()


		newie.add(name, email, number)

	windowadd = tk.Toplevel()
	windowadd.geometry('300x250')

	widget_label_name = tk.Label(windowadd, text = 'Enter name')
	widget_entry_name = tk.Entry(windowadd,text = 'Enter name',bg='#ffb700')
	widget_label_name.pack()
	widget_entry_name.pack()

	widget_label_email = tk.Label(windowadd, text = 'Enter email')
	widget_entry_email = tk.Entry(windowadd,text = 'Enter email',bg='#ffb700')
	widget_label_email.pack()
	widget_entry_email.pack()

	widget_label_number = tk.Label(windowadd, text = 'Enter number')
	widget_entry_number = tk.Entry(windowadd,text = 'Enter number',bg='#ffb700')
	widget_label_number.pack()
	widget_entry_number.pack()
	
	widget_button_adding = tk.Button(windowadd, text = 'add',
									width=5,
				    				height=2,
				    				background='#00cccc',
				  					foreground='black',
				  					command=button_adding)

	widget_button_adding.pack()


def deleting():
	def button_delete():
		name_del = entry_del.get()

		newie.delete(name_del)


	windowdel = tk.Toplevel()
	windowdel.geometry('300x250')

	label_del = tk.Label(windowdel, text = 'Enter name: ')
	label_del.pack()
	entry_del = tk.Entry(windowdel)
	entry_del.pack()

	button_del = tk.Button(windowdel, text = 'delete',
									width=5,
				    				height=2,
				    				background='#00cccc',
				  					foreground='black',
				  					command=button_delete)
	button_del.pack()





def changing_email():
	def button_change_email():
		old_email = entry_old.get()
		new_email = entry_new.get()

		newie.change_email(old_email, new_email)


	windowemail = tk.Toplevel()
	windowemail.geometry('300x250')

	label_email_name = tk.Label(windowemail, text = "Entry contact's name: ")
	label_email_name.pack()
	entry_old = tk.Entry(windowemail)
	entry_old.pack()
	label_email = tk.Label(windowemail, text = "Entry contact's new email: ")
	label_email.pack()
	entry_new = tk.Entry(windowemail)
	entry_new.pack()
	button_email = tk.Button(windowemail, text = 'change',
									width=5,
				    				height=2,
				    				background='#00cccc',
				  					foreground='black',
				  					command=button_change_email)
	button_email.pack()

def changing_number():
	def button_change_number():
		name_of_contact = entry_name_con.get()
		new_number = entry_new_numb.get()

		newie.change_number(name_of_contact, new_number)


	windowenumb = tk.Toplevel()
	windowenumb.geometry('300x250')

	label_numb = tk.Label(windowenumb, text = "Entry contact's name: ")
	label_numb.pack()
	entry_name_con = tk.Entry(windowenumb)
	entry_name_con.pack()
	new_numb_label = tk.Label(windowenumb, text = "Entry contact's new number: ")
	new_numb_label.pack()
	entry_new_numb = tk.Entry(windowenumb)
	entry_new_numb.pack()
	button_number = tk.Button(windowenumb, text = 'change',
									width=5,
				    				height=2,
				    				background='#00cccc',
				  					foreground='black',
				  					command=button_change_number)
	button_number.pack()


def reading():
	def button_reading():
		path = entry_read.get()
		newie.read(path)

	windowread = tk.Toplevel()
	windowread.geometry('300x250')

	label_read = tk.Label(windowread, text = 'Enter path of the file you want to read(without quotes)')
	label_read.pack()

	entry_read = tk.Entry(windowread)
	entry_read.pack()

	button_read = tk.Button(windowread, text = 'read',
									width=5,
				    				height=2,
				    				background='#00cccc',
				  					foreground='black',
				  					command=button_reading)
	button_read.pack()

def saving():
	def button_saving():
		path_s = entry_save.get() + "\\" + entry_save_name.get() + '.xlsx'
		print(path_s)
		newie.save(path_s)

	windowsave = tk.Toplevel()
	windowsave.geometry('300x250')

	label_save = tk.Label(windowsave, text = 'Enter path of the directory you want to save to(without quotes)')
	label_save.pack()

	entry_save = tk.Entry(windowsave)
	entry_save.pack()

	label_save_name = tk.Label(windowsave, text = 'Name the file')
	label_save_name.pack()

	entry_save_name = tk.Entry(windowsave)
	entry_save_name.pack()

	button_save = tk.Button(windowsave, text = 'save',
									width=5,
				    				height=2,
				    				background='#00cccc',
				  					foreground='black',
				  					command=button_saving)	
	button_save.pack()

widget_label = tk.Label(text='Hello, here is your menu. What do you want to do?',
				  foreground='black',
				  background='white') # можно указать код RGB
widget_label.pack()

widget_button = tk.Button(text = 'info',
				  width = 15,
				  height = 2,
				  background = '#00cccc',
				  foreground = 'black',
				  command = information)
widget_button.pack()
widget_button = tk.Button(text='add',
				  width=15,
				  height=2,
				  background='#00cccc',
				  foreground='black',
				  command = adding)
				  
widget_button.pack()
widget_button = tk.Button(text='delete',
				  width=15,
				  height=2,
				  background='#00cccc',
				  foreground='black',
				  command = deleting)
widget_button.pack()
widget_button = tk.Button(text='change_email',
				  width=15,
				  height=2,
				  background='#00cccc',
				  foreground='black',
				  command = changing_email)
widget_button.pack()
widget_button = tk.Button(text='change_number',
				  width=15,
				  height=2,
				  background='#00cccc',
				  foreground='black',
				  command = changing_number)
widget_button.pack()
widget_button = tk.Button(text='read',
				  width=15,
				  height=2,
				  background='#00cccc',
				  foreground='black',
				  command = reading)
widget_button.pack()
widget_button = tk.Button(text='save',
				  width=15,
				  height=2,
				  background='#00cccc',
				  foreground='black',
				  command = saving)

widget_button.pack()
window.mainloop()
 
