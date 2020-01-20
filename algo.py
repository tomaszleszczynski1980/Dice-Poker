tab = [0, 1, 1, 0, 0, 1, 1]
n = len(tab)
l = 0
r = n - 1

while l < r:
    if tab[l] == 0:
        l += 1
    if tab[r] == 1:
        r -= 1
    if tab[l] == 1 and tab[r] == 0:
        tmp = tab[l]
        tab[l] = tab[r]
        tab[r] = tmp
        r -= 1
        l += 1

