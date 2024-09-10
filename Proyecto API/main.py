import api.__init__ as api
import ui.__init__ as ui

datos_usuario = ui.obtener_datos_usuario()
datos_api = api.consultar_api(datos_usuario[0],datos_usuario[1],datos_usuario[2],datos_usuario[3])
datos_df = api.convertir_a_dataframe(datos_api)
ui.mostrar_datos(datos_df)

