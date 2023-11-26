from math import *
#round
x = 1.55
y = -1.55

print(round(x))
# 2
print(round(y))
# -2

# the second argument gives how many decimal places to round to (defaults to 0)here 1.55 '55 to 6''
round(x, 1)
# 1.6
round(y, 1)
# -1.6

floor(x) # 1
floor(y) # -2

ceil(x)
# 2
ceil(y)
# -1

trunc(x) # 1, equivalent to math.floor for positive numbers
trunc(y) # -1, equivalent to math.ceil for negative numbers

floor(-1.7) #ans ---2.0

pow(5,5) #3125.0

import math
pos_inf = math.inf
neg_inf = -math.inf
not_a_num = math.nan

math.isfinite(pos_inf)
# Out: False
math.isfinite(0.0)
#true