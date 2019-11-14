# print("------------------------------------------------------------------------------")
# print("##############################################################################")
# print("################################ Exercitiul 1 ################################")
# print("##############################################################################")
# print("------------------------------------------------------------------------------")
# a = [1,10,2,3,5,9,4,5]
# print("Lista initiala:")
# print(a)
# def max_tree_number(lists):
#     lists.sort(reverse=True)
#     return lists[0:3];

# print(max_tree_number(a))
# print("------------------------------------------------------------------------------")

# print("------------------------------------------------------------------------------")
# print("##############################################################################")
# print("################################ Exercitiul 2 ################################")
# print("##############################################################################")
# print("------------------------------------------------------------------------------")
# b = [1,3,4]
# print("Lista initiala:")
# print(b)
# def produsul(lists):
#     i = 1
#     for t in lists:
#         i *= t

#     return i;

# print(produsul(b))
# print("------------------------------------------------------------------------------")

# print("------------------------------------------------------------------------------")
# print("##############################################################################")
# print("################################ Exercitiul 3 ################################")
# print("##############################################################################")
# print("------------------------------------------------------------------------------")

# text = "This is Simple Text"
# print("Textul de la intrare:")
# print(text)
# def count_litter(text):
#     upper = 0
#     lower = 0
#     for char in text:
#         if char == " ":
#             continue

#         if char.isupper():
#             upper += 1
#         else:
#             lower += 1

#     return {"upper_case": upper, "lower_case": lower}

# print(count_litter(text))
# print("------------------------------------------------------------------------------")

# print("------------------------------------------------------------------------------")
# print("##############################################################################")
# print("################################ Exercitiul 4 ################################")
# print("##############################################################################")
# print("------------------------------------------------------------------------------")

# c = [1,2,1,1,2,2,4,4,5]
# print("Lista initiala:")
# print(c)

# def distincte(lists):
#     output = set(lists)
#     output = list(output)
#     # output = []
#     # for i in lists:
#     #     if i in output:
#     #         continue

#     #     output.append(i)

#     return output

# print("Lista primita:")
# print(distincte(c))
# print("------------------------------------------------------------------------------")


############################################## Lesson ##############################################
## Scope
# a = 10
# b = 20

# def double():
#     # print(a)
#     a = 5

# print(double())

# a = [1, 2, 3]

# def my_list(l):
#     l[0] = 33

# my_list(a)
# print(a)


# a = 1

# def my_list2(n):
#     n += 1
#     # print(n)

# my_list2(a)
# print(a)

## Functions, *args

# def my_function(a, *args):
#     print(a)
#     print(args)

# my_function(1,2,3,4,5,6,7,8)
# my_function(1,1)

# def multiply_list(*args):
#     test = list(args)

#     print(test)

# multiply_list(1, "Testare")

## Functions, **kwargs

# def myFunction(x, **kwargs):
#     print(x)
#     print(kwargs)

# myFunction(10, a = 10, b = 20, y = 30)
# myFunction(12, c = 10, d = 20, w = 30, i = 200)
# myFunction(12, **{'g':11, 'l':22, 'k':33})



def my_func(a, b = 10, *args, **kwargs):
    print(a, b, args, kwargs)


# my_func()                         # - Eroare
my_func(1)                          # - Va functiona
my_func(1, 20)                      # - Va functiona
my_func(1, 20, 11,22,33)            # - Va functiona
my_func(1, 20, 11,22,33, **{'f':5}) # - Va functiona
    