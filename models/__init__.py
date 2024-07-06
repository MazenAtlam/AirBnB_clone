#!/usr/bin/python3
"""Initialize the storage instance"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
