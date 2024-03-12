def tree_n_plus1(numero):
    """
    Calculates the Collatz sequence for a given number and prints the count of iterations.

    Parameters:
    - numero (int): The input number for the Collatz sequence.

    Example:
    >>> tree_n_plus1(6)
    La cantidad de veces: 8
    """
    i = 0
    while numero != 1:
        if numero % 2 == 0:
            numero = numero / 2
        else:
            numero = (3 * numero) + 1
        i = i + 1

    print("La cantidad de veces: " + str(i))

# Get input from the user
numero = int(input("Ingrese un número: "))
tree_n_plus1(numero)

if _name_ == "_main_":
    import doctest
    import sys

    # Verificar si se proporciona un argumento específico en la línea de comandos
    if len(sys.argv) > 1 and sys.argv[1] == "--rundoctest":
        doctest.testmod()