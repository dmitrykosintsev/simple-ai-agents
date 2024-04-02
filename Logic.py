"""
@author: Dmitrii Kosintsev
@date:   5 March 2024
"""

import numpy as np


class PropositionalLogic:
    """This class implements the propositional logic for three variables"""

    def __init__(self):
        # Declare the three variables
        self.P: bool
        self.Q: bool
        self.R: bool
        return

    """Implements conjunction: term1 ∧ term2"""

    def conjunction(self, term1, term2):
        return term1 and term2

    """Implements implication: Term1 => Term 2"""

    def implication(self, term1, term2):
        return not (term1 and not term2)

    """Creates a table of values using a 2D array"""

    def create_table(self):

        # Set values that can be used to access values in 2D array
        row = 0
        col = 0

        # Instantiate an empty array of shape 7x8 and type Boolean
        kb = np.zeros((8, 7), dtype=bool)

        # Go through all possible values of P, Q, and R and fill in the array using conjunction and implication
        for P in [True, False]:
            for Q in [True, False]:
                for R in [True, False]:
                    kb[row, col] = P  # Set P value and print it after
                    print("{!s:<6}".format(kb[row, col]), end=" ")
                    col += 1  # Move to the next column in the 2D array
                    kb[row, col] = Q  # Set Q value
                    print("{!s:<6}".format(kb[row, col]), end=" ")
                    col += 1
                    kb[row, col] = R  # Set R value
                    print("{!s:<6}".format(kb[row, col]), end=" ")
                    col += 1
                    kb[row, col] = self.implication(self.conjunction(P, Q), R)  # Set (P ^ Q) => R
                    print("{!s:<11}".format(kb[row, col]), end=" ")
                    col += 1
                    kb[row, col] = self.implication(Q, P)  # Set Q => P
                    print("{!s:<7}".format(kb[row, col]), end=" ")
                    col += 1
                    kb[row, col] = self.conjunction(self.conjunction(P, Q), R)  # Set kb = P ^ Q ^ R
                    print("{!s:<6}".format(kb[row, col]), end=" ")
                    col += 1
                    kb[row, col] = self.implication(kb[row, col - 1], R)  # Set kb => R
                    print("{!s:<8}".format(kb[row, col]))
                    col = 0
                    row += 1  # Move to the next row in the 2D array
        return kb

    """Prints the head of the table and calls create_table method"""
    def print_table(self):
        print("{:<6} {:<6} {:<6} {:<11} {:<7} {:<6} {:<8}".format('P', 'Q', 'R', '(P^Q) => R', 'Q => P', 'KB', 'KB => R'))
        kb = self.create_table()


# Create an object and runs the methods to print the necessary table
table = PropositionalLogic()
table.print_table()
