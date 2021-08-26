def distance_sum(coordinates):
    arr = sorted(coordinates)
    
    res = 0
    sum_ = 0
    
    for i in range(len(arr)):
        res += (arr[i] * i - sum_)
        sum_ += arr[i]
    
    return res

if __name__ == "__main__":
    N = int(input())
    
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    
    rp = [p[i]+q[i] for i in range(N)]
    rq = [q[i]-p[i] for i in range(N)]
    
    manhattan_sum = distance_sum(p) + distance_sum(q)
    chebyshev_sum = distance_sum(rp) + distance_sum(rq)
    
    print(2 * manhattan_sum - chebyshev_sum)