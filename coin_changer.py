

def main():
    print('#####################################')
    print('--------Coin Changer by Tellu--------')
    print('#####################################\n')

    while True:
        print('##############################')

        cost = numVal('Enter total cost: ')
        cash = numVal('Enter amount of cash given by the client: ')

        change(cash, cost)

        print('##############################\n\n\n')


def change(cash, cost):
    prefix = '$'
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

    change = round(cash - cost, 2)

    if change > 0:
        print('--------------------')
        print(f'Change: {prefix}{change}')
        print('--------------------')

        for denomination in denominations:
            quantity = 0
            while change >= denomination:
                change = round(change - denomination, 2)
                quantity += 1
            if quantity > 0:
                if denomination < 1:
                    prefix = ''
                    denomination = f'{int(denomination * 100)}¢'
                if quantity > 1:
                    denomination = f'{denomination} - x{quantity}'
                print(f'{prefix}{denomination}')

    elif change == 0:
        print('----------------')
        print('# No change! #')
        print('----------------')

    elif change < 0:
        print(
            '-----------------------------------------------------------------------')
        print(
            f'Not enough money! {prefix}{abs(change)} is missing!')
        print(
            '-----------------------------------------------------------------------')
    else:
        return


# Input sanitizing
def numVal(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print('Error! Only numbers are allowed! Decimals only after a dot.')
            continue

        # Checking if value isnt more than 100 mil because it takes forever to calculate the change.
        # And it checks if there isnt more than 2 decimal places.
        integer, decimal = str(value).split('.')  # Parsing inputed float
        if len(integer) > 8 or len(decimal) > 2:
            print(
                'Error! Number cant be larger than 100 million or have more than 2 decimal places!')
            continue

        else:
            return value


main()
