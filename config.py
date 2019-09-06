class FlaskConfig:
    # DEBUG = True
    @staticmethod
    def init_app(app):
        pass


config = {
    'default': {
        'flask': FlaskConfig
    }
}
