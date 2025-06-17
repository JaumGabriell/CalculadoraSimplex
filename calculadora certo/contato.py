import streamlit as st
from calculospulp import load_lottieurl

def contato():
    st.title("Nos contate")
    st.write("Qualquer duvida só nos chamar.")
    with st.container():
        st.write("---")
        st.header("Contato:")
        st.write("##")
        st.markdown(
            """
            <style>
            input[type="text"], input[type="email"], textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            margin-top: 6px;
            margin-bottom: 16px;
            resize: vertical;
            }
            button[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            }
            button[type="submit"]:hover {
            background-color: #45a049;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        contact_form = """
        <form action="https://formsubmit.co/contasecundariaminha123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Seu nome" required>
        <input type="email" name="email" placeholder="Seu email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()