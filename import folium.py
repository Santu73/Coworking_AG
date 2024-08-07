import folium
import geopandas as gpd

# Definir las coordenadas de la ubicación central del mapa
latitud = -31.6528
longitud = -64.4283

# Cargar el archivo GeoJSON con las regiones de la ciudad
gdf = gpd.read_file(r'C:/Users/Usuario/Documents/1/Posibilidades_de_Infraestructura_en_Alta_Gracia.geojson')

# Crear un mapa centrado en la ciudad
m = folium.Map(location=[latitud, longitud], zoom_start=13)

# Función para generar el contenido del popup
def popup_html(feature):
    nombre = feature['properties'].get('Name', 'N/A')  # Usar el campo 'Name' del GeoJSON
    # Aquí se asume que cada polígono tiene tipos de construcciones predefinidos. 
    # Puedes modificar esta parte para obtener datos más específicos si los tienes.
    construcciones = ["Construcción A", "Construcción B", "Construcción C"]
    html = f"""
    <h4>{nombre}</h4>
    <p>Tipos de construcciones permitidas:</p>
    <ul>
        {''.join([f'<li>{c}</li>' for c in construcciones])}
    </ul>
    """
    return html

# Agregar las regiones al mapa
folium.GeoJson(
    gdf,
    name='Regiones',
    style_function=lambda feature: {
        'fillColor': 'blue',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.5,
    },
    highlight_function=lambda feature: {'fillColor': 'yellow', 'color': 'yellow', 'weight': 2},
    tooltip=folium.GeoJsonTooltip(fields=['Name']),  # Usar el campo 'Name' del GeoJSON
    popup=folium.GeoJsonPopup(fields=['Name'], aliases=['Nombre'], labels=True)
).add_to(m)

# Guardar el mapa en un archivo HTML
m.save('mapa_interactivo.html')
