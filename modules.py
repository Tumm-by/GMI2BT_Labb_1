def common_denoms(denom_1, denom_2, range_start = 1, range_end = 1001):
    common_denoms = []
    for x in range(range_start, range_end):
        if (x % denom_1 == 0 and x % denom_2 == 0):
            common_denoms.append(x)
    return common_denoms

def guess_the_number(lower_limit = 1, upper_limit = 100):
    from random import randint
    target_number = randint(lower_limit, upper_limit)
    help_upper = upper_limit
    help_lower = lower_limit
    user_input = ""
    while (user_input != str(target_number)):
        user_input = input("Gissa talet. Talet är => %d och <= %d \n" % (help_lower, help_upper)).strip()
        if not user_input.replace(".", "", 1).removeprefix("-").isnumeric(): #remove prefix requires python 3.9
            print("%s är inte ett nummer, försök igen" % user_input)
            continue
        elif not (int(user_input) - float(user_input) == 0):
            print("%s är inte ett heltal, försök igen" % user_input)
            continue
        elif int(user_input) < lower_limit or int(user_input) > upper_limit:
            print("%s är utanför talrymden %d-%d, försök igen" % (user_input, lower_limit, upper_limit))
            continue
        elif int(user_input) > target_number:
            print("%s är större än målet" % user_input)
            if int(user_input) < upper_limit:
                help_upper = int(user_input)
            continue
        elif int(user_input) < target_number:
            print("%s är mindre än målet" % user_input)
            if int(user_input) > lower_limit:
                help_lower = int(user_input)
            continue
    print("GRATTIS du har gissat rätt")