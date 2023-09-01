from pathlib import Path
import dotenv
import os

# Дирректории
ROOT = Path(__file__).resolve().parent
LOG = Path(ROOT, 'log')

# Файлы
USERS = Path(LOG, 'users.yaml')

# API
dotenv.load_dotenv()
TOKEN = os.getenv('TG_TOKEN')  # Токен телеграмм бота t.me/u_alex90_bot
