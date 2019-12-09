import os


class Config(object):

    def __init__(self, data_dir):
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(data_dir, 'messages.sqlite')
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
