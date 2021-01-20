def common_denoms(denom_1, denom_2, range_start = 1, range_end = 1001):
    from statistics import mean
    common_denoms = []
    for x in range(range_start, range_end):
        if (x % denom_1 == 0 and x % denom_2 == 0):
            common_denoms.append(x)
    denom_dictionary = {"found_denoms": common_denoms, "mean_value" : mean(common_denoms)}
    return denom_dictionary

def guess_the_number(lower_limit = 1, upper_limit = 100):
    from random import randint
    from math import trunc
    target_number = randint(lower_limit, upper_limit)
    help_upper = upper_limit #Highest number the user has guessed
    help_lower = lower_limit #Lowest number the user has guessed
    user_input = ""
    while (user_input != str(target_number)):
        user_input = input("Gissa talet. Talet är => %d och <= %d \n" % (help_lower, help_upper)).strip()
        if not user_input.replace(".", "", 1).removeprefix("-").isnumeric(): #remove prefix requires python 3.9
            print("%s är inte ett nummer, försök igen" % user_input)
            continue
        float_user_input = float(user_input) #Python doesn't allow code between the elifs so had to break them up
        int_user_input = trunc(float_user_input)
        if not (int_user_input - float_user_input == 0): #Whole number check
            print("%s kan inte användas som ett heltal, försök igen" % user_input)
            continue
        elif int_user_input < lower_limit or int_user_input > upper_limit: #Within range check
            print("%s är utanför talrymden %d-%d, försök igen" % (user_input, lower_limit, upper_limit))
            continue
        elif int_user_input > target_number: #If larger than target
            print("%s är större än målet" % user_input)
            if int_user_input < help_upper:
                help_upper = int_user_input
            continue
        elif int_user_input < target_number: #If smaller than target
            print("%s är mindre än målet" % user_input)
            if int_user_input > help_lower:
                help_lower = int_user_input
            continue
    print("GRATTIS du har gissat rätt")