#Grouping the key-value pairs of a dictionary by the value with itemgetter :
from itertools import groupby
from operator import itemgetter
adict = {'a': 1, 'b': 5, 'c': 1}
print(dict((i, dict(v)) for i, v in groupby(adict.items(), itemgetter(1))))
#ans - {1: {'c': 1}, 5: {'b': 5}}
#using lamda function:
print(dict((i, dict(v)) for i, v in groupby(adict.items(), lambda x: x[1])))

#sorting a list of tuples by the second element ﬁrst the ﬁrst element as secondary:

alist_of_tuples = [(5,2), (1,3), (2,2)]
print(sorted(alist_of_tuples, key=itemgetter(1,0)))