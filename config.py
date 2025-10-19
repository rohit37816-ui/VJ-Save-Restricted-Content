import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7642147352:AAGSBBCZBZ4tIKjhiORErp12m9KVGWGHnTY")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "7642147352"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "AAGSBBCZBZ4tIKjhiORErp12m9KVGWGHnTY")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6065778458"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rohit37816_db_user:Cl1HDQb4Zw4LYiTE@cluster0.ak3iyvi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
