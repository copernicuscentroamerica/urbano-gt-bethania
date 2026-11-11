## Alcance técnico y metodológico implementado (Nueva León de Judá)

Esta sección documenta el flujo metodológico ejecutado para construir el **Modelo Digital de Elevación (DEM)**, el **Mapa de Pendientes** y la **Clasificación de Riesgo por Techo de Vivienda (Open Buildings + RPAS)** en la zona acotada de **Nueva León de Judá** (`S20-LDJ`).

### 1. Delimitación de la zona de estudio por recuadro predial

- Se tomó como referencia la capa vectorial de predios `lotes_leondejuda.shp` (105 polígonos en proyección `EPSG:32615` — WGS 84 / UTM Zone 15N).
- A partir de su envolvente mínima (*bounding box*: `xmin: 766,936.99 m`, `ymin: 1,622,953.54 m`, `xmax: 767,133.32 m`, `ymax: 1,623,253.85 m`) se aplicó un margen perimetral de **12 metros** para conformar un **recuadro rectangular de estudio** de `220.3 m × 324.3 m` (**7.15 ha**; `bbox EPSG:4326: [-90.521391, 14.66695, -90.519314, 14.669902]`).

### 2. Generación del Modelo Digital de Elevación (DEM 0.5 m) desde curvas de nivel

1. **Densificación de vértices topográficos:** Se seleccionaron las curvas de nivel de 1 m (`leóndejuda_curvas_clip.shp`) dentro del recuadro de estudio más un margen de guarda de 45 m (para eliminar artefactos de borde) y se densificaron sus vértices cada `2.5 m`, obteniendo **51,789 puntos `(x, y, z)`** con cotas entre `1,308 m` y `1,439 m s. n. m.`.
2. **Triangulación de Delaunay (TIN) e interpolación baricéntrica:** Mediante `shapely.delaunay_triangles` se construyeron **102,836 triángulos** y se resolvió la ecuación del plano `z = a·x + b·y + c` de cada faceta sobre una malla regular de **0.5 m/píxel** (`649 × 441 píxeles` en `EPSG:32615`).
3. **Filtrado de aristas TIN y sombreado analítico:** Se aplicó un filtro de suavizado gaussiano local para garantizar continuidad de primer orden en las derivadas parciales (`dz/dx`, `dz/dy`), obteniendo un DEM con cota mínima de **1,320.55 m**, máxima de **1,436.00 m** y media de **1,381.57 m s. n. m.**, acompañado de un sombreado analítico de relieve (*hillshade*, acimut solar `315°`, altitud `45°`).

### 3. Cálculo del Mapa de Pendientes y clasificación de amenaza de ladera

A partir del gradiente espacial del DEM de 0.5 m se calculó la pendiente en grados (`slope_deg = arctan(sqrt((dz/dx)² + (dz/dy)²))`) y en porcentaje, clasificando el territorio en cuatro rangos geotécnicos:

| Clase | Nivel de riesgo por pendiente | Rango en grados | Rango en porcentaje | Superficie en el recuadro | Proporción |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Clase 1** | 🟩 **Bajo** | `< 12°` | `< 21%` | `4,564.6 m²` (`0.46 ha`) | `6.4%` |
| **Clase 2** | 🟨 **Medio** | `12° – 22°` | `21% – 40%` | `3,356.9 m²` (`0.34 ha`) | `4.7%` |
| **Clase 3** | 🟧 **Alto** | `22° – 32°` | `40% – 62%` | `7,824.5 m²` (`0.78 ha`) | `11.0%` |
| **Clase 4** | 🟥 **Muy Alto / Crítico** | `> 32°` | `> 62%` | `55,661.4 m²` (`5.57 ha`) | `77.9%` |

### 4. Obtención de Open Buildings y clasificación de riesgo por techo de vivienda

1. **Extracción desde Google-Microsoft Open Buildings:** Se consultó mediante *HTTP Range Requests* la partición de Guatemala (`country_iso=GTM/GTM.parquet`, *row group 1544*) del catálogo combinado **Google-Microsoft Open Buildings (VIDA / Source Cooperative)**, recuperando **411 edificaciones** en el entorno de Colonia Bethania, de las cuales **100 polígonos** se ubican directamente dentro del recuadro de estudio de Nueva León de Judá.
2. **Individualización catastral y restitución fotogramétrica RPAS:** Dado que en asentamientos densos con cubiertas de lámina adosadas el modelo satelital agrupa varios techos contiguos en macro-polígonos, las huellas de *Open Buildings* se subdividieron utilizando los linderos de los **105 lotes** de UDEVIPO (con retranqueo técnico de `0.25 m`). En los 11 lotes ocupados donde la cobertura arbórea o el tamaño reducido impidió la detección satelital, se restituyó la huella del techo a partir de la ortofoto de dron (`leon_de_juda.tif`, `2.4 cm/px`), conformando un total de **124 techos de vivienda** (`105` dentro del asentamiento catastrado y `19` en el entorno inmediato del recuadro; **113** con fuente *Google-Microsoft Open Buildings* y **11** con *Restitución RPAS + Catastro*).
3. **Modelo multicriterio de nivel de riesgo por techo (`0 – 100 puntos`):**
   - **Amenaza por pendiente en el entorno de cimentación del techo (`0 – 46 pts`):** Calculada sobre el percentil 90 de pendiente (`pendiente_max_deg`) en un buffer de `1.5 m` alrededor de cada techo (`>=32°`: 46 pts; `24°–32°`: 34 pts; `15°–24°`: 20 pts; `<15°`: 8 pts).
   - **Exposición a servidumbre de líneas de alta tensión (`0 – 32 pts`):** Intersección directa del techo con los 3 polígonos de `lineasdealtatension_leondejuda.shp` (`32 pts` si el área bajo el corredor supera 4 m²; `26 pts` en intersección parcial).
   - **Factor hidro-sanitario de saturación de talud (`0 – 14 pts`):** Descarga directa de aguas negras o grises `Al barranco` (`+10 pts`) o infiltración in situ por pozo ciego/fosa séptica en ladera (`+5 pts`), más escorrentía pluvial directa al barranco (`+4 pts`).
   - **Vulnerabilidad física y sobrecarga (`0 – 6 pts`):** Cubierta de lámina (`+3 pts`) y edificaciones de 2 o 3 niveles emplazadas sobre pendientes `>=20°` (`+3 pts`).
   - **Umbrales de clasificación:**
     - 🟥 **Muy Alto (`>= 62 pts` o pendiente crítica `>= 32°` + alta tensión):** **24 techos** (18 en el asentamiento).
     - 🟧 **Alto (`44 – 61 pts`, en alta tensión o pendiente `>= 26°`):** **70 techos** (60 en el asentamiento).
     - 🟨 **Medio (`25 – 43 pts` o pendiente `14° – 26°`):** **19 techos** (19 en el asentamiento).
     - 🟩 **Bajo (`< 25 pts` y fuera de alta tensión en pendiente `< 14°`):** **11 techos** (8 en el asentamiento).

## Referencias documentales y de datos del expediente

- `S20` — `0. Perfiles de Proyectos/Grupo 5_Guatemala_Asentamientos Alto Riesgo/Ficha_05_Guatemala_Asentamientos_Alto_Riesgo.docx`.
- `S20-LDJ` — Levantamiento geoespacial del asentamiento **Nueva León de Judá** (`lotes_leondejuda.shp`, `lineasdealtatension_leondejuda.shp`, `leóndejuda_curvas_clip.shp`, `leon_de_juda.tif`) + **Google-Microsoft Open Buildings** (`GTM.parquet`).
