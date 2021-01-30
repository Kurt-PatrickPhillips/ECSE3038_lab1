#kurt-patrick(620108541)
#Lab1

#Q1 Hello World
def hello():
    print("ECSE3038 - Engineering IoT Systems") #this line displays the sentence

#Q2 Password Validation
#more than 7 characters
#atleast 2 numbers and alphanumeric
def ValidatePassword(Pwrd):
    Inc =0;

    if len(Pwrd) > 7 and Pwrd.isalnum():
        for val in Pwrd:
            if element.isdigit():
                Inc +=1
        if Inc >=2:
            return True
        else:
            return False
