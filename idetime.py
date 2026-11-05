import time

input("Press enter to start")
start = time.time()

input("Press enter to stop")
end = time.time()

x = end - start

print(f"{int(x)} seconds")