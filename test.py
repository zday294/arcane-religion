#test.py

from ctypes import cdll

lib = cdll.LoadLibrary('./arclib.so')

avg = lib.calcAvgAttempts(96, 30)

print(f"AVG: {avg}")

rolls = lib.performSimulations(30, 10, 20)

print(f"Rolls: {rolls}")

basic = lib.basicIf(51)
basic2 = lib.basicIf(10)

print(f"Basic: {basic}")
print(f"Basic 2: {basic2}")

fail = lib.fail()

print(f"Fail: {fail}")

print("Done")