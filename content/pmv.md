## Evidencias geoespaciales integradas en el Producto Mínimo Viable (PMV)

A partir de los levantamientos de **Nueva León de Judá** (Zona 7, colonia Bethania) y la integración de **Google-Microsoft Open Buildings**, el Producto Mínimo Viable cuenta con un geovisor operativo y nueve capas publicadas en `geovisor/capas/`:

1. **Modelo Digital de Elevación TIN a 0.5 m (`modelo_elevacion_leondejuda_cog.tif` y `.webp`):**
   - Generado mediante interpolación baricéntrica sobre una red irregular de triángulos de Delaunay (`102,836` triángulos construidos a partir de `51,789` vértices densificados de las curvas de nivel de 1 m).
   - Representa con fidelidad la transición entre la plataforma superior (`~1,436 m s. n. m.`) y el fondo de las laderas del barranco (`~1,320.5 m s. n. m.`).

2. **Mapa continuo de pendientes y zonificación vectorial de amenaza (`mapa_pendientes_leondejuda_cog.tif`, `.webp` y `zonas_riesgo_pendiente_leondejuda.geojson`):**
   - Clasifica el relieve en cuatro niveles de riesgo topográfico:
     - **Bajo (`< 12°` / `< 21%`):** `4,564.6 m²` (`6.4%`) — plataforma suave.
     - **Medio (`12° – 22°` / `21% – 40%`):** `3,356.9 m²` (`4.7%`) — ladera moderada.
     - **Alto (`22° – 32°` / `40% – 62%`):** `7,824.5 m²` (`11.0%`) — ladera fuerte susceptible a erosión.
     - **Muy Alto (`> 32°` / `> 62%`):** `55,661.4 m²` (`77.9%`) — escarpes y taludes críticos del barranco.

3. **Techos de vivienda clasificados por nivel de riesgo (`techos_vivienda_riesgo_leondejuda.geojson`):**
   - Integra **124 huellas de techos de vivienda** (`4,752.27 m²` techados): **113** provenientes del catálogo satelital **Google-Microsoft Open Buildings** (individualizadas por lindero predial) y **11** restituidas directamente sobre la ortofoto RPAS de `2.4 cm/px`.
   - Cada techo cuenta con su nivel de riesgo multicriterio (**Muy Alto: 24**, **Alto: 70**, **Medio: 19**, **Bajo: 11**), puntaje de riesgo (`0–100`), cota media, pendiente media y máxima en el entorno de cimentación, condición de servidumbre de alta tensión y sistema de desfogue sanitario.

4. **Catastro de predios enriquecido (`lotes_leondejuda.geojson`):**
   - Contiene los **105 predios** (**8,089.32 m²**) divididos en **Sector A** (50), **Sector B** (32), **Sector C** (22) y 1 predio sin sector, ahora enriquecidos con elevación media, pendiente máxima y clasificación de riesgo predial (**Muy Alto: 18**, **Alto: 60**, **Medio: 19**, **Bajo: 8**).

5. **Ortofoto RPAS (`ortofoto_leondejuda_cog.tif` / `.webp`), Líneas de alta tensión (`lineas_alta_tension_leondejuda.geojson`), Curvas de nivel de 1 m (`curvas_nivel_leondejuda.geojson`) y Recuadro de zona de estudio (`recuadro_zona_estudio_leondejuda.geojson`).**

## Especificación de módulos interactivos en el Geovisor

- **Conmutación de capas raster y vectoriales:** El panel lateral permite activar/desactivar y graduar la opacidad de la ortofoto RPAS, el mapa continuo de pendientes, el Modelo Digital de Elevación (DEM), la zonificación vectorial de pendientes y los techos de vivienda clasificados por riesgo.
- **Simbología semafórica automática (`auto_riesgo`):** Tanto los techos de vivienda como los predios y zonas de pendiente utilizan codificación cromática estandarizada: **Rojo (`#D92626`) = Muy Alto**, **Naranja (`#F2781C`) = Alto**, **Amarillo (`#F2C94C`) = Medio** y **Verde (`#2B9E5A`) = Bajo**.
- **Ficha emergente por techo y por lote:** Al hacer clic sobre cualquier techo (`TECHO-001` a `TECHO-124`) o predio se despliega su desglose de factores de riesgo (`factores_riesgo`), pendiente en grados, elevación en m s. n. m., fuente de la huella (`Google-Microsoft Open Buildings` vs `Restitución RPAS`) y variables sanitarias.
