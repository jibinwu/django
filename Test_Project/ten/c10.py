import re
a='A8C3721D86'
def covert(value):
    print(value)

    match=value.group()
    print(match)
    if int(match) >= 6:
        return '9'
    else:
        return '0'


r=re.sub('\d',covert,a)
print(r)
