#Global Variable 
order = True

print('Welcome to the Python Coffee Shop!')
 
customer_name = input('What is your name? ')
print('Hello, ' + customer_name + '! Let\'s order some coffee.')


price_coffee = 3.50
price_latte = 4.00
price_mocha = 5.00


print('Coffee: $' + str(price_coffee))
print('Latte: $' + str(price_latte))
print(f'Mocha:${str(price_mocha)}')

while order == True:
    choice = input('What would you like to order?: ').lower()
    
    if choice == 'coffee':
        cost = price_coffee
    elif choice == 'latte':
        cost = price_latte
    elif choice == 'mocha':
        cost = price_mocha
    else:
        print('Sorry, we do not have that.')
        cost = 0
    
    quantity = int(input(f'How many cups of {choice} would you like? '))
    
    total_cost += cost * quantity
    
    if quantity > 1:
        print('You get a discount of $1.00!')
        total_cost -= 1.00
        
    ordering = input(f"Would you like to order another coffee?").lower()  #ordering more then 1 type of coffee
    if ordering == 'yes':
        order = True
    else:
        order = False
        
student = input(f'Are you a student?').lower()
if student == 'yes':     #Student discount
    total_cost = total_cost * 0.9
    
print('Your total is: $' + str(total_cost))
print('Thank you, ' + customer_name + '! Please come again.')