#!/usr/bin/python3

"""N Queens"""
import sys


def main():
    """Solves the N Queens problem"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n_queens = int(sys.argv[1])
    except Exception as error:
        print('N must be an number')
        exit(1)
    if type(n_queens) is not int:
        print('N must be an number')
        exit(1)
    if n_queens < 4:
        print('N must be at least 4')
        exit(1)
        # TODO: Solve the problem
    return [[n_queens]]


if __name__ == '__main__':
    print(main())
