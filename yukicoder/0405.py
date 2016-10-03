s,t = input().split()
t = (int(t)+1200)%12
r = ["I","II","III","IIII","V","VI","VII","VIII","IX","X","XI","XII"]
print(r[(r.index(s)+t)%12])