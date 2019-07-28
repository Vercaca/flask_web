from app import create_app

if __name__ == '__main__':
    flask_app = create_app('default')
    flask_app.app_context().push()
    flask_app.run()
