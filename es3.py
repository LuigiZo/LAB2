#p = set([True, True, False, False])
#q = set([True, False, True, False])
#Point3

p = input("p: ")
q = input("q: ")

if(p.upper() == "TRUE"):
    p = True
else:
    p = False
if (q.upper() == "TRUE"):
    q = True
else:
    q = False

print(p,q)
print(not(p or q) == ((not p) and (not q)))
