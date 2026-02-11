n = int(input())

if 2 <= n <= 10:

    arr = map(int, input().split())
    score = list(arr)

    # Check range
    for i in score:
        if not (-100 <= i <= 100):
            print("Not valid")
            exit()

    # Sort in descending order
    score.sort(reverse=True)

    # Find maximum
    k = max(score)

    # Count how many times max appears
    a = 0
    for i in score:
        if i == k:
            a += 1

    # If all elements are same
    if a == n:
        print(k)
    else:
        # Print runner-up
        print(score[a])
