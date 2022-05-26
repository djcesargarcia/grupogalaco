![Este es el logotipo de Galaco](/images/logogalaco.png)
	
# Aplicación de TMS para Grupo Galaco 
- Sistema de Gestión del transporte para la logística del Grupo Galaco.
Incluye mapa para la gestión del transporte en tiempo real así como 
una API Rest realizada con Django Rest Framework para la conexión con
(tablets).

# Ficheros contenidos en el TMS
- Carpeta principal (TMS Project)

# Apps creadas con Django en formato CRUD
- Driver
- Provider
- Routes
- Order
- Country
- Article
- Zone
- Vehicle
- Area
- Customer
- Distance (Not available)
- Loading Platform (Load Lorries) SP: Muelles.


# Mapa para la visualización en tiempo real de la logística
- Implementación con Leaflet para la captación de la geolocalización en todo momento
de los camiones en reparto para la asignación de las rutas más alternativas al tráfico 
rodado en la ciudad de Las Palmas.

# Implementación de los archivos estáticos de la App
- Directorio de Imágenes (Images).
- Directorio de Javascript (JS files) incluido en app de mapas en la carpeta static.

# Añadido de plugins
- Selenium webdriver 
- Dockers
- Jenkins
- Integrar en Visual Studio Web: Jenkins Files escritos en el Editor.

# Gestion de Syslog con CSV con la importación a base de datos Mysql

- Diseño de CSV ejemplo y app countries.
- Managements commands with load_child_data.py
- Migraciones para la subida del CSV a la bbdd.
