# PyBCRA

Obtiene las estadísticas del Banco Central de la Republica Argentina.

## Uso 

Deberán pedir el token en el siguiente [link](https://estadisticasbcra.com/api/registracion)

```
pip install pybcra
```

Una vez instalado y obtenido el TOKEN de acceso se puede comenzar a usar. 

```
from bcra.estadisticas import BCRA
bcra = BCRA(TOKEN)
# Para obtener el historico del valor del dolar:
bcra.usd()
```
La salida debería ser similar a esta:

```
[{'d': '2000-05-24', 'v': 1.0005},
 {'d': '2000-05-25', 'v': 1.0005},
 {'d': '2000-05-26', 'v': 1.0004},
 {'d': '2000-05-29', 'v': 1.0007},
 {'d': '2000-05-30', 'v': 1.0009},
 {'d': '2000-05-31', 'v': 1.001},
  ...
 {'d': '2020-02-28', 'v': 77.75}]
```

Los datos a pedir pueden ser los siguientes:

```
bcra.milestones() # eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)
bcra.base()  # base monetaria
bcra.base_usd(): base monetaria dividida USD
bcra.reservas(): reservas internacionales
bcra.base_div_res(): base monetaria dividida reservas internacionales
bcra.usd(): cotización del USD
bcra.usd_of(): cotización del USD Oficial
bcra.cuentas_corrientes(): cuentas corrientes
bcra.cajas_ahorro(): cajas de ahorro
bcra.plazo_fijo(): plazos fijos
bcra.otros_depositos(): otros depositos
bcra.tasa_int_dep(): tasa de interés por depósitos
bcra.tasa_badlar(): tasa BADLAR
bcra.tasa_baibar(): tasa BAIBAR
bcra.cer(): CER
bcra.uva(): UVA
bcra.uvi(): UVI
bcra.m2_privado_variacion_mensual(): M2 privado variación mensual
bcra.var_usd_vs_usd_of(): porcentaje de variación entre la cotización del USD y el USD oficial
bcra.lebac(): LEBACs
bcra.lebac_nominal(): LEBACs (Nominal)
bcra.circulacion_monetaria(): circulación monetaria
bcra.billetes_y_monedas(): billetes y monedas
bcra.efectivo_en_ent_fin(): efectivo en entidades financieras
bcra.depositos_cuenta_ent_fin(): depositos de entidades financieras en cuenta del BCRA
bcra.var_usd_anual(): variación anual del dólar (porcentaje de variación de la cotización del dólar un año despues a la cotización de la fecha indicada)
bcra.var_usd_of_anual(): variación anual del dólar oficial (porcentaje de variación de la cotización del dólar oficial un año despues a la cotización de la fecha indicada)
bcra.var_merval_anual(): variación anual del MERVAL (porcentaje de variación del MERVAL un año despues al la cotización de la fecha indicada)
bcra.merval(): MERVAL
bcra.merval_usd(): MERVAL dividido cotización del USD
```

Para mas información dirigirse a la página oficial del [BCRA](https://estadisticasbcra.com/api/documentacion)
