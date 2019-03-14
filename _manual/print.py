"""
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    file:  a file-like object (stream); defaults to the current sys.stdout.
    flush: whether to forcibly flush the stream.
"""
# code for disabling the softspace feature
# return GFG
print('G', 'F', 'G', sep='')

# for formatting a date
# return 09-12-2016
print('09', '12', '2016', sep='-')

# another example
# return deecoob@simplesorb.com
print('deecoob', 'simplesorb.com', sep='@')

# end of string
# return python@simplesorb.com
print("python", end='@')
print("simplesorb.com")

#
print("Same text", file=sys.stdout)

