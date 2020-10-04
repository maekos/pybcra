import json
import requests
import logging


logger = logging.getLogger('estadisticas')

class BCRA:
    """ Obtiene estadisticas del banco central de la republica argentina

    Args:
        token: el token de acceso lo obtienen desde https://estadisticasbcra.com/api/registracion
    """
    URL_BASE =  'http://api.estadisticasbcra.com/'

    request_headers = {
        "Authorization": ""
    }
    TOKEN = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzMzODI1NTksInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJtYWVrb3NAZ21haWwuY29tIn0.rV208aRieKLD_g00nRepgUHaJXmLSdIcJEgVK4RTp-HmcNm8CvowFaDBeDj_59S8uS_Vs6GhVLpaYkNlUCIFLw'

    querys = {
        'milestones': 'eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)',
        'base': 'base monetaria',
        'base_usd': 'base monetaria dividida USD',
        'reservas': 'reservas internacionales',
        'base_div_res': 'base monetaria dividida reservas internacionales',
        'usd': 'cotización del USD',
        'usd_of': 'cotización del USD Oficial',
        'cuentas_corrientes': 'cuentas corrientes',
        'cajas_ahorro': 'cajas de ahorro',
        'plazo_fijo': 'plazos fijos',
        'otros_depositos': 'otros depositos',
        'tasa_int_dep': 'tasa de interés por depósitos',
        'tasa_badlar': 'tasa BADLAR',
        'tasa_baibar': 'tasa BAIBAR',
        'cer': 'CER',
        'uva': 'UVA',
        'uvi': 'UVI',
        'm2_privado_variacion_mensual': 'M2 privado variación mensual',
        'var_usd_vs_usd_of': 'porcentaje de variación entre la cotización del USD y el USD oficial',
        'lebac': 'LEBACs',
        'lebac_nominal': 'LEBACs (Nominal)',
        'circulacion_monetaria': 'circulación monetaria',
        'billetes_y_monedas': 'billetes y monedas',
        'efectivo_en_ent_fin': 'efectivo en entidades financieras',
        'depositos_cuenta_ent_fin': 'depositos de entidades financieras en cuenta del BCRA',
        'var_usd_anual': 'variación anual del dólar (porcentaje de variación de la cotización del dólar un año despues a la cotización de la fecha indicada)',
        'var_usd_of_anual': 'variación anual del dólar oficial (porcentaje de variación de la cotización del dólar oficial un año despues a la cotización de la fecha indicada)',
        'var_merval_anual': 'variación anual del MERVAL (porcentaje de variación del MERVAL un año despues al la cotización de la fecha indicada)',
        'merval': 'MERVAL',
        'merval_usd': 'MERVAL dividido cotización del USD',
    }

    def __init__(self,token):
        self.token = token
        self.request_headers['Authorization'] = "bearer {}".format(self.token)
        for k in self.querys.keys():
            setattr(self, k, lambda k=k: json.loads(self._get(k).content))


    def _get(self, query):
        url = self.URL_BASE + query
        try:
            r = requests.get(url=url, headers=self.request_headers)  # Add Timeout
        except:
            logger.error("Request timeout or something is wrong")
            return None
        return r
