Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='anjan'
b=20
c=BE-CSE
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c=BE-CSE
NameError: name 'BE' is not defined
C='BE-CSE'
d=('2 year's of experiance')
   
SyntaxError: unterminated string literal (detected at line 1)
d='two year,s'
   
print(a,b,c,d)
   
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a,b,c,d)
NameError: name 'c' is not defined. Did you mean: 'C'?
print(a,b,C,d)
   
anjan 20 BE-CSE two year,s
