## Alcance actual, hallazgos del modelo de riesgo y próximos pasos

### Hallazgos principales del análisis de elevación, pendientes y techos de vivienda

1. **Predominio de pendientes fuertes y escarpes de barranco:**
   - El Modelo Digital de Elevación (DEM de 0.5 m) revela un desnivel de **115.45 metros** dentro del recuadro de estudio (`1,320.55 m` a `1,436.00 m s. n. m.`).
   - El **77.9% del recuadro de estudio (`5.57 ha`)** presenta pendientes **Muy Altas (`> 32°`)** correspondientes a los flancos del barranco que rodean el asentamiento por el norte, oeste y sur, mientras que solo el **11.1% (`0.80 ha`)** tiene pendientes bajas a moderadas (`< 22°`).
2. **Clasificación de los 124 techos de vivienda (Open Buildings + RPAS):**
   - 🟥 **24 techos en Riesgo Muy Alto:** Corresponden principalmente a viviendas donde convergen dos o tres factores críticos: emplazamiento en borde de talud con pendiente máxima `>= 32°`, intersección con la franja de servidumbre de **líneas de alta tensión** y descarga directa de aguas negras/grises al barranco.
   - 🟧 **70 techos en Riesgo Alto:** Viviendas ubicadas sobre laderas fuertes (`22° – 32°`) o dentro de la franja de restricción eléctrica (39 predios intersectados en los Sectores A, B y C).
   - 🟨 **19 techos en Riesgo Medio:** Viviendas en pendiente moderada (`12° – 22°`) fuera del corredor de alta tensión.
   - 🟩 **11 techos en Riesgo Bajo:** Viviendas situadas en la plataforma de menor pendiente (`< 12°`), fuera de la servidumbre eléctrica y conectadas a red de drenaje.

### Limitaciones técnicas a considerar

- **Resolución del DEM interpolado:** El DEM de 0.5 m reproduce con fidelidad la topografía capturada por las curvas de nivel de 1 m (`leóndejuda_curvas_clip.shp`), pero no sustituye un levantamiento LiDAR debajo de vegetación densa ni estudios de mecánica de suelos para el diseño estructural de obras de contención.
- **Subdivisión de huellas Open Buildings:** En sectores con techos de lámina contiguos, las huellas satelitales de *Google-Microsoft Open Buildings* se individualizaron mediante corte con la cartografía catastral de UDEVIPO y verificación sobre la ortofoto RPAS (`2.4 cm/px`).
- **Protección de datos:** Todas las capas publicadas utilizan exclusivamente códigos técnicos (`TECHO-001` a `TECHO-124` y número de `LOTE`), sin exponer datos personales de las familias residentes.

### Próximos pasos recomendados para la Unidad de Catastro (UDEVIPO)

1. **Atención prioritaria a los 24 techos / 18 lotes clasificados en Riesgo Muy Alto:** Realizar inspección técnica en sitio en los lotes que combinan pendiente crítica de borde de barranco (`> 32°`) e intersección con el corredor de alta tensión.
2. **Obras de conducción de aguas grises y pluviales:** Intervenir prioritariamente los **40 lotes** que descargan aguas grises y **17 lotes** que descargan aguas negras hacia el barranco, dado que la infiltración continua sobre taludes de `> 25°` acelera procesos de erosión regresiva y deslizamiento.
3. **Dictamen de servidumbre eléctrica:** Coordinar con la entidad transmisora/distribuidora de energía la demarcación física en campo de los **39 predios** que intersectan los 3 polígonos de líneas de alta tensión antes de emitir resoluciones de escrituración.
