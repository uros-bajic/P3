"""
LAB 4
"""
from functools import reduce

"""
TASK 1:
Write the 'compute_product' function that receives an arbitrary number of numeric values and computes their product. 
The function also receives a named argument "absolute" with the default value False, which 
determines if the numeric values should be used as given or their absolute value should be used instead.

Implement the function in two different ways:
1) using a for loop
2) using the reduce() f. from the functools module together with an appropriate lambda f.
For an example and explanation of reduce() f. check, for example, these articles:
- https://realpython.com/python-reduce-function/
- https://www.python-course.eu/python3_lambda.php
"""
from functools import reduce
def compute_product(*numbers, absolute = False):
    # p = 1
    # for num in numbers:
    #     p *= num if not absolute else abs(num)
    # return p

    return reduce(lambda a, b: a*b, [abs(num) if absolute else num for num in numbers])


"""
TASK 2:
Write the 'select_strings' function that receives an arbitrary number of strings and returns a list 
of those strings where the first and the last character are the same (case-insensitive) and the total 
number of unique characters is above the given threshold. The threshold is the function's named argument 
with the default value of 3.

Implement the function in three different ways:
1) using the for loop
2) using list comprehension
3) using the filter() f. together with an appropriate lambda f.
"""

def select_strings(*strings, threshold = 3):
    # selection = list()
    # for s in strings:
    #     if (s.lower()[0] == s.lower()[-1]) and (len(set(s))>3):
    #         selection.append(s)
    # return selection
    # return [s for s in strings if (s.lower()[0] == s.lower()[-1]) and (len(set(s))>3)]
    return list(filter(lambda s: (s.lower()[0] == s.lower()[-1]) and (len(set(s))>3), strings))


"""
TASK 3:
Write the 'process_product_orders' function that receives a list of product orders, 
where each order is a 4-tuple of the form (order_id, product_name, quantity, price_per_item). 
The function returns a list of 2-tuples of the form (order_id, total_price) where total price 
(in USD) for an order is the product of the quantity and the price per item (in USD).
The function also receives two named arguments that may affect the computed total price:
- discount - the discount, expressed in percentages, to be applied to the total price;
  the default value of this argument is None
- shipping - the shipping cost to be added to orders with total price less than 100 USD; 
  the default value of this argument is 10 (USD).

Implement the function in three different ways:
1) using the for loop
2) using list comprehension
3) using the map() f. together with an appropriate auxiliary function
"""
def process_product_orders(orders, discount = None, shipping = 10):
    def apply_discount(price):
        return price*(1-discount/100) if discount else price

    def process_order(order):
        order_id, _, quantity, price_per_item = order
        tot_price = quantity * apply_discount(price_per_item)
        return (order_id, tot_price) if tot_price >= 100 else (order_id, tot_price + shipping)

    # processed_orders = list()
    # for order_id, _, quantity, price_per_item in orders:
    #     tot_price = quantity * price_per_item if not discount else quantity * apply_discount(price_per_item)
    #     tot_price += shipping if tot_price < 100 else 0
    #     processed_orders.append((order_id, tot_price))
    # return  processed_orders

    # processed_orders = [(order_id, quantity*apply_discount(price_per_item))
    #                     for order_id, _, quantity, price_per_item in orders]
    #
    # return [(order_id, tot_price) if tot_price >= 100 else (order_id, tot_price+shipping)
    #         for order_id, tot_price in processed_orders]

    return list(map(process_order, orders))

"""
TASK 4:
Create a decorator ('timer') that measures the time a function takes to execute and 
prints the duration to the console.

Hint 1: use the decorator-writing pattern:
import functools
def decorator(func):
     @functools.wraps(func)	 # preserves func's identity after it's decorated
     def wrapper_decorator(*args, **kwargs):
         # Do something before
         value = func(*args, **kwargs)
         # Do something after
         return value
     return wrapper_decorator

Hint 2: to measure the time of function execution, use the perf_counter() f.
from the time module (it returns a float value representing time in seconds).
"""

import functools
from time import perf_counter

def timer(func):
    @functools.wraps(func) # preserves func's identity after it's decorated
    def wrapper_timer(*args, **kwargs):
        # Do something before
        start_time = perf_counter()
        value = func(*args, **kwargs)
        # Do something after
        duration = perf_counter() - start_time
        print(f"The execution time of function {func.__name__}: {duration} s")
        return value
    return wrapper_timer


