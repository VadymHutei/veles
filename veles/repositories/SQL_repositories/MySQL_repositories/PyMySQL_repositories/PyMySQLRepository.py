from dataclasses import asdict

from pymysql import connect

from veles.repositories.SQL_repositories.MySQL_repositories.MySQLRepository import MySQLRepository
from veles.repositories.SQL_repositories.MySQL_repositories.PyMySQL_repositories.CredentialsDTO import CredentialsDTO


class PyMySQLRepository(MySQLRepository):

    def __init__(self, credentials: CredentialsDTO):
        self._credentials = credentials

    @property
    def connection(self, ):
        return connect(**asdict(self._credentials))
