Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={'a':10,'b':30,'c':50,'d':100}
>>> d['b']=300
>>> d
{'a': 10, 'b': 300, 'c': 50, 'd': 100}
>>> d.get()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 argument, got 0
>>> d['e']=600
>>> d
{'a': 10, 'b': 300, 'c': 50, 'd': 100, 'e': 600}
>>> d.values()
dict_values([10, 300, 50, 100, 600])
>>> x={'i':11,'j':12,'k':13,'l':14}
>>> d.update(x)
>>> d
{'a': 10, 'b': 300, 'c': 50, 'd': 100, 'e': 600, 'i': 11, 'j': 12, 'k': 13, 'l': 14}
>>> d.pop('j')
12
>>> d
{'a': 10, 'b': 300, 'c': 50, 'd': 100, 'e': 600, 'i': 11, 'k': 13, 'l': 14}
