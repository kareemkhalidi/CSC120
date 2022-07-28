def read_file(fobj):

    infoList = []
    f = fobj.read().split("\n")

    for i in range(f.count('')):
        f.remove('')

    for i in range(int(len(f)/2)):
        s = f[i * 2].split()
        songId = int(s[1])
        info = ""
        for j in range(len(s) - 2):
            info += s[j + 2] + " "
        infoList.append((songId, info, f[(i * 2) + 1].split()))

    return(infoList)

def get_slices(data, n):

    returnList = []

    for i in range(len(data) - n + 1):
        tempList = []
        for j in range(n):
            tempList.append(data[i + j])
        returnList.append(tempList)

    return(returnList)

def compare_sets(a, b):

    return(len(a & b) / len(a | b))


def compare_melodies(m1, m2, n):

    sm1 = get_slices(m1, n)
    sm2 = get_slices(m2, n)

    for i in range(len(sm1)):
        sm1[i] = tuple(sm1[i])

    for i in range(len(sm2)):
        sm2[i] = tuple(sm2[i])

    sm1 = set(sm1)
    sm2 = set(sm2)
    
    return(compare_sets(sm1, sm2))