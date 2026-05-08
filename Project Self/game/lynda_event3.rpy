label lyndaevent3:
if lynda_rating =<2:
    jump lyndaevent3bad
elif lynda_rating =>5:
    jump lyndaevent3neut
elif lynda_rating =>8:
    jump lyndaevent3good
