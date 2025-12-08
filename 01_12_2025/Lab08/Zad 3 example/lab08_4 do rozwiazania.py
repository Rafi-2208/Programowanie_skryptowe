# 8.4. Dla pliku dane.dat obliczyć prędkość w danej chwili v=s/t
# i zapisać do pliku dane1.dat w miejscu prędkości zamiast 0.000000.
# Uwaga na dzielenie przez zero!

results = []
out = open("dane1.dat" , 'w')
with open("dane.dat", "r") as f:
    lines = f.readlines()
    coments = lines[:4]
    lines = lines[4:]
for line in lines:
    fields = line.split()
    time = float(fields[0])
    pos = float(fields[1])
    vel = float(fields[2])
    all = (time, pos, vel)
    results.append(all)
s, t, v = 0, 0, 0
for i in coments:
    out.write(i)

for i in results:
    s = i[0]
    t = i[1]
    v = s / t
    out.write(str(s) + " " + str(t) + " " + str(v) + '\n')
out.close()
