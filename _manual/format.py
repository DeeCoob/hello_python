# форматирование строки в стиле C s – форматная строка, x 1 …x n – значения
# s % x
# s % (x 1 , x 2 , …, x n )
# return Python has 002 quote types.
print("%(language)s has %(number)03d quote types." % {'language': "Python", "number": 2})

# '#'	The value conversion will use the “alternate form” (where defined below).
# '0'	The conversion will be zero padded for numeric values.
# '-'	The converted value is left adjusted (overrides the '0' conversion if both are given).
# ' '	(a space) A blank should be left before a positive number (or empty string) produced by a signed conversion.
# '+'	A sign character ('+' or '-') will precede the conversion (overrides a “space” flag).


# s.format(args) 	форматирование строки в стиле C#

print("The sum of 1 + 2 + {0} is {1}".format(1+2, 6))

print("Harold's a clever {0!s}".format("boy"))        # Calls str() on the argument first
print("Bring out the holy {name!r}".format(name="1+3"))    # Calls repr() on the argument first
print("More {!a}".format("bloods"))     # Calls ascii() on the argument first