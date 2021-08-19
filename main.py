#def name_function():
    #print('Привет!')


#name_function()


#def name_function(name):
    #print('Привет, '+ name)


#name_function("Борис")


#def name_function(name='Андрей'):
    #print('Привет, '+ name)


#name_function()


#def say_hello(name = "ИМЯ"):
    #return 'Привет, '+ name


#result = say_hello("ИМЯ3")

#print(result)


#def add(n1,n2):
    #return n1+n2


#result = add(20,30)

#print(result)


#def cat_check(mystring):
    #if 'Кот' in mystring:
        #return True
    #else:
        #return False


#print(cat_check('Кот пришёл в дом'))
#print(cat_check('У нас есть кот'))


#def cat_check(mystring):
    #if 'кот' in mystring.lower():
        #return True
    #else:
        #return False


#print(cat_check('Кот пришёл в дом'))
#print(cat_check('У нас есть кот'))


#def cat_check(mystring):
    #return 'кот' in mystring.lower()


#print(cat_check('Кот пришёл в дом'))
#print(cat_check('У нас есть кот'))


def pig_latin(word):
    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin('word'))
print(pig_latin('apple'))
