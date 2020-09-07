TimeInSec = int(input("Введите время в секундах: "))
tis = int(TimeInSec)
h = TimeInSec // 3600
m = (TimeInSec - h * 3600) // 60
s = TimeInSec - (h * 3600 + m * 60)

print("{0} секунд = {1:02d}:{2:02d}:{3:02d}".format(TimeInSec, h, m, s))
print(f"{TimeInSec:d} секунд = {h:02d}:{m:02d}:{s:02d}")