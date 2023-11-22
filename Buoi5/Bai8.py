championLOL = ['Yasuo', 'Lee sin', 'Zed', 'Master Yi', 'Garen', 'Tryndamere']
dataLOL = [{'price':6300, 'Ulti':'Trăn trối'}, {'price':4800, 'Ulti':'Nộ long cước'},
           {'price':4800, 'Ulti':'Dấu ấn tử thần'}, {'price':450, 'Ulti':'Chiến binh sơn cước'},
           {'price':450, 'Ulti':'Công lí Demacia'}, {'price':1350, 'Ulti':'Từ chối tử thần'}]
d = {}
for i in range(6):
    d[championLOL[i]] = dataLOL[i]

championS = input()
if championS in d.keys():
    l = list(d[championS].items())
    print(l[0][1])
