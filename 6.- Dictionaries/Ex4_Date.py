# Ask for format date DD/MM/YYYY and display it with a message

print("")
months = {1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'}

date = input('Type a date in format DD/MM/YYYY: ')
date = date.split('/')

print("")
print(date[0], 'of', months[int(date[1])], 'from', date[2])