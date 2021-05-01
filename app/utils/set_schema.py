import functools

from alembic import op


def set_schema(schema):
    def decorator_set_schema(migration):
        @functools.wraps(migration)
        def wrapper_set_schema(*args, **kwargs):
            op.execute(f'SET search_path TO {schema};')
            migration()
            op.execute('SET search_path TO public;')
        return wrapper_set_schema
    return decorator_set_schema
