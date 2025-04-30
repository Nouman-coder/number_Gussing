import streamlit as st

st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")
st.title("🎮 Number Guessing Game")


secret_number = 7


guess = st.number_input("Guess a number between 1 and 10:", min_value=1, max_value=10, step=1)


if st.button("Check Guess"):
    if guess == secret_number:
        st.success(f"🎉 Right! You guessed the number {guess}.")
    elif guess > secret_number:
        st.warning("❌ Too high! Try a smaller number.")
    else:
        st.warning("❌ Too low! Try a bigger number.")
