import streamlit as st

def main():
    st.title("Echo Bot")
    if q := st.text_input("You:"):
        st.write("Bot:", q)

if __name__ == "__main__":
    main()
