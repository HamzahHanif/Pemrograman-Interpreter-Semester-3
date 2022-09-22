sum_a = 0
n = 0

for i in range(1, 101):
    sum_a = sum_a + i
    n += 1


#hitung rata rata
rata = sum_a / n

sum_b = 0 
for i in range(1,101):
    sum_b = sum_b + (i - rata)**2
    s = sum_b/(n-1)

print("Jumlah = " + str(sum_a))
print("Rata rata = " + str(rata))
print("s^2 = " + str(s))