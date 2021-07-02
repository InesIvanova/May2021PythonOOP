def print_row(size, star_count):
    for row in range(size - star_count):
        print(" ", end="")
    for row in range(1, star_count):
        print("*", end=" ")
    print("*")


size = int(input())
for star_count in range(1, size):
  print_row(size, star_count)
for star_count in range(size, 0, -1):
seco
