import tkinter as tk
from phonebook import PhoneBook

newie = PhoneBook()
window = tk.Tk()
# widget 'Label'
widget_label = tk.Label(text='Hello, here is your menu. What do you want to do? \nadd - 1\ninfo - 2\nsave - 3\nchange_email - 4\nchange_number - 5\nread - 6\ndelete - 7',
				  foreground='black',
				  background='white') # можно указать код RGB

def menu_number():
	menu_number = widget_entry.get()
	if menu_number == '1':
		def adding():
			window = tk.Tk()
			widget_label = tk.Label(text="Enter contact's name, email and phone number")
			widget_entry_name = tk.Entry(width=50)
			widget_entry_email = tk.Entry(width=50)
			widget_entry_number = tk.Entry(width=50)
			newie.add(widget_entry_name, widget_entry_email, widget_entry_number)
			widget_button = tk.Button(text='Ok',
				  width = 5,
				  height = 2,
				  background = 'blue',
				  foreground = 'yellow',
				  command = adding)
			widget_label.pack()
			widget_entry_name.pack()
			widget_entry_email.pack()
			widget_entry_number.pack()
			widget_button.pack()
			window.mainloop()
# переменные, функции логика
		def getting_info():
			window = tk.Tk()
			widget_label = tk.Label(text = 'Here is all your contacts')
			print(newie.info())
			widget_label.pack()
			window.mainloop()

		def saving():

			def deep_save():
				newie.save(widget_entry_path)
			window = tk.Tk()
			widget_label = tk.Label(text = 'Where to save?')
			widget_entry_path = tk.Entry(width=50)
			widget_button = tk.Button(text='save',
				  width=5,
				  height=2,
				  background='blue',
				  foreground='yellow',
				  command=) #нужна либо глобальная переменная либо параметр фиксированный внутри функции, которая запускается с помощью кнопки
			
			widget_label.pack()
			widget_entry_path.pack()
			widget_button.pack()
			window.mainloop()

		def changing_email():
			window = tk.Tk()
			widget_label = tk.Label(text = 'Which email you want to change? Enter name of the contact')
			widget_entry_name = tk.Entry(width=50)
			widget_button = tk.Button(text='Ok',
				  width=5,
				  height=2,
				  background='blue',
				  foreground='yellow',
				  command=newie.change_email(widget_entry_name))
			widget_entry_name.pack()
			widget_label.pack()
			widget_button.pack()
			window.mainloop()

		def reading():
			window = tk.Tk()
			widget_label = tk.Label(text = 'Enter the location of the file you want to read')
			widget_entry_read = tk.Entry(width = 100)
			widget_button = tk.Button(text='Ok',
				  width=5,
				  height=2,
				  background='blue',
				  foreground='yellow',
				  command=newie.read(widget_entry_read))
			widget_entry_read.pack()
			widget_label.pack()
			widget_button.pack()
			window.mainloop()

		def deleting():
			window = tk.Tk()
			widget_label = tk.Label(text = 'Enter the name of the contact you wnat to delete')
			widget_entry_name = tk.Entry(width = 50)
			widget_button = tk.Button(text='Ok',
				  width=5,
				  height=2,
				  background='blue',
				  foreground='yellow',
				  command=newie.delete(widget_entry_name))
			widget_entry_name.pack()
			widget_label.pack()
			widget_button.pack()
			window.mainloop()
# widget 'Button'
widget_button = tk.Button(text='Ok',
				  width=5,
				  height=2,
				  background='blue',
				  foreground='yellow',
				  command=menu_number)
# widget 'Entry'
widget_entry = tk.Entry(width=50)

widget_entry.pack()
widget_label.pack()
widget_button.pack()

name = widget_entry.get() # read the content of the entry
print(name)

#widget_entry.insert(0, 'Hello, world') # write something in the enrty
window.mainloop()