# cast and type functions
# cast creates a new object of the casted type
# so int(mystring) creats a new object that's
# an int instead of a cast

a = input( 'Enter A Number :' )
b = input( 'Now enter another Number :' )

sum = a + b
print( '\nData Type Sum  :', sum, type(sum) )

sum = int(a) + int(b)
print( 'Data Type Sum  :', sum, type(sum) )

sum = float(sum)
print( 'Data Type sum  :', sum, type(sum) )

sum = chr( int(sum) )
print( 'Data Type sum :', sum, type(sum) )


