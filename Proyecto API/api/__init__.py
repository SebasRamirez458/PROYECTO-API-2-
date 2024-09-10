from sodapy import Socrata
import pandas as pd

def consultar_api(departamento_usuario, municipio_usuario, cultivo_usuario, limite_registros):
    client = Socrata("www.datos.gov.co", None)
    result = client.get("ch4u-f3i5", departamento=departamento_usuario, municipio=municipio_usuario, cultivo=cultivo_usuario, limit=limite_registros)
    return result

def calcular_medianas(df, PH, Fosforo, Potasio):
    df[PH] = pd.to_numeric(df[PH], errors='coerce')
    df[Fosforo] = pd.to_numeric(df[Fosforo], errors='coerce')
    df[Potasio] = pd.to_numeric(df[Potasio], errors='coerce')

    mediana_campo1 = df[PH].median()
    mediana_campo2 = df[Fosforo].median()
    mediana_campo3 = df[Potasio].median()

    medianas = {
        "PH": mediana_campo1,
        "Fosforo": mediana_campo2,
        "Potasio": mediana_campo3
    }
    
    return medianas


def convertir_a_dataframe(result):
    pd.set_option('display.max_rows', None)
    #pd.set_option('display.max_columns', None)
    result_dt = pd.DataFrame.from_records(result)

    columnas_interes = ["departamento", "municipio", "cultivo", "topografia", 
                        "ph_agua_suelo_2_5_1_0", "f_sforo_p_bray_ii_mg_kg", "potasio_k_intercambiable_cmol_kg"]
    
    columnas_validas = [col for col in columnas_interes if col in result_dt.columns]
    df_filtrado = result_dt[columnas_validas] 

    
    medianas = calcular_medianas(df_filtrado, "ph_agua_suelo_2_5_1_0", "f_sforo_p_bray_ii_mg_kg", "potasio_k_intercambiable_cmol_kg")
    for key, value in medianas.items():
        df_filtrado[f'mediana_{key}'] = value

    return df_filtrado