"""
TASK 4.1
Write the 'compute_sum' function that for each number x in the range 1..n (n is the input parameter)
computes the sum: S(x) = 1 + 2 + ... + x-1 + x, and returns the sum of all S(x).
Decorate the function with the timer decorator.

Write the function in a few different ways - e.g. (1) using a loop; (2) using list comprehension;
(3) using the map f. - and decorate each one with the timer to compare their performance
"""

@timer
def compute_sum(n):
    s = 0
    for x in range(1, n+1):
        for i in range(1, x+1):
            s += i
    return s

@timer
def compute_sum_v2(n):
    return sum([sum(range(1, x+1)) for x in range(1, n+1)])

@timer
def compute_sum_v3(n):
    return sum(map(lambda x: sum(range(1, x+1)), range(1, n+1)))


"""
TASK 4.2
Write the 'mean_median_diff' function that creates a list by generating n random numbers (integers) 
between 1 and k (n and k are the function's input parameters). After generating and adding each number 
to the list, the function computes and prints the difference between mean and median of the list elements. 
Decorate the function with the timer decorator.

Bonus: assure that each function invocation produces the same results
"""
@timer
def mean_median_diff(n, k):
    from random import randint, seed
    from statistics import mean, median

    rand_list = list()
    seed(1)
    for i in range(n):
        num = randint(1, k)
        rand_list.append(num)
        print(f"After adding {num} to the list, mean-median is: {abs(mean(rand_list) - median(rand_list))}")


"""
TASK 5:
Create a decorator ('standardiser') that standardizes (= z-transforms) a list of numbers before passing 
the list to the decorated function for further computations. The decorator also rounds the computation 
result to 4 digits before returning it (as its return value).

Bonus: before calling the decorated function, print, to the console, its name with the list of input 
parameters (after standardisation)
"""


def standardiser(func):
    @functools.wraps(func)
    def wrapper_standardiser(*args, **kwargs):

        from statistics import mean, stdev
        m = mean(args)
        sd = stdev(args)
        stand_args = [(a-m)/sd for a in args]

        print(f"Executing function {func.__name__} with the following arguments:")
        print(f"{', '.join([str(a) for a in stand_args])}")
        print(f"{', '.join([name + '=' + str(val) for name, val in kwargs.items()])}")

        value = func(*stand_args, **kwargs)

        value = round(value, ndigits=4)

        return value

    return wrapper_standardiser


"""
TASK 5.1:
Write the 'sum_of_sums' function that receives an arbitrary number of int values and 
for each value (x) computes the following sum:
S(x) = 1 + x + x**2 + x**3 + ... + x**n
where n is a named argument with default value 10.
The function returns the sum of S(x) of all received int values.
Decorate the function with the standardise decorator.
"""

@standardiser
def sum_of_sums(*numbers, n=10):
    return sum(map(lambda x:sum([x**i for i in range(0, n+1)]), numbers))



if __name__ == '__main__':

    pass

    # Task 1
    # print(compute_product(1,-4,13,2))
    # print(compute_product(1, -4, 13, 2, absolute=True))
    # print()
    # # Calling the compute_product function with a list
    # num_list = [2, 7, -11, 9, 24, -3]
    # print(num_list)
    # print(*num_list)
    # print()
    # # This is NOT a way to make the call:
    # print("Calling the function by passing a list as the argument")
    # print(compute_product(num_list))
    # print()
    # # instead, this is how it should be done (the * operator is 'unpacking' the list):
    # print("Calling the function by passing an UNPACKED list as the argument")
    # print(compute_product(*num_list))
    # print()

    # kada funkcija kao argument ima neku sekvencu proizvoljnih dimenzija
    # ona se u pozivu uvek prosledjuje kao raspakovana

    # Task 2
    # str_list = ['yellowy', 'Bob', 'lovely', 'Yesterday', 'too']
    # print(select_strings(*str_list)) # raspakovali smo listu
    # print()

    # Task 3
    # orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
    #           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
    #           ("77226", "Head First Python, Paul Barry", 3, 32.95),
    #           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
    #
    # print(process_product_orders(orders))
    # print()
    # print("The same orders with discount of 10%")
    # print(process_product_orders(orders, discount=10))
    # print()

    # Task 4.1
    # print(compute_sum(10000))
    # print()
    # print(compute_sum_v2(10000))
    # print()
    # print(compute_sum_v3(10000))
    # print()

    # Task 4.2
    mean_median_diff(100, 250)
    print()

    # Task 5.1
    # print(sum_of_sums(1,3,5,7,9,11,13, n=7))


