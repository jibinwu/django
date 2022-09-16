# print(dir())
# ptye(__doc__)
# type(__name__)
# type(__package__)
# type(__file__)
# a=1
# print(type(__doc__))
# print(type(__name__))
# print(type(__package__))
# print(type(__file__))
'''
this is a doc
'''
import t
print(t.time.ctime())
print('name:'+__name__)
print('package:'+(__package__ or'nihao'))
print('doc:'+__doc__)
print('file:'+__file__)


