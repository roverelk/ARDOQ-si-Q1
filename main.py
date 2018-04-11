
def main():
    calculations(manual_enter())

def manual_enter():
    print('Pleace give a row of numbers to be multiplied. '
          '\nEach number given with a space between.'
          '\nPress ENTER when all chosen numbers are entered.')

    num_input = input('Enter numbers: ')
    num_input += ' '

    return num_input

def calculations(num_input):
    num_list = []

    try:
        num_ = ''
        for i in num_input:
            if i == ' ':
                if num_ != '':
                    num_list.append(float(num_))
                    num_ = ''
            else:
                num_ = num_ + i

        print('\nYou have added the numbers:')
        num_list.sort(reverse=True)
        print(num_list)

        print('\nThe highest product of 3 of the numbers entered are:')
        print(num_list[0] * num_list[1] * num_list[2])

    except:
        print('You have added an invalid number, please try again.')

main()

