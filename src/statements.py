
__all__ = [
    'insert_comment_stmt',
    'get_comment_stmt',
]


insert_comment_stmt = """
    INSERT INTO comments (id, content, created_at) VALUES (%(id)s, %(content)s, %(created_at)s)
    RETURNING id
"""

get_comment_stmt = """
    SELECT * FROM comments WHERE id = %(id)s
"""
