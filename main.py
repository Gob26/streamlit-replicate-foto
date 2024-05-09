import time
import streamlit as st
import replicate

st.markdown("# :rainbow[ИИ для создания изображений]")


REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]
def configure_sitebar():
    with st.sidebar:
        with st.form('my form'):
            width = st.number_input('Ширина изображения', min_value=256, max_value=2048,value=1024, step=16)
            height = st.number_input('Высота изображения',min_value=256, max_value=2048,value=1024, step=16)
            prompt = st.text_area('Введите ПРОМТ для создания изображения')
            submitted = st.form_submit_button("Создать", type="primary")

        return {
            "width": width,
        "height": height,
        "prompt": prompt,
        "submitted": submitted,
        }


def main_page(
                width:int,
                height:int,
                prompt:str,
                submitted:bool,
):
    if submitted:
        with st.spinner('Обработка'):
            output = replicate.run(
                "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
                input={
                    "width": width,
                    "height": height,
                    "prompt": prompt,
                }
            )
          #  time.sleep(5)

def main():
    data = configure_sitebar()
    main_page(**data)

if __name__=="__main__":
    main()
