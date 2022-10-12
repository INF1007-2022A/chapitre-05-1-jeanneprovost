#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    absolute = number
    if number < 0:
        absolute = -number
    return absolute


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []
    for letter in prefixes:
        names.append(letter + suffixe)
    return names


def prime_integer_summation() -> int:
    prime_list = []
    sum = 0
    i = 2
    while len(prime_list) < 100:
        prime = True
        for prime_number in prime_list:
            if i % prime_number == 0:
                prime = False
                break
        if prime:
            prime_list.append(i)
            sum += i
        i += 1

    return sum


def factorial(number: int) -> int:
    fact = 1
    for i in range(number,0,-1):
        fact = fact*i

    return fact


def use_continue() -> None:
    for i in range(10):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    list_verify = []
    for group in groups:
        valid = True
        number_seventy = 0
        number_fifty = 0

        if len(group) > 10 or len(group) <= 3:
            valid = False
        else:
            for person in group:
                if person < 18:
                    valid = False
                    break
                elif person > 70:
                    number_seventy += 1
                elif person == 50:
                    number_fifty += 1
            if 25 in group:
                valid = True
            elif number_seventy == 1 and number_fifty == 1:
                valid = False
        list_verify.append(valid)

    return list_verify


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
