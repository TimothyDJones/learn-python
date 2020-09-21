# fizzbuzz_sum.py

def fizzbuzz_sum(max):
	sum = 0
	for i in range(max):
		if (not (i % 3) or not (i % 5)):
			sum += i

	return sum

if __name__ == "__main__":
	print(fizzbuzz_sum(10))
	print(fizzbuzz_sum(100))
	print(fizzbuzz_sum(1000))
