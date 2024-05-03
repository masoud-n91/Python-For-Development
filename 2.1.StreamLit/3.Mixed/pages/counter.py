import streamlit as st

def show():
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        minus_btn = st.button("➖", type='primary')

    with col2:
        header_placeholder = st.empty()

    with col3:
        plus_btn = st.button("➕", type='primary')

    if minus_btn:
        st.session_state.counter -= 1

    if plus_btn:
        st.session_state.counter += 1

    header_placeholder.header(st.session_state.counter)


if __name__ == "__main__":
    show()

        