first_name = input('Enter your First Name:')

last_name = input('Enter your Last Name:')

def hello(first_name:str=None, last_name:str=None):
    if not last_name:
        print(f'Hello {first_name}!')
    else:
        print(f'Hello {first_name} {last_name}!')

hello(first_name, last_name)
