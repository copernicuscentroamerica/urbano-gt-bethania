"""Flujo reproducible de evaluación multicriterio de riesgo predial y de techos
en el asentamiento Nueva León de Judá (Zona 7, Colonia Bethania, Ciudad de Guatemala).
Integra DEM 0.5 m (curvas cada 1 m), mapa de pendientes, servidumbre eléctrica y
huellas de techos Google-Microsoft Open Buildings + ortofoto RPAS (~2.4 cm/px).
"""
from pathlib import Path
import geopandas as gpd
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CAPAS = ROOT / "geovisor" / "capas"

def calcular_resumen_riesgo() -> pd.DataFrame:
    zonas = gpd.read_file(CAPAS / "zonas_riesgo_pendiente_leondejuda.geojson")
    techos = gpd.read_file(CAPAS / "techos_vivienda_riesgo_leondejuda.geojson")
    lotes = gpd.read_file(CAPAS / "lotes_leondejuda.geojson")
    filas = []
    for nivel in ["Muy Alto", "Alto", "Medio", "Bajo"]:
        filas.append({
            "nivel_riesgo": nivel,
            "superficie_pendiente_ha": round(float(zonas.loc[zonas["nivel_riesgo"] == nivel, "area_ha"].sum()), 3),
            "techos_n": int((techos["nivel_riesgo"] == nivel).sum()),
            "predios_n": int((lotes["nivel_riesgo"] == nivel).sum()),
        })
    return pd.DataFrame(filas)

if __name__ == "__main__":
    df = calcular_resumen_riesgo()
    print(df.to_string(index=False))
