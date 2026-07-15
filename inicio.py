import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Dashboard PIB APEC",
    layout="wide"
)


df = pd.read_csv("pib_limpio.csv")

for col in df.columns[2:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")


apec = [
    'Australia',
    'Brunei Darussalam',
    'Canadá',
    'Chile',
    'China',
    'Corea, República de',
    'Estados Unidos',
    'Federación de Rusia',
    'Filipinas',
    'Hong Kong, Región Administrativa Especial',
    'Indonesia',
    'Japón',
    'Malasia',
    'México',
    'Nueva Zelandia',
    'Papua Nueva Guinea',
    'Perú',
    'Singapur',
    'Viet Nam'
]


df_apec = df[df["Country Name"].isin(apec)]


st.title("Dashboard Interactivo")
st.subheader("Crecimiento del PIB (% anual) - Países APEC") whith


st.sidebar.header("Panel de navegación")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpjWwKg2T0Y8Uek5thVlKtlQQyjijaqRWlpSw7qLSFeA&s=10", use_container_width=True)

pais = st.sidebar.selectbox(
    "Seleccione un país",
    sorted(df_apec["Country Name"].unique())
)


años = df_apec.columns[2:]


año_inicio, año_fin = st.slider(
    "Seleccione rango de años",
    min_value=int(años[0]),
    max_value=int(años[-1]),
    value=(int(años[0]), int(años[-1]))
)


años_filtrados = [
    str(año) for año in range(año_inicio, año_fin + 1)
]


datos_pais = df_apec[
    df_apec["Country Name"] == pais
][años_filtrados].iloc[0]


promedio_apec = df_apec[años_filtrados].mean()


fig, ax = plt.subplots(figsize=(12, 5))


ax.plot(
    años_filtrados,
    datos_pais,
    marker="o",
    label=pais
)


ax.plot(
    años_filtrados,
    promedio_apec,
    marker="o",
    label="Promedio APEC"
)


ax.set_title("Crecimiento del PIB (% anual)")
ax.set_xlabel("Año")
ax.set_ylabel("PIB (%)")

ax.legend()

plt.xticks(rotation=45)

st.pyplot(fig)



promedio_pais = round(datos_pais.mean(), 2)

promedio_grupo = round(promedio_apec.mean(), 2)

diferencia = round(
    promedio_pais - promedio_grupo,
    2
)



col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        label="Promedio PIB del país",
        value=f"{promedio_pais}%"
    )


with col2:
    st.metric(
        label="Promedio PIB APEC",
        value=f"{promedio_grupo}%"
    )


with col3:
    st.metric(
        label="Diferencia",
        value=f"{diferencia}%"
    )
