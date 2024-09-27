import os


# The number of CPUs to be used
workers = int(os.environ.get('GUNICORN_PROCESSES', '2'))

# The number of threads per worker
threads = int(os.environ.get('GUNICORN_THREADS', '4'))

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

# The bind address
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')


# The access log file to write to
forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

# Run gunicorn
# gunicorn --config gunicorn_config.py app:app