#!/usr/bin/env python3
# Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator.
# The second variable should use all upper case characters with underscore as the word separator.
# The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.
#
#Make all three variables be strings that refer to IPv6 addresses.
#
#Use the from future technique so that any string literals in Python2 are unicode.
#
#compare if variable1 equals variable2
#compare if variable1 is not equal to variable3

from __future__ import print_function

an_example_variable = "2001:db8::1"
SECOND_EX_VAR = "2001:db8::2"
third3_Example_Var = "2001:db8::3"

print()
print("Is an_example_variable equal to SECOND_EX_VAR: {}".format(an_example_variable == SECOND_EX_VAR))
print("Is an_example_variable not equal to third3_Example_Var: {}".format(an_example_variable != third3_Example_Var))
print()
