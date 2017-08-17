from flask_script import Manager
from flask_script import Command
from index import app

manager = Manager(app)


class Hello(Command):
    def run(self):
        print("hello")


@manager.command
def hello():
    print("hello")


if '__main__' == __name__:
    manager.run()
