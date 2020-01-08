def prymitywna_wizualka (hand: list):

    pattern = (('   ',' 0 ','   '),     #1
               ('0  ','   ','  0'),     #2
               ('0  ',' 0 ','  0'),     #3
               ('0 0','   ','0 0'),     #4
               ('0 0',' 0 ','0 0'),     #5
               ('0 0','0 0','0 0')      #6
               )

    print (' ')

    for x in range(3):

        for i in hand:

               print (pattern[i-1][x], end='   ')

        print (' ')

    print (' ')     
       



    
