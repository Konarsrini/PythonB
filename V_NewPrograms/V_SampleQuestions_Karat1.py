#============================================================
'''
Problem: Following is a list of time, user name and some info in a list within a list. Get the row with
minimum and maximum unit of the first value'
'''
L1 = [
['300','user1','JLKHKJHKJJL'],
['301','user2','XYZP'],
['200','user2','POILKJHS'],
['900','user2','JHS'],
['100','user3','XYZPKJHS'],
['897','user1','XYPPOIJHS'],
['200','user8','ZPPOILKJH'],
['300','user2','XZPPOILJ']
]

def Get(lstL):
    x1 = lstL[0][0]
    for j in L1:
        if j[0] < x1:
            min = j[0]
            Lmin = [j]
        if j[0] > x1:
            max = j[0]
            Lmax = [j]
    print(f'Minimum: {Lmin} and Maximum: {Lmax}')
#===================================================================
Get(L1)
#Minimum: [['200', 'user8', 'ZPPOILKJH']] and Maximum: [['897', 'user1', 'XYPPOIJHS']]