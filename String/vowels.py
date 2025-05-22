def recursion_vowels(n, i=0, res=''):
    if i >= len(n):
        return res
    if n[i] in 'AEIOUaeiou':
        res += n[i]
    return recursion_vowels(n, i + 1, res)

x = input("Enter the string: ")
print("Vowels in the string:", recursion_vowels(x))

