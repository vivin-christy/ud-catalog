class Auth:
    """
    Auth class contains details for flow used in OAuth authentication
    using Google
    """
    # OAuth credentials
    CLIENT_ID = '544406063127-k38vd06fg22m0802h9vo69i63ce0m3pf.apps.googleusercontent.com'
    CLIENT_SECRET = '9NEB4PQ5-UTtm5yW0yOIsiiq'
    # URI that google server will redirect to
    REDIRECT_URI = 'http://catalog.aavi.me/gCallback'
    # Endpoint to start OAuth request from
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    # Endpoint to fetch user token
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    # Endpoint to get user information at the end of oauth
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    # Data we plan to access from Google profile
    SCOPE = ['profile', 'email']
