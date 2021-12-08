# First Repeating Element

# Given an array arr[] of size n, find the first repeating element. The element should occurs more than once and the index of its first occurrence should be the smallest.

array = [ 1, 5, 3, 4, 3, 5, 6 ]
library = {}

for index in range ( 0 , len ( array ) ) :
    temp = array [ index ]

    if temp not in library :
        node = {}
        node [ "element" ] = temp
        node [ "count" ] = 1
        node [ "min_index" ] = index
        library [ temp ] = node

    else : 
        library [ temp ] [ "count" ] += 1

min_repeating_index = len ( array )

for node in library :

    if library [ node ] [ "count" ] != 1 :
        temp = library [ node ] [ "min_index" ]

        if temp < min_repeating_index :
            min_repeating_index = temp

print ( min_repeating_index +1 , "th position element" )
