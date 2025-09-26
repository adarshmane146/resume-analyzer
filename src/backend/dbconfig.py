import os
from dotenv import dotenv_values
from urllib.parse import quote_plus  # <-- needed for special characters

# default local dev settings
env_local = {
    'username': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
}

# read your actual .env in backend folder
env_file_config = dotenv_values('.env')  

# AWS config if running on AWS (optional)
aws_config = {}
if 'RDS_HOSTNAME' in os.environ:
    aws_config = {
        'username': os.environ['RDS_USERNAME'],
        'password': os.environ['RDS_PASSWORD'],
        'host': os.environ['RDS_HOSTNAME'],
        'port': os.environ['RDS_PORT'],
        'database': os.environ['RDS_DB_NAME'],
    }

# merge configs: env_local < .env < aws_config
config = {**env_local, **env_file_config, **aws_config}

# encode password for SQLAlchemy connection URL
config['password'] = quote_plus(config['password'])
