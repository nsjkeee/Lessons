#Reversed loop
def descending_order(num):
    direct = ""
    for n in reversed(str(num)):
        direct += n
    return int(direct)
