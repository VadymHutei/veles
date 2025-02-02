from dataclasses import dataclass

import pymysql


@dataclass
class CredentialsDTO:

    host: str
    username: str
    password: str
    database: str
    charset: str = 'utf8mb4'
    cursorclass = pymysql.cursors.DictCursor
