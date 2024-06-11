# https://cloudcomputinghuawei.streamlit.app/
import streamlit as st
import pandas as pd
import pip
pip.main(["install", "openpyxl"])
#from openpyxl import reader,load_workbook,Workbook
import numpy as np
from PIL import Image

##############
st.sidebar.image("img/huawei.png",
                 caption="HUAWEI: CLOUD COMPUTING")

#############################Pagina 1##############################    
def Home():
    st.markdown("# Temario")
    st.sidebar.markdown("# CLOUD COMPUTING")

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('Unidad 1: TABLAS')
        st.write('''Diseño. Quitar duplicados. Filtros básicos, filtros avanzados.
        Listas personalizadas. Validación de datos.''')
        
    with total2:
        st.info('Unidad 2: Funciones condicionales')
        st.write (pd.DataFrame({'Tema': ['Función SI',
                                          'Función SI', 
                                          'Formatos'], 
                                'Fecha': ["con varias condiciones", "(Y-O) anidada", 
                                           "condicionales"]}))
    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Unidad 3: Principales funciones usadas en bases de datos')
        st.write('''BDCONTAR, BDSUMA, BDMAX, BDMIN, BDPROMEDIO, BDCONTARA y BDEXTRAER. Función BUSCARV, Función BUSCARH''')
        
    with total4:
        st.info('Unidad 4: Gráficos')
        st.write ('''Diagrama de Gantt en Excel. Gráficos de Cumplimiento o de Progreso en EXCEL.''')

    total5, total6 = st.columns(2, gap='large')

    with total5:
        st.info('Unidad 2: Funciones condicionales')
        st.write (pd.DataFrame({'Tema': ['Creación de una Tabla Dinámica',
                                          'Cálculos', 
                                          'Extracción de datos'], 
                                'Fecha': ["Ordenamiento y agrupamiento de datos", "Formato", 
                                           "Modificación y actualización"]}))

    with total6:
        st.info('Unidad 6: Solver Excel')
        st.write ('''Aplicaciones y ejercicios.''')
    
#############################Pagina 2##############################    
def page2():
    st.markdown("Tablas en Excel")
    st.sidebar.markdown("Práctica Nº1")
    
    st.info('Generalidades')
    st.write('''El formato de tabla en Excel se refiere a una funcionalidad que convierte un rango de datos en una tabla estructurada y con estilo. Esta herramienta no solo mejora la apariencia visual de los datos, sino que también proporciona una serie de características que facilitan la gestión y el análisis de la información. Al aplicar el formato de tabla, los datos se organizan en filas y columnas claramente definidas, con la opción de incluir encabezados de fila y columna.''')
    st.write('''Para los siguientes ejercicios usar el libro llamado "practica 1 datos.xlsx" ''')
    st.info('A. Crear tablas y aplicarles formato')  

    df = pd.read_csv('csv/practica_1_datos_1.csv')
    st.write(df)
    st.write('''Para dar el formato de tabla en Excel a un rango de datos se deberá hacer lo siguiente:''')
    st.write('''(a) Seleccionar la lista de datos sea arrastrando con clic derecho sin soltar desde la primera celda hasta la ultima o usando el atajo Ctrl + E. Otra manera de seleccionar todos los datos es usar las teclas Ctrl + Shift + -> y luego Ctrl + Shift + ⭣''')

    st.write('''(b) Luego en la barra de herramientas clic en el icono “Dar formato como tabla” o usar el atajo Ctrl + T. Seleccione el estilo de color que mas le agrade. Finalmente dar aceptar verificando que la casilla de encabezados este marcada.''')    
    st.write('''(c) La apariencia cambiará de acuerdo a nuestra selección de estilo dando por finalizado el proceso.''')
    st.write('''(d) Crear un campo nuevo llamado Promedio y calcular el promedio simple de las 3 notas.''')
    #st.image("img/img1.png", caption="Tabla y promedio")  
    st.write('''(e) Crear un campo llamado Promedio2 que representa el promedio eliminando la nota mas baja. Use en la primera celda la formula.''')
    
    st.info('''=(SUMA(H2\:J2)-MIN(H2\:J2))/(CONTARA(H2\:J2)-1)''')
    #st.image("img/img2.png", caption="Tabla y promedio2")

    st.info("B. Filtro avanzado:")
    st.write('''(a) Crear una hoja nueva llamada Filtrar.''')
    st.write('''(b) En dos celdas contiguas colocar:''')

    #st.image("img/img3.png")

    st.write('''Esto representa los criterios de aplicación del filtro.''') 
    st.write('''Nota: Debe ser escrito tal como esta en la base de datos.''')
    st.write('''(c) Usar el filtro avanzado''')

    #st.image("img/img4.png")
    st.write('''(d) Seleccionar “Copiar a otro lugar”. En “Rango de la lista” seleccionar 
    la tabla de datos. En “Rango de criterios” seleccionar las celdas con los criterios de 
                filtro de la hoja Filtrar. En “Copiar a” indicar donde serán colocados los datos filtrados. ''')

    #st.image("img/img5.png")
    #st.image("img/img6.png")
    #st.image("img/img7.png")

    st.write("(e) Aplicar el siguiente filtro:")
    #st.image("img/img8.png")
    #st.image("img/img9.png")
  
    st.write("(f) Aplicar el siguiente filtro:")
    #st.image("img/img10.png")
    #st.image("img/img11.png")

    st.info("C. Quitar Duplicados")
    st.write("(a) Use la hoja base duplica y haga una copia.")
    st.write("(b) Dar formato de tabla.")
    #st.image("img/img12.png")
    st.write('''(c) Cada vez que se ingrese a la tabla se activa la ficha 
    "Diseño de tabla" donde encontrará la opción "Quitar duplicado" ''')
    #st.image("img/img13.png")

    st.write('''(d) Elegir el criterio de coincidencia, para este ejercicio 
    considerar ID estudiante, Apellido paterno, Apellido materno y Nombre. 
    Aceptar.''')
    #st.image("img/img14.png")
    #st.image("img/img15.png")
    st.write("Mensaje de Excel que indica la detección de duplicados y posterior eliminación.")

    st.info("Detección de valores duplicados mediante el uso de formato condicional")

    st.write('''Si se desea analizar los datos duplicados antes de eliminarlos se 
    puede proceder de la siguiente manera:''')
    st.write("(a) Copiar los datos darle formato de tabla.")
    st.write("(b) Seleccionar la columna que se usara para detectar registros duplicados.")
    st.write('''(c) Ir a “Formato condicional”, “Regla para resaltar celdas” y “Valores duplicados”''')

    #st.image("img/img16.png")

    st.write("(d) Se puede elegir el formato que se usara para resaltar los registros duplicados.")
    #st.image("img/img17.png")

    st.write("(e) Excel mostrara los duplicados de acuerdo al formato elegido.")
    #st.image("img/img18.png")

    st.write('''(f) Para una mejor visualización de los registros duplicados puede hacer 
    uso de la opción de filtro que tiene la tabla. Primero aplicar “Ordenar de menor a 
    mayor” y luego “Ordenar por color”.''')
    #st.image("img/img19.png")
    #st.image("img/img20.png")

    st.write("(g) Se muestra el resultado a continuación.")
    #st.image("img/img21.png")

    st.info("Validación de Datos")
    #st.image("img/img22.png")









