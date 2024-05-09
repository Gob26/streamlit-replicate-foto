import streamlit as st


st.markdown("# :rainbow[AI II Image]")


def configure_sitebar():
    with st.sidebar:
        with st.form('my form'):
            width = st.number_input('Ширина изображения')
            height = st.number_input('Высота изображения')
            submitted = st.form_submit_button("Создать", type="primary")
def main():
    configure_sitebar()


if __name__=="__main__":
    main()