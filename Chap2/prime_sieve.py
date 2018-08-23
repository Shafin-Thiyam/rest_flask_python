def Eratosthenes(upper_bound):
    prime = [True] * upper_bound     
    for p in range(3, upper_bound, 2):
        if p > (upper_bound**.5):
            break
        if prime[p]==True:
            for i in range(p * p, upper_bound, 2 * p):
                prime[i] = False
        return [2] + [p for p in range(3, upper_bound, 2) if    
            prime[p]]