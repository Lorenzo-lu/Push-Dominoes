class Solution:
  def pushDominoes(self, dominoes: str) -> str:
    
    N = len(dominoes)
    left = [0]*N
    right = [0]*N
    i = 0
    while i <= (N-1):
        if dominoes[i] == 'R':
          #right[i] = 1
          right[i] = N
          j = 1
          while (i+j) <= (N-1):
            if dominoes[i+j] !='.':
              break
            #right[i+j] = 1/j
            right[i+j] = N-j
            j += 1
          i = i+j-1
        i += 1
    i = 0
    while i<= (N-1):
        if dominoes[N-i-1] == 'L':
          #left[N-i-1] = 1
          left[N-i-1] = N
          j = 1
          while (N-i-1-j) >= 0:
            if dominoes[N-i-1-j] !='.':
              break
            #left[N-i-1-j] = 1/j
            left[N-i-1-j] =N-j
            j += 1
          i = i+j-1
        i += 1
    out = ''
    for i in range(N):
      if left[i] > right[i]:
        out += 'L'
      elif left[i] == right[i]:
        out += '.'
      else:
        out += 'R'
    return (out)
