# prime.py

def prime_details(number):
    if number <= 1:
        result = f"Number: {number}\nNot Prime\n"
    else:
        for i in range(2, number):
            if number % i == 0:
                result = f"Number: {number}\nNot Prime\n"
                break
        else:
            result = f"Number: {number}\nPrime\n"

    return result


if __name__ == "__main__":
    number = 7
    print(prime_details(number))
