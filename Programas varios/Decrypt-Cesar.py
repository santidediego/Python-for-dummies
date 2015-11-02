'''
Program to decrypt a encrypted text with Cesar Cipher
'''
def main():
    message = 'INTRODUCETHETEXTHERE'
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text=''

    for key in range(len(LETTERS)):
        for symbol in message:
            next=ord(symbol)+key
            if(next>90):
                next=64+(next-90)
            symbol=chr(next)
            text=text+symbol
        print(text)
        text=''
main()
