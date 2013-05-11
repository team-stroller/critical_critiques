from base import *

########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
########## DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'critical_critiques_test',
        'USER': 'critical_critiques_test',
        'PASSWORD': 'critical_critiques_test',
        'PORT': '5432',
        'HOST': 'localhost',
        'OPTIONS': {
            'autocommit': True,
        }
    }
}


########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#broker-redis
BROKER_URL = 'redis://localhost:6379/0'
########## END CELERY CONFIGURATION

######### SOCIAL AUTH
GITHUB_APP_ID = '86a483896d08237f9062'
GITHUB_API_SECRET = '8bc213d537311efb600445b667c7e294c5e8ffb9'

######### END SOCIAL AUTH
