n = int(input())

mmin = [1990, 1, 1]
mmax = [2010, 12, 31]

youngest, oldest = "", ""
for i in range(n):
    name, day, month, year = input().split()
    day, month, year = int(day), int(month), int(year)
    if (year > mmin[0]) or (year >= mmin[0] and month > mmin[1]) or (year >= mmin[0] and month >= mmin[1] and day > mmin[2]):
        youngest = name
        mmin = [year, month, day]
    if (year < mmax[0]) or (year <= mmax[0] and month < mmax[1]) or (year <= mmax[0] and month <= mmax[1] and day < mmax[2]):
        oldest = name
        mmax = [year, month, day]
print(youngest, oldest)