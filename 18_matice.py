# matrix = [[0 for _ in range(10)] for _ in range(10)]

# matrix[1][2] = 1

# for row in matrix:
#   print(row)

# matrix = [0 for _ in range(10) for _ in range(10)]
# len(matrix)
# print("**************")
# matrix = [0 for _ in range(10) for _ in range(10)]
# len(matrix)

# jak pomoci while/else otestovat jeslti je nejake cislo prvocislo - znate prvocisla?
maybe_prime = 683 # OK
# maybe_prime = 684 # Neni

n = maybe_prime - 1

while n > 1:
  if (maybe_prime % n) == 0:
    print("Neni prvocislo")
    break
    
  n = n - 1
  print(n)
else:
  print(maybe_prime, "je prvocislo")
