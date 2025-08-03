import openpyxl
import os

ARCHIVO = "backend/datos.xlsx"

def obtener_libro():
    if os.path.exists(ARCHIVO):
        return openpyxl.load_workbook(ARCHIVO)
    else:
        libro = openpyxl.Workbook()
        libro.save(ARCHIVO)
        return libro

def guarda_hoja(hoja):
    libro = hoja.parent
    libro.save(ARCHIVO)
