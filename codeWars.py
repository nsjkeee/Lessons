#Reversed loop
def descending_order(num):
    direct = ""
    for n in reversed(str(num)):
        direct += n
    return int(direct)


#Switch alternative
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

=============================
#Filter all list
def array_diff(a, b):
    return [x for x in a if x not in b]

#here another example 
# squares = [x**2 for x in range(10)]
=
=============================
# Calculate summ of all numbers n = 3 (1,2,3) that is % 2 == 0
def solution(number):
    return sum(x for x in range(number) if x % 2 == 0)

=============================
#Calculate all unique uppercase
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
