# https://skillsmart.ru/algo/lvl1/gc8b.html

# boolean TransformTransform(int A[], int N)


def TransformTransform(A, N):
    return sum(transform(transform(A))) % 2 == 0


def transform(A):
    B = []
    for i in range(len(A)):
        for j in range(len(A) - i):
            k = i + j
            B.append(max(A[j:k+1]))
    return B
    
