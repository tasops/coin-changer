

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
    name = ''
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
                quantity = quantity + 1
            if quantity > 0:
                if denomination < 1:
                    prefix = ''
                    name = '¢'
                    denomination = int(denomination * 100)
                if quantity > 1:
                    name = name + f' - x{quantity}'
                print(f'{prefix}{denomination} {name}')

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


def numVal(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print('Error! Only numbers are allowed! Decimals only after a dot.')
            continue
        else:
            return value


main()