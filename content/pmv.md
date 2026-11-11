## Evidencias geoespaciales integradas en el Producto Mínimo Viable (PMV)

A partir de los datos técnicos del asentamiento **Nueva León de Judá** (Zona 7, colonia Bethania), el Producto Mínimo Viable cuenta con un geovisor operativo y cinco capas publicadas y validadas en `geovisor/capas/`:

1. **Delimitación por recuadro a partir de la capa de predios (`recuadro_zona_estudio_leondejuda.geojson` y `perimetro_zona_estudio.geojson`):**
   - Generado automáticamente a partir de los límites espaciales (*bounding box*) de los 105 lotes de `lotes_leondejuda.shp`, añadiendo un margen perimetral de 12 metros (`220.3 m × 324.3 m`, **7.15 ha**).
   - Actúa como máscara de enfoque territorial del visor y encuadra tanto el parcelario completo como la ortofoto de dron.

2. **Ortofoto RPAS de alta resolución (`ortofoto_leondejuda_cog.tif` y `ortofoto_leondejuda.webp`):**
   - Procesada desde el archivo original `leon_de_juda.tif` (`8087 × 6644 px`, ~2.4 cm/px en `EPSG:32615`) a coordenadas geográficas `EPSG:4326`.
   - Se despliega directamente sobre el lienzo de MapLibre GL JS con control de opacidad y está disponible como Cloud-Optimized GeoTIFF para análisis en SIG de escritorio.

3. **Catastro de predios y variables de saneamiento (`lotes_leondejuda.geojson`):**
   - Contiene los **105 predios** (**8,089.32 m²**) divididos en **Sector A** (50), **Sector B** (32), **Sector C** (22) y 1 predio sin sector.
   - Permite consultar al hacer clic sobre cada predio su código de lote (`LOTE`), sector, área en m², estado de ocupación, niveles de construcción, desfogue de aguas negras, aguas grises, aguas pluviales y si presenta intersección con la franja de alta tensión.

4. **Franja de líneas de alta tensión (`lineas_alta_tension_leondejuda.geojson`):**
   - Representa los **3 polígonos** del corredor eléctrico (**4,303.51 m²**) que atraviesa el asentamiento.
   - El cruce espacial integrado en la capa de predios identifica **39 lotes** que se superponen total o parcialmente con esta franja de restricción.

5. **Curvas de nivel cada 1 m (`curvas_nivel_leondejuda.geojson`):**
   - Recorte de **536 curvas de nivel** (normales cada 1 m y directoras cada 5 m) dentro del recuadro de estudio de Nueva León de Judá, reflejando la fuerte pendiente hacia el barranco entre las cotas **1,308 m y 1,439 m s. n. m.**.

## Especificación de módulos de aplicación en el Geovisor

- **Enfoque automático en Nueva León de Judá:** El visor inicia centrado en `[-90.520353, 14.668426]` con nivel de zoom `17.4`, mostrando el recuadro delimitador en cian y la máscara exterior atenuada.
- **Superposición multicapa con orden jerárquico garantizado:** La ortofoto RPAS se dibuja en la base de las capas del proyecto, seguida por las curvas de nivel de 1 m, los 105 predios coloreados según afectación por alta tensión, el corredor eléctrico en magenta y el recuadro delimitador en la parte superior.
- **Consulta interactiva por lote:** Al hacer clic sobre cualquier predio se despliega su ficha técnica sin exponer datos personales sensibles, facilitando la revisión de gabinete por parte de la Unidad de Catastro de UDEVIPO.
