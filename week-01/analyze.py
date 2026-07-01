numbers = [12, 7, 23, 7, 42, 15, 8, 23, 7, 30]
words = ["Python", "ml", "python ", "Data", "ML", "data", "python", "AI"]

def number_stats(nums):
    number = len(nums)
    minimum = min(nums)
    maximum = max(nums)
    summa = sum(nums)
    average = summa / number
    print("Minimum number:", minimum, "Maximum number:", maximum)
    print(f"Average number: {average:.2f}")
    print("Sum of numbers:", summa)
    print("all numbers:", number)

number_stats(numbers)

def word_stats(words):
    new_words = [word.strip().lower() for word in words]
    counts = {}
    for word in new_words:
        counts[word] = counts.get(word, 0) + 1
    unique_words = set(new_words)
    most_common = max(counts, key=counts.get)

    print("Частоты:", counts)
    print("Уникальные слова:", unique_words)
    print("Самое частое слово:", most_common)

word_stats(words)

