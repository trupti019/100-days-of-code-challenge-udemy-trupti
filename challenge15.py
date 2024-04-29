# day 15- coffee machine project

'''make 3 hot flavours-
espresso-50  ml water 18g coffee 
latte 200ml water 24 g coffee 150 ml milk
cappuccin0 250 ml water 24 g coffee 100 ml milk

coin operated
print report

check if resources are sufficient

process coins

check transaction is successful?

make coffee- deduct resources


'''


# coins- penny(1 cent), nickel(5 cents), dime(10 cents), quarter(25 cents)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# while True:
profit = 0

def is_resource_sufficient(order_ingredients):
    for ingredient, quantity in order_ingredients.items():
            if quantity>=resources[ingredient]:
                print(f'sorry theres no enough {ingredient}')
                return False
    return True


def print_resources():
    '''prints the resources '''
    print("Current Resources:")
    for item, quantity in resources.items():
        print(f' {item} : { quantity}')
        print(f'profit -- {profit}')



def coins():
    '''takes the users coin input and processes it'''
    print('please insert coins: ')
    total_amount= int(input('enter penny: ')) * 0.01
    total_amount+=int(input('enter nickles: '))* 0.05
    total_amount+=int(input('enter dimes: '))*0.1
    total_amount+=int(input('enter quarter: '))*0.25
    return total_amount

def is_transaction_successful(money_received, drink_cost):
    if money_received>= drink_cost:
        change= round(money_received - drink_cost, 2)
        print(f'heres your change nigga : ${change}')
        global profit
        profit+= MENU[user_input]['cost']
        return True
    else: 
        print('u broke asf u lame punk ass nigga u cant buy shit--- money refunded')
        print(f'amount u entered : {money_received} and ur coffee costs {MENU[user_input]["cost"]}')
        return False
    # elif total_amount==MENU[user_input]['cost']:
    #     print('no change')
    

def minus_resources(drink_name, order_ingredients):
    '''updates the resources does not return anything'''
    for ingredient, quantity in order_ingredients.items():
            resources[ingredient]-=quantity
    print(f' heres your {user_input} hahahaha have funnnnnn!!!!')


is_on=True
while is_on:
    user_input= input('what would you like? (espresso/latte/cappuccino):').lower()
    if user_input=='off':
        is_on=False

    elif user_input=='report':
        print_resources()


    elif user_input in ['espresso', 'latte', 'cappuccino']:
        drink= MENU[user_input]
        if is_resource_sufficient(drink['ingredients']):
                    payment= coins()
                    if is_transaction_successful(payment,drink['cost']):
                        minus_resources(user_input, drink['ingredients'])
                
    elif user_input=='off':
        print('program exitted')
    else:
        print('Invalid input. Please choose from espresso, latte, cappuccino, or report.')