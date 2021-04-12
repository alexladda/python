# list notation     []
#
#  t   h   i   s       i   s       a       s   e   n   t   e   n   c   e
#  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17
# -18 -17 -16 -15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
# slicing           <str>[start:end:increment]      start is inclusice
#                                                   end is exclusive


sentence = "this is a sentence"

print (sentence)
print (sentence[0])
print (sentence[17])
print (sentence[-1])
print (sentence[0:4])
print (sentence[5:7])           # from index position 5 to 6
print (sentence[0:100:2])       # every other character
print (sentence[5:])            # from index position five to the end
print (sentence[5::2])          # from index position five to the end every other
print (sentence[-5:])           # last 5 characters
