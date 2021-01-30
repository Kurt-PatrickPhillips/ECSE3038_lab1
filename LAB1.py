# kurt-patrick(620108541)
# Lab1

# Q1 Hello World
def hello():
    # this line displays the sentence
    print("ECSE3038 - Engineering IoT Systems")
# Q2 Password Validation
# more than 7 characters
# atleast 2 numbers and alphanumeric


def ValidatePassword(Pwrd):
    Inc = 0
# password should be more than 7 characters and alphanumeric
    if len(Pwrd) > 7 and Pwrd.isalnum():
        for character in Pwrd:
            # password should contain at least 2 numbers
            if character.isdigit():
                Inc += 1
        if Inc >= 2:
            return True
        else:
            return False
    else:
        return False


# Q3 Number addition

def SumUpToN(num):
    digit = 0
    num = num+1
    # check if number entered more than -1
    if num < 1:
        return -1
    else:
        # adds numbers inbetween number input and one
        for inc in range(1, num+1):
            digit = digit+inc
    return digit

    hello()
    print(ValidatePassword(sadlkj876))
    print(SumUpToN(21))
