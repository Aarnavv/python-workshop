from functions import initialize

def main():
    ran, multiple1, multiple2 = initialize()
    message = ''
    for i in range(1, ran+1):
        if i % multiple1 == 0 or multiple1 == i % 10:
            message += 'fizz'
        if i % multiple2 == 0 or multiple2 == i % 10:
            message += 'buzz'
        
        if message == '':
            print(i)
        else:
            print(message)

        message = ''
    
if __name__ == '__main__':
    main()