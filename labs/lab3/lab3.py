"""
LAB 3
"""
from operator import  itemgetter
from collections import defaultdict, Counter

"""
TASK 1:
Write a function that receives an integer value (n) and generates  
a dictionary with entries in the form x: (1 + 2 + ... + x), 
where x is a number between 1 and n.
The function also prints the dictionary in the decreasing value 
of the key, in the following way (for n=5):
5: 1+2+3+4+5=15
4: 1+2+3+4=10
3: 1+2+3=6
2: 1+2=3
1: 1=1
"""

def create_print_numeric_dict(n):
    d = dict()
    for x in range(1, n+1):
        d[x] = sum(range(1, x+1))
    for key, val in sorted(d.items(), reverse= True, key = lambda item: item[1]):
        print(f"{key}: {'+'.join([str(i) for i in range(1, key+1)])}={val}")
        # print(f'{key}: {"+".join([str(i) for i in range(1, key + 1)])}={val}')

"""
TASK 2:
Write a function that creates a dictionary from the two given lists, so that
elements of the 1st list are keys, while the corresponding elements of the 
2nd list are values. 
Print the dictionary sorted based on the element values.
(hint: use itemgetter() f. from the operator module)

Example: a list of countries and a list of the countries' national dishes
should be turned into a dictionary where keys are country names and values
are the corresponding dishes.
"""

def lists_to_dict(l1, l2):
    d = dict()
    for item1, item2 in zip(l1, l2):
        d[item1] = item2
    for key, val in sorted(d.items(), key=itemgetter(1)):
        print(f"{key}: {val}")

"""
TASK 3:
Write a function that receives a string as its input parameter, and
calculates the number of digits, letters, and punctuation marks (.,!?;:)
in this string.
The function returns a dictionary with the computed values.
"""

def string_stats(string):
    # default dict, unapred se definise tip vrednosti kljuceva
    # d = {'digits':0, 'letters':0, 'pmarks':0}
    d = defaultdict(int) # tip svih vrednosti ce biti int

    for ch in string:
        if ch.isdigit(): d['digits'] += 1
        elif ch.isalpha(): d['letters'] += 1
        elif ch in '.,!?;:': d['pmarks'] +=1
    return dict(d)


"""
TASK 4:
Write a function that receives a list of web addresses (= website names) of various organisations.
Compute the number of addresses for each suffix (e.g., com, org, net) encountered in the list.
Create and return a dictionary of thus computed values (keys are website suffixes, values are
the corresponding counts)
"""

def website_stats(website_names):
    d = defaultdict(int)
    for name in website_names:
        _, suffix = name.rsplit('.', maxsplit=1) # splituj po tacki sa desne strane i to samo jednom
        suffix = suffix.rstrip('/')
        d[suffix] +=1
    return dict(d)

    # varijacija kada su vrednosti liste
    # d = defaultdict(list)
    # for name in website_names:
    #     rest, suffix = name.rsplit('.', maxsplit=1) # splituj po tacki sa desne strane i to samo jednom
    #     suffix = suffix.rstrip('/')
    #     d[suffix].append(rest)
    # return dict(d)

"""
# TASK 5:
Write a function that receives a piece of text and computes the frequency of tokens 
appearing in the text (consider that a token is a string of contiguous characters between two spaces). 
Compute token frequency in case-insensitive manner (do not consider the difference between upper and 
lowercase letters).
Tokens and their frequencies should be stored in a dictionary. 
The function prints tokens and their frequencies after sorting the tokens alphanumerically.

After testing the function, alter it so that:
- tokens are cleared of any excessive characters (e.g. spaces or punctuation marks)
before being added to the dictionary
- only tokens with at least 3 characters are added to the dictionary
- before being printed, the dictionary entries are sorted: 
    i) in the decreasing order of the tokens' frequencies, and then 
    ii) in increasing alphabetical order.
"""

# auxiliary function for sorting option 2 (see lines 128-130)
def custom_key(dict_item):
    pass

def token_frequency(text):
    # d = defaultdict(int)
    # for token in [token.rstrip('.,?!;:') for token in text.split() if (len(token) >= 3)]:
    #     if len(token) >= 3: d[token] += 1
    # for token, freq in sorted(sorted(d.items(), key=itemgetter(0), reverse=False), key=itemgetter(1), reverse=True):
    #     print(f"{token}: {freq}")
    tokens = [token.rstrip('.,?!;:') for token in text.split() if (len(token.rstrip('.,?!;:')) >= 3)]
    c = Counter(tokens)
    for token, freq in sorted(sorted(c.items(), key=itemgetter(0), reverse=False), key=itemgetter(1), reverse=True):
        print(f"{token}: {freq}")

"""
TASK 6:
Write a function that accepts a sequence of comma separated passwords and
checks their validity using the following criteria:
1. At least 1 letter between [a-z] => At least 1 lower case letter
2. At least 1 number between [0-9] => At least 1 digit
3. At least 1 letter between [A-Z] => At least 1 upper case letter
4. At least 1 of these characters: $,#,@
5. Length in the 6-12 range (including 6 and 12)
The function creates and returns a dictionary with checked passwords as keys, 
whereas the value of a key would be:
- the word "valid" if the corresponding password proved to be valid
- list of identified issues, if the corresponding password is not vlaid 
"""

