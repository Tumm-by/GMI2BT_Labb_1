import modules

denom_1 = 7
denom_2 = 11
dict_found_denoms = modules.common_denoms(denom_1, denom_2)
print("Gemensamma nämnare för %d och %d: %s" % (denom_1, denom_2, dict_found_denoms["found_denoms"]))
print("medelvärde %0.3f" % dict_found_denoms["mean_value"])

modules.guess_the_number()