def palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = int(input("Enter a number: "))

if palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
