def vacation(N,happy_point): # Bài C 
    prev = [0] * 3 
    for i in range(N):
        a, b, c = happy_point[i]
        curr=[
        max(prev[1]+a,prev[2]+a),
        max(prev[0]+b,prev[2]+b),
        max(prev[0]+c,prev[1]+c)]
        prev = curr
    return max(prev)
