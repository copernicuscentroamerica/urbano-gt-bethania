## Alcance técnico y metodológico implementado (Nueva León de Judá)

Esta sección documenta tanto los parámetros originales declarados en el perfil institucional (`S20`) como el flujo metodológico ejecutado para construir el geovisor de la zona acotada de **Nueva León de Judá** (`S20-LDJ`).

### 1. Territorio, escala y delimitación por recuadro predial

- **Ciudad, sector y asentamiento:** Ciudad de Guatemala, Zona 7, colonia Bethania — **Asentamiento Nueva León de Judá**.
- **Escala principal de análisis:** Escala microurbana / predial (`1:1,000`).
- **Método de delimitación de la zona de estudio (Recuadro):**
  - Se tomó como referencia la capa vectorial de predios `lotes_leondejuda.shp` (105 polígonos originalmente en proyección `EPSG:32615` — WGS 84 / UTM Zone 15N).
  - Se calculó la envolvente mínima (*bounding box*) de la totalidad de los predios (`xmin: 766,936.99 m`, `ymin: 1,622,953.54 m`, `xmax: 767,133.32 m`, `ymax: 1,623,253.85 m`) y se aplicó un margen perimetral uniforme de **12 metros** para conformar un **recuadro rectangular de estudio** de `220.3 m × 324.3 m` (**71,458.5 m² = 7.15 ha**).
  - Reproyectado a `EPSG:4326`, el recuadro abarca el *bounding box* `[-90.521391, 14.66695, -90.519314, 14.669902]` con centroide en `14.668426, -90.520353`.

### 2. Procesamiento de capas geoespaciales locales

El flujo automatizado (`prepare_leondejuda_layers.py`) procesó las cuatro fuentes primarias de la carpeta de datos de **Nueva León de Judá**:

1. **Capa de predios (`lotes_leondejuda.shp` → `geovisor/capas/lotes_leondejuda.geojson`):**
   - Limpieza y normalización de atributos alfanuméricos (`LOTE`, `Sector`, `ocupacion`, `niveles`, `desfogue_a`, `aguas_gris`, `aguas_pluv`, ` Techo`, `Pared`, `Piso`).
   - Cálculo de superficie plana en UTM Zona 15N (`area_m2`), sumando **8,089.32 m²** (**0.81 ha**) en **105 predios**.
   - Cruce espacial con el corredor de líneas de alta tensión para etiquetar cada lote con el atributo `riesgo_at` (`Intersecta corredor alta tensión`: **39 lotes**; `Fuera de corredor`: **66 lotes**) y `area_at_m2` (superficie del lote bajo la franja eléctrica).

2. **Corredor de líneas de alta tensión (`lineasdealtatension_leondejuda.shp` → `geovisor/capas/lineas_alta_tension_leondejuda.geojson`):**
   - Reproyección de los **3 polígonos** de servidumbre eléctrica a `EPSG:4326` y cálculo de superficie (**4,303.51 m²**).

3. **Curvas de nivel cada 1 m (`leóndejuda_curvas_clip.shp` → `geovisor/capas/curvas_nivel_leondejuda.geojson`):**
   - Recorte espacial (*clip*) de las 9,716 curvas originales al recuadro de estudio de Nueva León de Judá, conservando **536 curvas** que describen con precisión las laderas del barranco entre **1,308 m y 1,439 m s. n. m.** (diferenciadas por el atributo `TIPO` en curvas `Directora` cada 5 m y `Normal` cada 1 m).

4. **Ortofoto de dron (`leon_de_juda.tif` → `geovisor/capas/ortofoto_leondejuda_cog.tif` y `geovisor/data/ortofoto_leondejuda.webp`):**
   - Reproyección mediante *warping* bilineal desde `EPSG:32615` (`8087 × 6644 px`, ~2.4 cm/px) a `EPSG:4326`.
   - Generación de un archivo **Cloud-Optimized GeoTIFF (COG)** con compresión JPEG/YCbCr y máscara de transparencia interna, más una textura **WebP RGBA** de alta resolución (`3072 × 2604 px`) servida directamente en el visor MapLibre GL JS sobre las coordenadas `[-90.520841, 14.668087, -90.519344, 14.669852]`.

---

## Parámetros declarados originalmente en el perfil institucional (`S20`)

Los siguientes campos conservan como referencia histórica la formulación inicial del perfil general para Colonia Bethania:

- **Instrumento de planificación o gestión al que aporta:** Plan de gestión de riesgo / regularización y escrituración en UDEVIPO.
- **Descripción del producto:** Ver a nivel de cada lote su condición de exposición y riesgo para toma de decisiones sobre obras de protección o escrituración.
- **Frecuencia de actualización prevista:** Semestral.
- **Nivel de acceso:** Uso institucional y consulta técnica agregada sin datos personales.
- **Pregunta orientadora:** ¿Qué variables físicas, topográficas y de servicios básicos determinan las condiciones de riesgo por lote en el asentamiento?

## Referencias documentales y de datos del expediente

- `S20` — `0. Perfiles de Proyectos/Grupo 5_Guatemala_Asentamientos Alto Riesgo/Ficha_05_Guatemala_Asentamientos_Alto_Riesgo.docx`.
- `S20-LDJ` — Levantamiento geoespacial del asentamiento **Nueva León de Judá** (`lotes_leondejuda.shp`, `lineasdealtatension_leondejuda.shp`, `leóndejuda_curvas_clip.shp` y `leon_de_juda.tif`).
