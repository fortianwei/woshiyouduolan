
class Article:

    def __init__(self, article_id, author_id, title, content, create_date,
                 modified_date, rating, comments, other_infos):
        self.article_id = article_id
        self.author_id = author_id
        self.title = title
        self.content = content
        self.create_date = create_date
        self.modified_date = modified_date
        self.rating = rating
        self.comments = comments
        self.other_infos = other_infos
