# Caesar_encryption_decryption
    #### Video Demo:  https://youtu.be/i0sYLZbyadw
    #### Description: This project is about basic caesar encryption and decryption:

    Encryption:

    Encryption is the method by which information is converted into secret code that hides the information's true meaning. Cryptography is a science that encrypts and decrypts information.

    Encryption:  plaintext + key = ciphertext

    Here when we give input plaintext , key to encrypt function it gives us cipher text

    Decryption:

    Decryption is the process of transforming data that has been rendered unreadable through encryption back to its unencrypted form. In decryption, the system extracts and converts the garbled data and transforms it to texts and images that are easily understandable not only by the reader but also by the system. It is generally a reverse process of encryption.

    ciphertext + key =  plaintext

    Here we give ciphertext,key as inputs to decrypt function we get output as plain text

    In this project I impeleted five functions other than main i.e.encrypt, decrypt, validations, take_input, display_out

    flow is like this program execution starts from main first it call validations function based on user input it calls encrypt or decrypt function and that ouput is handled back to main function

    validations function :
        it checks if len of arguments should be 2 if not it exits program.
        if len of arguments is 2 it checks for second argument either is "-e" or "-d"
        "-e" : encryption
        "-d" : decryption
        after that it takes input from the user and called either encrypt or decrypt function

    encrypt function:
        inputs are plaintext , key
        outputs is cipher text
        so basically alphabets are 26 so every alphabet has ascii value so we add key value to that after that we perform mod operation
    decrypt function:
        inputs are ciphertext key
        output is plain text
        Here we subtract key value and perform mod operation.

    display_out fucntion
        This function displays the output function.

    test_project.py:
        This is implemented to automatically test the function of encrypt and decrypt functions.