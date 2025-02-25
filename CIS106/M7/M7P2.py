start = int(input('Enter the start value: '))
stop = int(input('Enter the stop value: '))
increment = int(input('Enter the increment value: '))
count = 0
print(start)
while count < stop:
  count = start + increment
  increment = increment + 1
  print(count)
