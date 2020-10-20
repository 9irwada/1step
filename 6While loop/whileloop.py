num_of_tries = 0
while num_of_tries != 5:
    username  = input('Please insert your usernmae :')
    passowrd  = input('Please insert your passowrd :')

    if username == 'Nabiot' and passowrd == '2424':
        print ('Hi Baby')
        num_of_tries = 0
        exit()
    else:
        print ('Error')
        num_of_tries +=1
        print ('you have '+ str(5 - num_of_tries   )  + " tries left" )