from typing import List


def show_menu():
    print('1. Citire lista')
    print('2. Afisare numere prime')
    print('3. Afisare cea mai lunga subsecventa cu toate numerele divizibile cu 10')
    print('x. Exit')


def read_list() -> List[int]:
    lst = []
    lst_str = input('Dati numerele separate prin spatiu:')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst


def is_prime(n: int) -> bool:
    '''
    Determina daca un numar dat este prim.
    :param n: numarul dat
    :return: True daca e prim si False altfel
    '''
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True
def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(29) == True


def get_primes(lst: List[int]) -> List[int]:
    '''
    Determina numerele prime dintr-o lista.
    :param lst: lista de numere.
    :return: o lista cu numerele prima din lst.
    '''
    result = []
    for num in lst:
        if is_prime(num):
            result.append(num)
    return result


def get_longest_subarray_all_divisible_by_10(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa in care toate elementele sunt divizibile cu 10.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''

    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_div_10 = True
            for num in lst[st:dr+1]:
                if num % 10 != 0:
                    all_div_10 = False
                    break
            if all_div_10:
                if dr - st + 1 > len(result):
                    result = lst[st:dr+1]
    return result


def main():
    lst = []
    while True:
        show_menu()
        opt = input('Optiunea: ')
        if opt == '1':
            lst = read_list()
        elif opt == '2':
            primes = get_primes(lst)
            print('Numere prime din lista sunt:', primes)
        elif opt == '3':
            print('Cea mai lunga subsecv cu toate numerele divizibile cu 10 este:', get_longest_subarray_all_divisible_by_10(lst))
        elif opt == 'x':
            break
        else:
            print('Optiune invalida.')


if __name__ == '__main__':
    test_is_prime()
    main()
