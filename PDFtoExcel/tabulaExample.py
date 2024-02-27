### pip install tabula-py
### pip install pandas
### pip install openpyxl
### pip install JPype1

import tabula
import pandas as pd

archivo_pdf = "C:/ADySO/Python/pythonTaks/PDFtoExcel/Remates.pdf"

tablas_pdf = tabula.read_pdf(archivo_pdf, pages='2-18', multiple_tables=False)

df_final = pd.DataFrame()
for tabla in tablas_pdf:
    df_final = pd.concat([df_final, tabla])

drop_columna = "Refencia"
df_final = df_final.drop(columns=[drop_columna])

archivo_excel = "RematesExcel.xlsx"
df_final.to_excel(archivo_excel, index=False)

print("Archivo convertido")



# file_path = "PDFtoExcel/RematesExcel.pdf"
# output_path = "PDFtoExcel/RematesExcel.csv"
# df = tabula.read_pdf(file_path, pages="all")
# tabula.convert_into(file_path, output_path, output_format="csv", pages="all")
# print(df)

# Read pdf into list of DataFrame
#dfs = tabula.read_pdf("Remates.pdf", pages='[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]')

# convert PDF into CSV file
#tabula.convert_into("Remates.pdf", "output.xlsx", output_format="xlsx", pages='[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]')

# convert all PDFs in a directory
# tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')