def password_check(passwords):

    passwords = [p.strip() for p in passwords.split(',')]
    print(passwords)
    d = dict()
    for p in passwords:
        validity = [False] * 5
        errors = []

        one_lowercase = any([ch.islower() for ch in p])
        one_digit = any([ch.isdigit() for ch in p])
        one_upper = any([ch.isupper() for ch in p])
        special = any([ch in '$#@' for ch in p])
        length = 6 <= len(p) <= 12

        if one_lowercase: validity[0] = True
        if not one_lowercase: errors.append('Nema bar 1 malo slovo.')
        if one_digit: validity[1] = True
        if not one_digit: errors.append('Nema bar 1 cifru.')
        if one_upper: validity[2] = True
        if not one_upper: errors.append('Nema bar 1 veliko.')
        if special: validity[3] = True
        if not special: errors.append('Nema \'$#@\' karakter.')
        if length: validity[4] = True
        if not length: errors.append('Duzina nije [6, 12] karaktera.')

        if all(validity):
            d[p] = ['valid']
        else:
            d[p] = errors
    return d

"""
TASK 7:
Write a function that prompts the user for name, age, and competition score (0-100) of members of a sports team. 
All data items for one member should be entered in a single line, separated by a comma (e.g. Bob, 19, 55). 
The entry stops when the user enters 'done'.
The function stores the data for each team member as a dictionary, such as
{name:Bob, age:19, score:55}
where name is string, age is integer, and score is a real value.
The data for all team members should form a list of dictionaries.
The function prints this list sorted by the members' scores (from highest to lowest) and
then returns the list as its return value.
"""

def collect_team_data():
    members = list()
    print("""
                Please enter team members data in the following order:
                name, age, score
                Enter 'done' to finish the task.
            """)
    done = False
    while not done:
        user_input = input("Enter data for next team member:\n")
        if user_input.lower() == 'done':
            done = True  # moglo i break umesto done uslova
            continue
        parts = user_input.split(',')
        if len(parts) != 3:
            print("Wrong input! Please see instructions and try again.")
            continue
        name, age, score = parts
        members.append({'name': name, 'age': int(age), 'score': float(score)})

    for member in sorted(members, reverse=True, key=itemgetter('score')):
        # umesto itemgettera key = lambda m: m['score']
        print(f"{member['name']}, {member['age']} years old, scored {member['score']} ponts.")
    return members

"""
TASK 8:
Write a function that takes as its input the list of dictionaries created by the previous
function and computes and prints the following statistics:
- the average (mean) age of the team members
- median, first and third quartile for the team's score
- name of the player with the highest score among those under 21 years of age

Hint: the 'statistics' module provides functions for the required computations
"""

def team_stats(team_members):
    from statistics import mean, quantiles
    scores = [member['score'] for member in team_members]
    m = mean(scores)
    q1, mdn, q3 = quantiles(scores, n=4)
    best_under21 = max([member for member in team_members if member['age']< 21], key=itemgetter('score'))
    print(f"Mean score value: {m:.2f}")
    print(f"Mdn(Q1,Q3) = {mdn}({q1:.3f}:{q3:.3f})")
    print(f"Best team member under 21: {best_under21['name']}")



"""
TASK 9:
Write a function to count the total number of students per class. The function receives
a list of tuples of the form (<class>,<stud_count>). For example:
[('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
The function creates a dictionary of classes and their student numbers; it then
prints the classes and their sizes in the decreasing order of the class size.

After testing the function, try writing it using the Counter class from
the collections module.
"""

def classroom_stats(class_data):
    classes = []
    for c in class_data:
        for el in [c[0]]*c[1]:
            classes.append(el)
    print(classes)
    c = Counter(classes)
    for key, value in sorted(c.items(), reverse=True, key=itemgetter(1)):
        print(f"{key}: {value}")

if __name__ == '__main__':

    # # Task 1
    # create_print_numeric_dict(7)
    # print()
    #
    # # Task 2
    # dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    # countries = ["Italy", "Germany", "Spain", "USA", "Serbia"]
    # lists_to_dict(countries, dishes)
    # print()
    #
    # # Task 3
    # print("string_stats('Today is November 5, 2021!'):")
    # print(string_stats("Today is November 5, 2021!"))
    # print()
    #
    # Task 4
    # sample_websites = ['https://www.technologyreview.com/', 'https://www.tidymodels.org/',
    #                    'https://podcasts.google.com/', 'https://www.jamovi.org/', 'http://bg.ac.rs/']
    #
    # print(website_stats(sample_websites))
    # print()
    #
    # Task 5
    # response by GPT-3 to the question why it has so entranced the tech community
    # source: https://www.wired.com/story/ai-text-generator-gpt-3-learning-language-fitfully/
    # gpt3_response = ("""
    #     I spoke with a very special person whose name is not relevant at this time,
    #     and what they told me was that my framework was perfect. If I remember correctly,
    #     they said it was like releasing a tiger into the world.
    # """)
    # token_frequency(gpt3_response)
    # print()
    #
    # Task 6:
    # print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    # validation_dict = password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR")
    # print("Validation results:")
    # for password, result in validation_dict.items():
    #     print(f"- {password}: {', '.join(result)}")
    # print()
    #
    # # Task 7:
    # team = collect_team_data()
    # print()
    #
    # # Task 8:
    # team = [{'name': 'Bob', 'age': 18, 'score': 50.0},
    #         {'name': 'Tim', 'age': 17, 'score': 84.0},
    #         {'name': 'Jim', 'age': 22, 'score': 94.0},
    #         {'name': 'Joe', 'age': 19, 'score': 85.5}]
    # team_stats(team)
    # print()
    #
    # Task 9:
    l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
    classroom_stats(l)