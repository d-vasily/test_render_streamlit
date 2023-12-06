import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
file_path = 'data.csv'  # Укажите путь к вашему CSV файлу
data = pd.read_csv(file_path)

# Заголовок приложения
st.title('Разведочный анализ данных')

# Отображение первых строк данных
st.subheader('Первые строки данных')
st.write(data.head())


# Описательные статистики
st.subheader('Описательные статистики')
st.write(data.describe())

st.subheader('Уникальные значения и их количество')
l_columns = []
for col in data.columns:
    if data[col].nunique() < 10:
        l_columns.append(col)
selected_column = st.selectbox('Выберите колонку', l_columns)
st.write(data[selected_column].value_counts())



# Графики распределений признаков
st.subheader('Графики распределений признаков')

# Выберите колонну для построения гистограммы
selected_column = st.selectbox('Выберите колонку для построения гистограммы', data.columns)
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data[selected_column], kde=True, ax=ax)
plt.grid()
st.pyplot(fig)

# Матрица корреляций
st.subheader('Матрица корреляций')
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)

# Графики зависимостей целевой переменной и признаков
st.subheader('Scatterplot целевой переменной и признаков')

# Выбираем признак для оси y
selected_column_y = st.selectbox('Выберите признак для оси y', data.columns)

# Создаем график с осью x как 'TARGET' и осью y как выбранный признак
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='TARGET', y=selected_column_y, data=data, ax=ax)
st.pyplot(fig)

# Boxplots для сравнения различных категорий
st.subheader('Boxplots признаков с делением по TARGET')

# Выбор колонны для сравнения
selected_column_boxplot = st.selectbox('Выберите колонку для построения Boxplot', data.columns)

fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='TARGET', y=selected_column_boxplot, data=data, ax=ax)
st.pyplot(fig)

# streamlit run main.py