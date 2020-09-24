from datetime import date


def prompAndExtractDate():
    print("Enter your birthday.")




def main():
    bornBefore = date(1988,7,16)

    ## Extract birth dates from the user
    date = prompAndExtractDate()
    while date is not None:
        if date <= bornBefore:
            print("Is at least 21 years of age..")
        date = prompAndExtractDate()


