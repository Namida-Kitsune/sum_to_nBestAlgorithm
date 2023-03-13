def sum_to_n(n):
    return n*(n+1)//2
if __name__ == "__main__":
    try:
        n = int(input("Input : "))
        print("Answer",sum_to_n(n))
    except:
        print("Failed")
