import logging
import math
import operator
from functools import reduce
from typing import Union

logger = logging.getLogger("Bloger")
logging.basicConfig(filename='20.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def sum_of_numbers(*args: Union[int, float]) -> Union[int, float]:
    suma = reduce((lambda x, y: x + y), args)
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    try:
        suma
    except TypeError:
        logging.exception("Ivedete ne skaiciu!")
    else:
        return suma


def root_of_number(x: Union[int, float]) -> Union[int, float]:
    root = math.sqrt(x)
    logging.info(f"Saknis is skaiciaus {x} : {math.sqrt(x)}")
    try:
        root
    except TypeError:
        logging.exception("Ivedete ne skaiciu!")
    else:
        return root


def counting_symbols(l: str) -> int:
    kiek_sim = len(l)
    logging.info(f"Simboliu kiekis liste {l} : {len(l)}")
    try:
        kiek_sim
    except TypeError:
        logging.exception("Nieko neivedete")
    else:
        return kiek_sim


def number_division(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    dividing = operator.truediv(x, y)
    logging.info(f"Padalinus {x} is {y} gauname {dividing}")
    try:
        dividing
    except ZeroDivisionError:
        logging.exception("Dalyba is nulio negalima")
    else:
        return dividing


if __name__ == "__main__":
    print(sum_of_numbers(1, 2.7, 3, 5))
    print(root_of_number("labas"))
    print(counting_symbols("Labas vakaras!"))
    print(number_division(200, 0))
