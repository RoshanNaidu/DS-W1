import streamlit as st
from apputil import *
import time

st.write('''# Week 1: [Palindrome and Parenthesis Balancer]''')

# A separator for an organized document
st.markdown("---")

st.write('''**Exercise 1: Palindrome Checker**''')

word = st.text_input("Palindrome Input to be checked: ")

if word: # If Else condition to check TRUE or FALSE
    with st.spinner('Checking palindrome sequence... 🕵️‍♂️'):
        time.sleep(3)  # To Simulate the processing time for UI appeal
    if palindrome(word):
        st.write(f"The input '{word}' is a palindrome 🎉")
    else:
        st.write(f"The input '{word}' is not a palindrome 😢")


# A separator for an organized document
st.markdown("---")

st.write('''**Exercise 2: Parentheses Balancer**''')

sequence = st.text_input("Enter a parentheses sequence: ")

if sequence: # If Else condition to check TRUE or FALSE
    with st.spinner('Balancing parentheses... ⚖️'):
        time.sleep(3)  # To Simulate the processing time for UI appeal
    if parentheses_balance(sequence):
        st.write(f"The parentheses sequence '{sequence}' is balanced ✅")
    else:
        st.write(f"The parentheses sequence '{sequence}' is not balanced ❌")