
from database import SQLite
from errors import ApplicationError


class Comment(object):

    def __init__(self, content, post_id, comment_id=None):
        self.id = comment_id
        self.post_id = post_id
        self.content = content

    def to_dict(self):
        return self.__dict__

    def save(self):
        with SQLite() as db:
            cursor = db.execute(self.__get_save_query())
            self.id = cursor.lastrowid
        return self

    @staticmethod
    def find_by_post(post_id):
        result = None
        with SQLite() as db:
            result = db.execute(
                    "SELECT content, post_id, id FROM comment WHERE post_id = ?",
                    (post_id,))
        comments = result.fetchall()
        return [Comment(*comment) for comment in comments]

    def __get_save_query(self):
        query = "{} INTO comment {} VALUES {}"
        if self.id == None:
            args = (self.content, self.post_id)
            query = query.format("INSERT", "(content, post_id)", args)
        else:
            args = (self.id, self.content, self.post_id)
            query = query.format("REPLACE", "(id, content, post_id)", args)
        return query






