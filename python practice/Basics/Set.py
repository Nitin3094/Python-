Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={1,2,3,4,5}
>>> b={3,4,5,6,7,8,9}
>>> a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a&b
{3, 4, 5}
>>> a.add(6)
>>> a
{1, 2, 3, 4, 5, 6}
>>> a-b
{1, 2}
