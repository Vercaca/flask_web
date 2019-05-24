from flask_script import Manager, Command, Server
from myapp import app


manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=5566))


class Hello(Command):
    """prints hello world"""
    def run(self):
        print("Hello World!")


# @manager.command
# def hello(name):
#     "Just say Hello"
#     print(f"Hello {name}")
#     # # $ python manage.py hello Joe
#     # #  hello Joe


@manager.option('-n', '--name', dest='name', default='joe', help="Your name")
@manager.option('-u', '--url', dest='url', default=None)
def hello(name, url):
    """
    :param name, url:
    :return:
    $ python manage.py hello -n Ver -u Yahoo
    hello, Ver, from Yahoo

    """
    if url is None:
        print(f"hello, {name}")
    else:
        print(f"hello, {name}, from {url}")


@manager.command
def verify(verified=False):
    """
    checks if verified
    :param verified:
    :return None:
\
    $ python manage.py verify -v
    VERIFIED? Yes
    $ python manage.py verify
    VERIFIED? No
    """
    print(f"VERIFIED? {'Yes' if verified else 'No'}")


if __name__ == '__main__':
    # manager.add_command('hello', Hello())
    # manager.run({"hello": Hello()})
    manager.run()
