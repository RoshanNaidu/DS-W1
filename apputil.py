

# add code below ...
#Generate a function in Python for solving palindrome with attributes taken as words or sentences with spaces as well as punctuations.

#Defining a function to remove spaces, punctuation and convert the letters to lowercase. Also to treat '0' as 'o'
def normalize(s):
    # Remove spaces and punctuation, convert to lowercase, and treat '0' as 'o'
    return ''.join(('o' if c.lower() in ['o', '0'] else c.lower()) for c in s if c.isalnum())

def palindrome(s):
    cleaned = normalize(s)
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    reversed_str = cleaned[::-1]
    return cleaned == reversed_str

s = "A man, a plan, a canal: Panama"
print(palindrome(s))

s1 = "Nurses run"
print(palindrome(s1))

s2 = "N0 lem0n, n0 mel0n"
print(palindrome(s2))
# The issue is that in is_palindrome, you are re-cleaning s instead of using the normalized version.
# Let's fix is_palindrome to use the cleaned string from normalize(s):

def palindrome(s):
    cleaned = normalize(s)
    # Check if the cleaned string is equal to its reverse
    reversed_str = cleaned[::-1]
    return cleaned == reversed_str

s3 = "No lemon, no mel0n"
print(palindrome(s3))

s4 = "Sit on a potato pan, 0tis"
print(palindrome(s4))


#Generate a function called parentheses with the attribute passing as sequence that takes a string and return 'True' if the string's parentheses are balanced, False if they aren't
def parentheses_stack(sequence):
    stack = []
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

#Generate another way to solve this problem with better time or space complexity
def parentheses_balance(sequence):
    balance = 0
    for char in sequence:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

# Test cases
print(parentheses_balance("((blah)()()())"))      # True
print(parentheses_balance("(((())blee))"))        # True
print(parentheses_balance("(()hello((())()))"))   # True
print(parentheses_balance("((((((())"))           # False
print(parentheses_balance("()))"))                # False

# The second implementation is better in terms of space complexity because it uses a single integer variable (balance) instead of a stack to keep track of the parentheses. This reduces the memory overhead, especially for long strings with many nested parentheses.
stri1 = "(((ABC)))"
stri2 = "((qc)"
stri3 = "()q)("

print(parentheses_balance(stri1))  # False
print(parentheses_balance(stri2))  # False
print(parentheses_balance(stri3))  # False