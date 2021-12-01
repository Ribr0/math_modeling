a = int(input('Введите первую сторону:'))

b = int(input('Введите вторую сторону:'))

c = int(input('Введите третью сторону:'))

if c < (a + b) and a < (b + c) and b < (a + c):
  if a == b and b == c and a == c:
    print('Треугольник равносторонний')
  elif (a == b) != c and (a == c) != b and (b == c) != a:
    print('Треугольник равнобедренный')
  else:
    print('Треугольник разносторонний')
else:
  print('Треугольник невозможен')
