import string
alphabet = list(string.ascii_uppercase)


# Cyclic implementation
def gen_subsets_C(my_list):
    subsets = [[]]
    for item in my_list:
        new_part_with_item = [subset + [item] for subset in subsets]
        subsets = subsets + new_part_with_item
    return subsets


# Recursive implementation
def gen_subsets_R(my_list):
    if len(my_list) == 0:
        return [[]]
    part_without_item = gen_subsets_R(my_list[:-1])
    item = my_list[-1]
    new_part_with_item = [subset + [item] for subset in part_without_item]
    return part_without_item + new_part_with_item


for i in range(len(alphabet)+1):
    subsets = gen_subsets_C(alphabet[:i])
    print(subsets)
    print(i, '->', len(subsets))
    input()
