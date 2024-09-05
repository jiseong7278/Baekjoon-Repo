import math

def solution(arrayA, arrayB):
    answer = 0

    gc_a, gc_b= 0,0

    for i in range(len(arrayA)):
        gc_a = math.gcd(gc_a,arrayA[i])

    for i in range(len(arrayB)):
        gc_b = math.gcd(gc_b,arrayB[i])

    for j in range(len(arrayA)):
        if arrayA[j] % gc_b == 0:
            gc_b = 1
        if arrayB[j] % gc_a == 0:
            gc_a = 1

    if gc_a == 1 and gc_b ==1:
        return 0
    else:
        return max(gc_a, gc_b)
    
    return answer