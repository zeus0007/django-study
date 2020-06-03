1 == '1'

(1 == 1) and (1 != 1)

if 1 < 2:
    print('First Block')
    if 20 > 3:
        print("True!")
    elif 3 == 3:
        print('elif ran')
    else:
        print('False!')

# For Loops

    # list loops
    seq = [1, 2, 3, 4, 5, 6]

    for item in seq:
        # Code here
        print(item)

    # dictionary loops
    d = {"Sam": 1, "Frank": 2, "Dan": 3}

    for item in d:
        print(item)  # 순서없이 가져오게 된다.
        print(d[item])
    # tuple loops
    mypairs = [(1, 2), (3, 4), (5, 6)]

    for item in mypairs:
        print(item)
    for tup1, tup2 in mypairs:
        print(tup2)
        print(tup1)
# while loops
i = 1

while i < 5:
    print(f"i is: {i}")
    i = i + 1

# range
range(5)
print(range(0, 5))
list(range(0, 5))
list(range(0, 20, 2))

for item in range(10):
    print(item)

# List Comprehesion
x = [1, 2, 3, 4]

out = []
for num in x:
    out.append(num**2)
print(out)

result = [num**2 for num in x]
print(result)
