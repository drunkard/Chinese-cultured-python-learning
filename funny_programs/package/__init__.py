# example of `import`

# print(f'\n__file__ = {__file__}')
var = '这是 package/__init__.py 里的变量 var'
print(f'这是 package/__init__.py 里的变量 __package__ = {__package__}')

from .mod2 import DAM
print('hahaha', DAM)
