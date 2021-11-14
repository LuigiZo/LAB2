#p = set([True, True, False, False])
#q = set([True, False, True, False])
#Point3
p = True
q = True
print(not(p or q) == ((not p) and (not q)))

p = True
q = False
print(not(p or q) == ((not p) and (not q)))

p = False
q = True
print(not(p or q) == ((not p) and (not q)))

p = False
q = False
print(not(p or q) == ((not p) and (not q)))


