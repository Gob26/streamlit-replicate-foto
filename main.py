import streamlit as st


st.markdown("# :rainbow[AI II Image]")


def configure_sitebar():
    with st.sidebar:
        with st.form('my form'):
            width = st.number_input('Ширина изображения', min_value=256, max_value=2048,value=1024, step=16)
            height = st.number_input('Высота изображения',min_value=256, max_value=2048,value=1024, step=16)
            promt = st.text_area('Введите ПРОМТ для создания изображения')
            submitted = st.form_submit_button("Создать", type="primary")

        return {
            "width": width,
        "height": height,
        "promt": promt,
        "submitted": submitted,
        }
def main():
    configure_sitebar()


if __name__=="__main__":
    main()