#me quede en validacion de datos

#############################Pagina 3##############################    

def page3():
  st.header('''Funciones Condicionales''')

  st.info("A. Función SI con dos condiciones")
  st.write('''La función SI se utiliza para hacer una comparación lógica: 
  ¿Es el valor consultado idéntico al valor esperado o no? Solo si esta consulta es cierta,
  puede ocurrir un determinado evento. Si la comparación es incorrecta, se 
  desencadena otra acción, es decir, si A, entonces B; en caso contrario, C. La 
  función SI tiene los siguientes argumentos: ''')

#############################Pagina 4##############################    

def page4():
  st.header('Más información', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/Quimica_1_FIA_UNI/")

#############################Pagina 5##############################    

def page5():
  st.header('EXAMEN PARCIAL', divider='rainbow')
   
  st.link_button("SOLICITAR", "https://forms.gle/T8hNLvZeDQLZLbKy8")
  #https://drive.google.com/drive/folders/1H-X0lKR19MznkDvHQH_SpsdbAf_iVzVi?usp=sharing

#############################Pagina 6##############################    

def page6():
  st.header('Más información', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/Quimica_1_FIA_UNI/")

#############################Pagina 7##############################    

def page7():
  st.header('TABLAS DINÁMICAS', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/Quimica_1_FIA_UNI/")

  st.write('''Seleccionar... ''')

  #st.image("img/6_1.png")
  #st.image("img/6_2.png")
  #st.image("img/6_3.png")
  #st.image("img/6_4.png")
  #st.image("img/6_5.png")

#############################Pagina 8##############################    

def page8():
  st.header('Más información', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/Quimica_1_FIA_UNI/")

#############################Pagina 9##############################    

def page9():
  st.header('Más información', divider='rainbow')
   
  st.link_button("Github", "https://github.com/inefable12/Quimica_1_FIA_UNI/")

################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "Contenido del Curso": Home,
  "Clase 1. Tablas en Excel": page2,
  "Clase 2: Funciones Condicionales": page3,
  "Clase 3: Base de Datos": page4,
  "Examen Parcial": page5,
  "Clase 4: Gráficos": page6,
  "Clase 5: Tablas Dinámicas": page7,
  "Clase 6: Solver Excel": page8,
  "Examen Final": page9,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
