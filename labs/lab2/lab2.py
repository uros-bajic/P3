"""
LAB 2
"""

"""
TASK 1:
Write a function that receives two lists and returns a new list that contains 
only those elements (without duplicates) that appear in both input lists.
"""


def common_elements(l1, l2):
    # # new_list = list()
    # new_set = set()
    # for item in l1:
    #     if item in l2:
    #         new_set.add(item)
    # return list(new_set)
    new_list = [item for item in l1 if item in l2]
    return list(set(new_list))


"""
TASK 2:
Write a function that receives 2 lists of the same length and returns a new list 
obtained by concatenating the two input lists index-wise. Example:
Input lists:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Output: ['My', 'name', 'is', 'Kelly']
"""

def concat_index_wise(l1, l2):
    # Option 1:
    # new_list = list()
    # for i in range(len(l1)):
    #     new_list.append(l1[i]+l2[i])
    # return new_list

    # Option 2:
    # return [item + l2[i] for i, item in enumerate(l1)]

    # Option 3:
    # zip() je funkcija koja vraca objeka pa ne moze da se printuje sama
    # sekvence koje se uparuju moraju da imaju iste duzine
    # pre 3.10 verzije je prolazilo precutno, tj. uzimala se duzina najkrace sekvence
    # od verzije 3.10, zip() prima i parametar strict (bool)
    # True - sve sekvence moraju biti iste duzine
    # False - ne moraju
    return [item1 + item2 for item1, item2 in zip(l1, l2)]

""" 
TASK 3:
Write a function that checks and returns whether a given string is a pangram or not.
Pangrams are sentences or phrases containing every letter of the alphabet at least once 
(for example: "The quick brown fox jumps over the lazy dog")

Hint: ascii_lowercase from the string module can be used to get all letters
"""

def pangram(string):
    from string import ascii_lowercase
    # for l in ascii_lowercase:
    #     if l not in string.lower(): return False
    # return True
    return all([l in string.lower() for l in ascii_lowercase])
    # all() vraca True ako su svi True i False ako je bar jedan
    # any() True za bar jedan, False za sve

"""
TASK 4:
Write a function that receives a string with a mix of lower and upper case letters.
The function arranges letters in such a way that all lowercase letters come first,
followed by all upper case letters. Non-letter characters (if any) are ignored, that is,
not included in the new 're-arranged' string.
The new,'re-arranged' string is the function's return value.
"""

def rearrange_string(string):
    new_list = [ch for ch in string if ch.islower()]
    new_list.extend([ch for ch in string if ch.isupper()])
    return "".join(new_list)


"""
TASK 5:
Write a function that accepts a sequence of comma separated passwords and
checks their validity using the following criteria:
1. At least 1 letter between [a-z] => At least 1 lower case letter
2. At least 1 number between [0-9] => At least 1 digit
3. At least 1 letter between [A-Z] => At least 1 upper case letter
4. At least 1 of these characters: $,#,@
5. Length in the 6-12 range (including 6 and 12)
Passwords that match the criteria should be printed in one line separated by a comma.
"""

# def check_pass(password):
#     from string import ascii_lowercase
#     from string import ascii_uppercase
#
#     first = False
#     second = False
#     third = False
#     fourth = False
#     fifth = False
#
#     if (len(password) >= 6) and (len(password) <= 12):
#         fourth = True
#
#     for ch in password:
#         if ch in ascii_lowercase:
#             first = True
#         if ch in ascii_uppercase:
#             second = True
#         if ch.isnumeric():
#             third = True
#         if ch in '$#@':
#             fifth = True
#
#     return first and second and third and fourth and fifth

def password_check(passwords):
    pass_list = [p.lstrip() for p in passwords.split(',')]

    # Option 1: sa pomocnom funkcijom
    # output = ""
    # for p in pass_list:
    #     if check_pass(p):
    #         output += p + ', '
    # print(output.rstrip(', '))

    # Option 2: elegantnije
    valid_passwords = []
    for p in pass_list:
        validity = [False] * 5
        if any([ch.islower() for ch in p]): validity[0] = True
        if any([ch.isdigit() for ch in p]): validity[1] = True
        if any([ch.isupper() for ch in p]): validity[2] = True
        if any([ch in '$#@' for ch in p]): validity[3] = True
        if 6 <= len(p) <= 12: validity[4] = True
        if all(validity):
            valid_passwords.append(p)
    print(f"Valid passwords: {'. '.join(valid_passwords)}")


"""
TASK 6:
Write a function that receives a report (as a string) on the state (up / down) of several servers.
Each line of the report refers to one server, and has the following format:
"Server <server_name> is <up/down>"
Note that some lines may be empty.
The function should process the report and print:
- the total number of servers mentioned in the report
- the proportion of servers that are down
- names of servers that are down (if any)
"""

def server_status(report):
    s_down = []
    lines = [l.strip() for l in report.split('\n') if l.strip() != ""]
    for line in lines:
        server = line.split()
        # _, s_name, _, s_status = line.split(' ') elementi mogu i ovako
        if server[-1] == 'down':
            s_down.append(server[1])
    print(f'Total number of servers in report is: {len(lines)}.')
    print(f'Proportion of servers that are down is: {len(s_down)/len(lines)*100:.3f} %.')
    print(f'Servers that are down: {", ".join(s_down)}.')
    # obratiti paznju kada je izvestaj prazan ili na deljenje nulom

"""
TASK 7:
Write a function that finds numbers between 100 and 400 (both included)
where each digit of a number is even. The numbers that match this criterion
should be printed as a comma-separated sequence.
"""

# def numbers_with_all_even_digits():
#     all_even = list()
#     for num in range(100, 401):
#         if all([ch in '02468' for ch in str(num)]):
#             all_even.append(num)
#     print(", ".join([str(num) for num in all_even]))


# Option 2
def all_even_digits(num):
    while(num > 0):
        if (num % 10) % 2 != 0: return False
        num = num // 10
    return True

def numbers_with_all_even_digits():
    all_even = list()
    for num in range(100, 401):
        if all_even_digits(num): all_even.append(num)
    print(",".join([str(num) for num in all_even]))



if __name__ == '__main__':

    # Task 1:
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 5, 10]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(common_elements(a,b))
    #
    # # Task 2:
    # list1 = ["M", "na", "i", "Ke"]
    # list2 = ["y", "me", "s", "lly"]
    # print(concat_index_wise(list1, list2))
    #
    # # Task 3:
    # print("The quick brown fox jumps over the lazy dog")
    # print(pangram("The quick brown fox jumps over the lazy dog"))
    # print("The quick brown fox jumps over the lazy cat")
    # print(pangram("The quick brown fox jumps over the lazy cat"))
    #
    # Task 4:
    # print(("Rearranging string: 'PyNaTive_2021'"))
    # print(rearrange_string("PyNaTive_2021"))
    #
    # Task 5:
    # print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    # password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    #
    # Task 6:
    # sample_input = '''
    #     Server abc01 is up
    #     Server abc02 is down
    #     Server xyz01 is down
    #     Server xyz02 is up
    #     Server abd21 is down
    #     '''
    # server_status(sample_input)
    #
    # Task 7:


    numbers_with_all_even_digits()
