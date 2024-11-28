import streamlit as st
import pandas as pd
import numpy as np
 
st.set_page_config(page_title = "Título de la web", page_icon = "😉")

st.title("Mi segunda aplicación con Streamlit")

st.write("Mi nombre Leonardo Dcbv ^^,")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns = ["a", "b", "c"])

st.line_chart(chart_data)

st.scatter_chart(chart_data)

st.bar_chart(chart_data)

st.table(chart_data)