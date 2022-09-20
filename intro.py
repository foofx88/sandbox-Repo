first_name = input('Enter your First Name:')

last_name = input('Enter your Last Name:')

def hello(first_name:str=None, last_name:str=None):
    if not first_name or last_name:
        print("Wow Nameless!")
    else:
        print(f'Hello {first_name} {last_name}!')
