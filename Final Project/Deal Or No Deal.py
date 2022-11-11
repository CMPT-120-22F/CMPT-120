import random

def average(list):
    sum = 0
    for x in range(0, list.len() - 1):
        print(x)
        sum = sum + list[x]

    avg = sum / list.len()
    print(avg)

def main():
    cases = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000,
             10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000,
             750000, 1000000]

    dealOffered = average(cases)
    print(dealOffered)
    print("Hello")
