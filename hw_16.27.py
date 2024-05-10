def geo_progress(start, step):
    while True:
        yield start
        start *= step


gen = geo_progress(-2, -5)
for i in range(6):
    print(next(gen))

print("---"*20)

gen = geo_progress(10, 3)
for i in range(6):
    print(next(gen))
