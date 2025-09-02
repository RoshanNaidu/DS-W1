import streamlit as st

from apputil import *


st.write(
'''
# Week 1: [Palindrome and Parenthesis Balancer]

** Exercise 1: Palindrome Checker **

''')

word = st.text_input("Palindrome Input to be checked: ")

if word:
    if palindrome(word):
        st.write(f"The input '{word}' is a palindrome.")
    else:
        st.write(f"The input '{word}' is not a palindrome.")


st.write('''
**Exercise 2: Parentheses Balancer**
''')

sequence = st.text_input("Enter a parentheses sequence: ")

if sequence:
    if parentheses_balance(sequence):
        st.write(f"The parentheses sequence '{sequence}' is balanced!")
    else:
        st.write(f"The parentheses sequence '{sequence}' is not balanced.")