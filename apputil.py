

# add code below ...

#Defining a function to remove spaces, punctuation and convert the letters to lowercase. Also to treat '0' as 'o'
def normalize(s):
    # Remove spaces and punctuation, convert to lowercase, and treat '0' as 'o'
    # loops through each alphanumeric character in 's', replacing 'o' or '0' with 'o', and converts other characters to lowercase. The result is joined into a newer string
    return ''.join(('o' if c.lower() in ['o', '0'] else c.lower()) for c in s if c.isalnum())

#Generate a function in Python for solving palindrome with attributes taken as words or sentences with spaces as well as punctuations
def palindrome(s):
    cleaned = normalize(s) # Normalize the input string
    # Check if the cleaned string is equal to its reverse
    reversed_str = cleaned[::-1]
    return cleaned == reversed_str # Check if the cleaned string is a palindrome or not

# Test cases that I tried
s1 = "No lemon, no mel0n"
print(palindrome(s1))

s2 = "Sit on a potato pan, 0tis"
print(palindrome(s2))



#Generate a function called parentheses with the attribute passing as sequence that takes a string and return 'TRUE' if the string's parentheses are balanced, 'FALSE' if they aren't
def parentheses_stack(sequence):
    stack = [] # Initialize empty stack
    for char in sequence: # Iterate through each character in sequence
        if char == '(': # If character is '('
            stack.append(char) # Push in the stack
        elif char == ')': # If the character is ')'
            if not stack: # If stack is empty
                return False # Unmatched closing parenthesis
            stack.pop() # Pop the matching opening parenthesis
    return not stack # If stack is empty, it means that the parentheses are balanced

# Another way to solve this problem with better space complexity
def parentheses_balance(sequence):
    balance = 0 # Initialize balance counter
    for char in sequence: # Iterate through each character in sequence
        if char == '(': # If character is '('
            balance += 1 # Increment balance
        elif char == ')': # If character is ')'
            balance -= 1 # Decrement balance
        if balance < 0: # If balance is negative
            return False # Then unmatched closing parenthesis
    return balance == 0 # If balance is zero, then it means that the parentheses are balanced

# Test cases that I tried
print(parentheses_balance("((blah)()()())"))
print(parentheses_balance("(((())blee))"))
print(parentheses_balance("(()hello((())()))"))
print(parentheses_balance("((((((())"))
print(parentheses_balance("()))"))

# The second implementation is better in terms of space complexity because it uses a single integer variable (balance) instead of a stack to keep track of the parentheses. This reduces the memory overhead, especially for long strings with many nested parentheses.
stri1 = "(((ABC)))"
stri2 = "((qc)"
stri3 = "()q)("

print(parentheses_balance(stri1))
print(parentheses_balance(stri2))
print(parentheses_balance(stri3))