def fizzbuzz ():
    #for
    for number in range(1, 101):
        # Si number es múltiplo de 3 y de 5, imprime "fizzbuzz"
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        # Si number es múltiplo de 3, imprime "fizz"
        elif number % 3 == 0:
            print("fizz")
        # Si number es múltiplo de 5, imprime "buzz"
        elif number % 5 == 0:
            print("buzz")
        # Si number no es múltiplo de 3 ni de 5, imprimime el número
        else:
            print(number)

fizzbuzz() 
