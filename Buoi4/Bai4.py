n = int(input())
l = list(map(int, input().split()))
odd_cnt = 0
even_cnt = 0
for i in l:
    if i % 2 != 0:
        odd_cnt += i
    if i % 2 == 0:
        even_cnt += i
if odd_cnt == even_cnt:
    print('equal')
else:
    print('odd' if odd_cnt > even_cnt else 'even')
    