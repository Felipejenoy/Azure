# Configuración de la cadena de conexión
SERVER = 'felipe.database.windows.net'
DATABASE = 'Felipe'
USERNAME = 'felipe'
PASSWORD = 'johan.2020'
DRIVER = 'ODBC Driver 18 for SQL Server'

#connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
connectionString = 'DRIVER='+DRIVER+';SERVER='+SERVER+';PORT=1433;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+PASSWORD