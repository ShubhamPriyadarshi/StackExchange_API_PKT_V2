# Superset specific config
ROW_LIMIT = 5000
SECRET_KEY = 'Mzwone3Tms/NbAZ5OqbTSfQdi+0QAle0c9pZhGJhpTvuqUAJwuEUnaH7'
SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/shubhampriyadarshi/PycharmProjects/StackExchange_API_PKT/superset_se/superset.db'


# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''