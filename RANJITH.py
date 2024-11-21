import streamlit as st
import random
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
def restart_game():
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
st.title("Number Guessing Game")
st.write("I have selected a random number between 1 and 100. Try to guess it!")
st.write(f"Attempts: {st.session_state.attempts}")
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess")
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.number_to_guess:
            st.write("Your guess is too low! Try again.")
        elif guess > st.session_state.number_to_guess:
            st.write("Your guess is too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True
if st.session_state.game_over:
    if st.button("Play Again"):
        restart_game()