'''Define basic bone'''

from random import shuffle

LEFTTILES = [
'''
 -------
|
|
|
 -------
''',
'''
 -------
|
|   o   
|
 -------
''',
'''
''',
'''
''',
'''
''',
'''
'''
]

class Bone:
    '''
    A bone has two values, left and right
      1-6, or 0 for blank

    A bone can display itself
    '''

    def __init__(self, left='', right=''):
    	'''left and right values will always be passed'''
    	'''in, but wewill add validation for manual testing'''

    	while int(left) not in list(range(7)):
    		left = input("Enter a left value: (0-6) ")
    	while int(right) not in list(range(7)):
    		right = input("Enter a right value: (0-6) ")

    	# order by largest on left
    	if left >= right:
    		self.left = left
    		self.right = right
    	else:
    		self.left = right
    		self.right = left

    def display(self, order=0):
    	'''display a bone'''
    	'''order is optional. default 0 is random ordering'''
    	'''of left and right. order=1 displays highest value on left'''

    	display_order = [self.left, self.right]
    	if order==0:
    		shuffle(display_order)
    		
    	print("{} | {}".format(*display_order), end="  ")

