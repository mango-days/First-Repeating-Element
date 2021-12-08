# First Non-Repeating Element

# Find the first non-repeating element in a given array arr of N integers. Note: Array consists of only positive and negative integers and not zero.

array = [ -1, 2, -1, 3, 2 ]

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

    if library [ node ] [ "count" ] == 1 :
        temp = library [ node ] [ "min_index" ]

        if temp < min_repeating_index :
            min_repeating_index = temp

print ( min_repeating_index +1 , "th position element" )
