from app import create_app,db
from flask_script import Manager, Server

from flask_migrate import Migrate, MigrateCommand

app = create_app('development')
manager = Manager(app)
Migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)




if __name__ == "__main__":
    manager.run()