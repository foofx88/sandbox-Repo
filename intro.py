first_name = input('Enter your First Name:')

last_name = input('Enter your Last Name:')

def hello(first_name:str, last_name:str=None):
    print(f'Hello {first_name} {last_name}!')