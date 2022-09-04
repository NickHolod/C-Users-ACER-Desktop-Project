def check_email(email):
      def check_domen(email):
        counter = 0
        domens = ['ru', 'com']
        email = email.split('@')
        splited = email[1].split('.')
        for domen in domens:
          if domen in splited:
            counter +=1
        if counter > 1:
            return False
        if counter == 0:
            return False
        return True
        
      counter_of_dog = 0
      if '@' not in email:
        return False
      for i in email:
        if i == '@':
          counter_of_dog += 1 
        if counter_of_dog > 1:
          return False
      if check_domen == False:
        return False
      return True

def number_check(number):
  if len(number) > 13:
    return False
  if len(number) < 10:
    return False
  if not(number[0] == '8' or number[0:2] == '+7'):
    return False 

def information():
  print(newie.info())

def adding():
  name = input('Enter name: ')
  email = input('Enter email: ')
  number = input('Enter number: ')
  newie.add(name, email, number)
  
  
def deleting():
  del_name = input('Enter name of the contact: ')
  newie.delete(del_name)

def changing_email():
  em_name = input('Enter name of the contact: ')
  newie.change_email(em_name)

def changing_number():
  num_name = input('Enter name of the contact: ')
  newie.change_number(num_name)

def changing_email():
  em_name = input('Enter name of the contact: ')
  newie.change_email(em_name)

def reading():
  r_path = input('Enter path: ')
  newie.read(r_path)

def saving():
  s_path = input('Enter path of saving: ')
  newie.save(s_path)