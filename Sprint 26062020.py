print('Press q to quit the program at any point')
cont = 'yes'

ans = 0

op = input(('Which operation would you like to do?\nUse + for addition\nUse - for subtraction\nUse * for multiplication\nUse / for division\n'))
n1 = int(input('Enter the first value\n'))
n2 = int(input('Enter the second value\n').lower())

class calc:
    def sum(self):
        if op == '+' :
            ans = n1 + n2
        elif op == '-':
            ans = n1 - n2
        elif op == '/' :
            ans = n1 / n2
        elif op == '*' or op == 'x':
            ans = n1 * n2
    print('{} {} {} = {}'.format(n1, op, n2, ans))  
     
s1 = calc()
s1.sum()
         

