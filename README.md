#Self-Esteem Course

## Usage

```
git clone git@github.com:dizballanze/m00dbot.git
cd m00dbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Create database
python create_db.py <database file name>
# Start bot
TG_TOKEN="<telegram bot token>" DB_NAME="<database file name>" python bot.py
```

