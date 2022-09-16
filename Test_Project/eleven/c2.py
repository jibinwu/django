from enum   import Enum,unique
@unique
class VIP(Enum):
    YELLOW=1
    # YELLOW=6
    GREEN=2
    BLACK=3
    RED=4

# print(type(VIP.GREEN))
# print(VIP.GREEN.value)
# print(type(VIP.GREEN.name))
# print(VIP['YELLOW'])
# # for i in VIP:
# #     print(i)
# # VIP.GREEN=3
# print(VIP.GREEN.value)
# # print(VIP.__name__)
# print(dir())
print(VIP(1))
