import re



def solution(S,C):
    #print S.split(',')[2]
    names = S.split(', ')
    dlist = {}

    for p in names:
        P = p.split()
        last = P[len(P) - 1]
        first = P[0]
        middle = ''
        for i in range(len(P)):
            if i == 0 or i == len(P) - 1:
                continue
            middle += P[i]
        if len(last.split('-')) > 1:
            last = re.sub('\-', '', last)
        mail = last.lower() + '.' + first.lower()[0]
        if middle:
            mail = last.lower() + '.' + first.lower()[0] + '.' + middle.lower()[0]

        dlist.update({p: mail})
    revd = {}
    for key, value in dlist.items():
        revd.setdefault(value, set()).add(key)
    dic = []
    for i in range(len(revd.values())):
        if len(str(revd.values()[i])) > 1:
            dic.append(revd.keys()[i])
    #print len(dlist.values())
    #print dlist.keys()
    #print dlist
    for j in range(len(dic)):
        n = 1
        for i in range(len(dlist.values())):

            if dlist.values()[i] == dic[j]:
                k = dlist.keys()[i]
                v = dlist.values()[i]
                if n > 1:
                    v = v + str(n)
                v = v + '@' + C + '.com'
                dlist.update({ k : v })

                n = n + 1
    out = ''
    lib = len(dlist.values())
    for i in range(lib):
        if i != lib-1:
            out = out + dlist.keys()[i] + ' <' + dlist.values()[i] + '>, '
        else:
            out = out + dlist.keys()[i] + ' <' + dlist.values()[i] + '>'
    return out
    #print revd.keys()
    #print len(revd.values())
    #print len(revd.values()[0])
    #print dlist



S = 'John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker'
C = 'example'

solution(S,C)