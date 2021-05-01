from collections import namedtuple

Ingestion = namedtuple('Ingestion', ['schema', 'name', 'fields', 'file_format', 'file_path', 'header', 'parser'])