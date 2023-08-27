"""
Problem statement:
----------
You have been given an integer 'N'. Your task is to generate and return all binary strings of length 'N' such that there are no consecutive 1's in the string. A binary string is that string which contains only '0' and '1'.
Let 'N' = 3, hence the length of binary string would be 3. 
We can have the following binary strings with no consecutive 1s.
000, 001, 010, 100 101

"""


def gen(num, active, ls):
    if num == 0:
        ls.append(active)
        return
    if not active or active[-1] == '0':
        gen(num - 1, active + '1', ls)

    gen(num - 1, active + '0', ls)

    return ls


def generate_string(num):
    return gen(num, "", [])


if __name__ == '__main__':
    func = generate_string
    print(func(1))
    print(func(2))
    print(func(3))
    print(func(4))
