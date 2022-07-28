def main():
    fact = 1
    num = int(input("Enter the Number :"))
    try:
        for i in range(1,num+1):
            fact = fact*i
        print(f"Factorial of {num} is {fact}")
    except Exception as e:
        print("Error Occurred to find the Factorial")


if __name__ == '__main__':
    main()