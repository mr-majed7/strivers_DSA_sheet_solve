#https://www.codingninjas.com/studio/problems/sorted-array_6613259?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def sortedArray(a, b):
    pa = 0
    pb = 0
    merged = []
    while pa<len(a) and pb<len(b):
        if a[pa] < b[pb]:
            if len(merged) == 0 or merged[-1] !=a[pa]:
                merged.append(a[pa])
            pa +=1
        else:
            if len(merged) == 0 or merged[-1] !=b[pb]:
                merged.append(b[pb])
            pb +=1
                
    while pa<len(a):
        if merged[-1] !=a[pa]:
            merged.append(a[pa])
        pa +=1
    
    while pb<len(b):
        if merged[-1] !=b[pb]:
            merged.append(b[pb])
        pb +=1
    return merged