# DrBinary10
# 1/24/2020

# encryption function
def encryption_f():
            # user inputs phrase that wants to be encrypted
            phrase_i = input("Enter phrase with each letter separated by space \n --> ")
            # user input gets split for a list for further action
            phrase_il = phrase_i.split()
            # user inputs the key(number of shifts) to encrypt message
            cck = int(input("Set the shift key : "))
            # elements in the phrase_il list gets shift to the key position
            for i in phrase_il:
                # checks if letter is out of range and resets it to the start
                # of the alphabet and continues depending on key
                if((ord(i)+cck)>122):
                    i =chr((ord(i)-122)+96)
                # positions input message with key and inputs the whole
                # new encrypted message
                print(chr(ord(i)+cck), end=" ")
            # returns to main
            main()
# decryption function            
def decryption_f():
            # user inputs the encrypted phrase that wants to be decrypted
           ephrase_i = input("Enter encrypted message with each letter separated by space \n --> ")
           # user input gets split for a list for furthert action
           ephrase_il = ephrase_i.split()
           # user inputs the key(number of shifts)
           cck = int(input("Enter the shift key : "))
           # for loop to decrypt each letter with the key
           for i in ephrase_il:
               # if letter is less than a then i will go to z and substract the remaining number of shifts
               if((ord(i)-cck)<97):
                   # for loop to decode letter
                   for j in range(cck):
                       # when(if) letter equals a then it will go two z and subtract the rest from z
                       if(ord(i)== 97):
                           # subtracts the remaining shifts
                            i=chr(123-1)
                       else:
                           # keeps subtracting shifts from letter if if above is false 
                           i = chr((ord(i)-1))
                   # adds key(number of shift) temporaly and gets subtracted later
                   i = chr(ord(i)+cck)
               # if the letter is between a and z it just subtracts the shifts and displays it
               # Decrypts the whole message
               print(chr(ord(i)-cck), end=" ")
           # returns to main
           main()
           
            #
def main():
    # user choice
    options = input("\nDo you want to encrypt or decrypt? E or D : ")
    if (options == "E"):
        encryption_f() 
    elif (options== "D"):
        decryption_f()
        # option error handler
    else:
        print("Only E(Encryption) or D(Decryption")
        main()
main()
