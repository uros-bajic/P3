"""Demonstrates peculiarities of if, for, while and other statements.
"""


def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings (), but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    imagine = 'Imagine'
    if imagine is 'Imagine':
        print(True)
    if imagine:
        print(True)
    print()

    # u pythonu nema switcheva kao u javi, zapravo i u javi switch
    # radi kao vise elifova - u pythonu elif zamenjuje switch

    if imagine:
        print(True)
    elif 23:
        print(True)
    elif ['Imagine']:
        print(True)
    else:
        print(False)



def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    a = [1, 2, 4, 5, 6]
    for i in a[2:-2]:
        print(i)

    for i in range(0, 10, 3):
        print(i)
    print()

    for _ in range(4): # ako indeks nije bitan
        print('Imagine')
    print()

    i = 0
    while i < 5:
        print(i)
        i += 1


if __name__ == '__main__':

    # demonstrate_branching()
    demonstrate_loops()