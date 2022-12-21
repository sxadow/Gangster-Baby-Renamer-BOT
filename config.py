import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "5166878")

API_HASH = os.environ.get("API_HASH", "fdafb41f9a67f40e34a6c67f47730a92")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5819824799:AAHzJoDiqDzniXtNpNDo3emgj2GiPJnVefE

") 

FORCE_SUB = os.environ.get("FORCE_SUB", "tronmovies

") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://tron:tron@cluster0.xs0gvih.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/c6698434e5dd75bc43663.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1601316529 762308466').split()]

PORT = os.environ.get("PORT", "8080")
