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
                submitted:bool,):
    if submitted:
        with st.spinner('Обработка'):
            result = replicate.run(
                "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                input={
                    "width": width,
                    "height": height,
                    "prompt": prompt,
                }
            )
            image = result[0]   # получаем одну картинку
            with st.container(): #создаем пустой контейнер
                st.image(image, caption="получившиеся изображение" )


def main():
    data = configure_sitebar()
    main_page(**data)

if __name__=="__main__":
    main()
