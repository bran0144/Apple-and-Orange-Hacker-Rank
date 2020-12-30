# Completed python code to solve Hackerrank Apple and Orange

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_num = 0
    orange_num = 0
    for apple in apples:
        if apple + a >= s and apple + a <= t:
            apple_num += 1
    for orange in oranges:
        if orange + b >= s and orange  + b <= t:
            orange_num += 1
    print(apple_num)
    print(orange_num)