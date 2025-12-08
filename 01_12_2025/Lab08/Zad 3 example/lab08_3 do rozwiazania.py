# 8.3. Dla pliku dane.dat obliczyć sumaryczny czas ruchu,
# sumaryczną przebytą drogę oraz prędkość średnią.
results = []
with open("dane.dat", "r") as f:
    lines = f.readlines()[4:]
for line in lines:
    fields = line.split()
    time = float(fields[0])
    pos = float(fields[1])
    vel = float(fields[2])
    all = (time, pos, vel)
    results.append(all)
s, t, v = 0, 0, 0
for i in results:
    s += i[0]
    t += i[1]
v = s / t
print(s, t, v)
