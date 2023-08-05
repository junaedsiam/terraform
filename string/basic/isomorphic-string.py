"""
Problem description: 
---------
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself. 

------
You must understand the this question needs us to check if there is one directional map exist between given string and a pattern. In the given question, we can treat 's' as given string and 't' as pattern. So, essentially, we have to check if there is a one-directional map exist from 's' to 't'.
Whatever character is there in 's' is not same as in 't'. For instance, s = 'PAPER', t = 'TITLE'. If we can see, character 'E' is common between string 's' and pattern 't'. Character 'E' from string 's' is mapped to character 'L' in pattern 't'. Meanwhile, character 'E' in the pattern 't' is being mapped to character 'R' from string 's'.

string (s)	pattern (t)
P	T
A	I
E	L
R	E
So, as long as, character from string 's', have only one map towards character in pattern 't', the strings are isomorphic.
--------

Example 1:
---------
Input: s = "badc", t = "baba"
{ b: b , a: a , d: b (X) , c: a (X) }
Output: false

Example 2:
----------
Input: s = "foo", t = "bar"
{ f: b , o: a, o: r (X) } 
Output: false

Example 3:
----------
Input: s = "paer", t = "tile"
{ p : t , a : i , e: l, r: e }
Output: true
 
Constraints:
-------------
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""


def isomorphic_string(s1, s2):
    # Time complexity:
    # both strings must be at same length to be isomorphic
    n = len(s1)
    m = len(s2)
    if n != m:
        return False
    ht = {}
    visited = {}
    for i in range(n):
        if s1[i] not in ht:
            if s2[i] not in visited:
                ht[s1[i]] = s2[i]
                visited[s2[i]] = True
            else:
                return False
        elif ht[s1[i]] != s2[i]:
            return False

    return True


if __name__ == '__main__':
    ex_1, ex_2, ex_3 = ("badc", "baba"), ("foo", "bar"), ("paer", "tile")
    print(isomorphic_string(ex_1[0], ex_1[1]))
    print(isomorphic_string(ex_2[0], ex_2[1]))
    print(isomorphic_string(ex_3[0], ex_3[1]))
