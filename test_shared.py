import shared as sh
sh.afunction()

# another_functio() is a function I created
sh.another_function()


# test space compress function

## if it is passed word word word it should return word word word
#print(sh.space_compress('word word word'))

## if it is passed only a multiline string should only return one line
#print(sh.space_compress('string \n new line \n another one'))

## if ti is passed an int or bool "Expected string but got {}"
#print(sh.space_compress(69402)) 
#print(sh.space_compress(True))
