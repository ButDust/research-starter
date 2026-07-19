#   
def list_stats(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    average_value = sum(numbers) / len(numbers)
    print("Lists:",numbers)
    print("Max:",max_value)
    print("Min",min_value)
    print("Average",average_value)

def count_characters(text):
    count = {}                         # Create an empty dictionary
    for char in text:                  # Iterate through each character in text
        if char in count:              # Check if char is a key in count, to prevent KeyError
            count[char] = count[char] + 1
        else:
            count[char] = 1            # Equivalent to creating a new key, where the key is char and the value is 1
    print("Original Text:",text)        
    print("Character Count:",count)

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def count_vowels(text):
    vowels = "aeiouAEIOU"               # Create a variable to store the string    
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count

def print_even_numbers():
    for number in range(1,101):
        if number % 2 == 0:
            print(number)

def sum_up():
    sum = 0
    number = 1
    while number <= 100:
        sum = sum + number
        number = number + 1 
    return sum

def remove_duplicates(items):
    duplicates_removed_items = set(items) 
    return duplicates_removed_items

def square_numbers(numbers):
    square = [number**2 for number in numbers]
    return square

def is_prime(n):
    if n <= 1 :
        return False
    for number in range(2,n):
        if n % number == 0:
            return False
    return True

def Fibonacci(n):
    if n <= 0 :
        return []
    if n == 1 :
        return [0]
    result = [0,1]
    while(len(result) < n):
        next_number = result[-1] + result[-2]
        result.append(next_number)
    return result 

if __name__ == "__main__":
    print("Exercise 1: list max, min, average")
    list_stats([88, 92, 75, 100, 67])
    print()

    print("Exercise 2: character frequency")
    count_characters("hello research")
    print()

    print("Exercise 3: is_even(n)")
    print("Is 10 even?", is_even(10))
    print("Is 7 even?", is_even(7))
    print()

    print("Exercise 4: count_vowels(text)")
    print("Number of vowels:", count_vowels("Hello Research"))
    print()

    print("Exercise 5: print even numbers from 1 to 100")
    print_even_numbers()
    print()

    print("Exercise 6: sum from 1 to 100 using while")
    result = sum_up()
    print("Sum:", result)

    print("Exercise 7: remove duplicates with set")
    numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
    print("Original:", numbers_with_duplicates)
    print("Unique:", remove_duplicates(numbers_with_duplicates))
    print()

    print("Exercise 8: list comprehension")
    numbers = [1, 2, 3, 4, 5]
    print("Numbers:", numbers)
    print("Squares:", square_numbers(numbers))
    print()

    print("Exercise 9: prime number check")
    print("Is 2 prime?", is_prime(2))
    print("Is 7 prime?", is_prime(7))
    print("Is 12 prime?", is_prime(12))
    print("Is 1 prime?", is_prime(1))
    print()

    print("Exercise 10: first n Fibonacci numbers")
    print("First 10 Fibonacci numbers:", Fibonacci(10))
    print("First 1 Fibonacci number:", Fibonacci(1))
    print("First 0 Fibonacci numbers:", Fibonacci(0))
    print()