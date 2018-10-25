def square_root(N):
  if N > 0: # The number must be greater than zero
    iter = 2 # number of iteration to calculate the square root
    x0 = 1
    # calculate the squarter number close to N (27)
    while x0*x0 <= N:
      x0 = x0 + 1
    x0 = x0 - 1
    # iteration to calculate the quarter root
    c = 0
    while c < iter:
      xi = (float)(pow(x0,2) + N)/(2*x0)
      x0 = xi
      c = c + 1
    return xi
  else:
    return 0  

#print(square_root(27))
