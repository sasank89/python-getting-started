first_name = 'Sasank'
last_name = 'Kalipatnapu'
print (first_name+last_name)
print('Hello '+ first_name + ' '+ last_name)


#Functions on strings
sentence = 'This sentence is exciting me'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('e'))

#combining both the top concepts
first_name = input('What is your first name?')
last_name = input('What is your last name?')
print (first_name+last_name)
print('Hello '+ first_name.capitalize() + ' '+ last_name.capitalize())

#Using placeholders to format strings
output = 'Hello, '+ first_name + ' ' + last_name
output = 'Hello, {} {}'.format(first_name,last_name)
output = 'Hello, {0} {1}'.format(first_name,last_name)
#only available in Python 3
output = f'Hello, {first_name} {last_name}'

