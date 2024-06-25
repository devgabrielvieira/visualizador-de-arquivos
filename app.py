import streamlit as st
from pandas import read_csv

st.title('Visualizador de Arquivos')


file = st.file_uploader(
    label='Suba seu arquivo aqui!',
    type=['txt', 'json', 'jpg', 'png', 'csv', 'py', 'mp3', 'mp4'],
)

if file:
    if file.type == 'text/plain':
        st.text(file.read().decode())
    elif file.type == 'application/json':    
        st.json(file.read().decode())
    elif file.type == 'image/jpeg':
        st.image(file)
    elif file.type == 'text/csv':
        df = read_csv(file)
        st.dataframe(df)    
        st.line_chart(df.set_index('mês'))
        st.bar_chart(df.set_index('mês'))
    elif file.type == 'text/x-python':
        st.code(file.read().decode(), linguage='python')
    elif file.type == 'audio/mpeg':
        st.audio(file)  
    elif file.type == 'video/mp4':
        st.video(file)         

else:
    st.warning('Ainda não tem arquivo!')    