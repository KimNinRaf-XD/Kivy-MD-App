"""
This type stub file was generated by pyright.
"""

from os import environ

'''
Cache manager
=============

The cache manager can be used to store python objects attached to a unique
key. The cache can be controlled in two ways: with a object limit or a
timeout.

For example, we can create a new cache with a limit of 10 objects and a
timeout of 5 seconds::

    # register a new Cache
    Cache.register('mycache', limit=10, timeout=5)

    # create an object + id
    key = 'objectid'
    instance = Label(text=text)
    Cache.append('mycache', key, instance)

    # retrieve the cached object
    instance = Cache.get('mycache', key)

If the instance is NULL, the cache may have trashed it because you've
not used the label for 5 seconds and you've reach the limit.
'''
__all__ = ('Cache', )
class Cache:
    '''See module documentation for more information.
    '''
    _categories = ...
    _objects = ...
    @staticmethod
    def register(category, limit=..., timeout=...): # -> None:
        '''Register a new category in the cache with the specified limit.

        :Parameters:
            `category`: str
                Identifier of the category.
            `limit`: int (optional)
                Maximum number of objects allowed in the cache.
                If None, no limit is applied.
            `timeout`: double (optional)
                Time after which to delete the object if it has not been used.
                If None, no timeout is applied.
        '''
        ...
    
    @staticmethod
    def append(category, key, obj, timeout=...): # -> None:
        '''Add a new object to the cache.

        :Parameters:
            `category`: str
                Identifier of the category.
            `key`: str
                Unique identifier of the object to store.
            `obj`: object
                Object to store in cache.
            `timeout`: double (optional)
                Time after which to delete the object if it has not been used.
                If None, no timeout is applied.

        :raises:
            `ValueError`: If `None` is used as `key`.

        .. versionchanged:: 2.0.0
            Raises `ValueError` if `None` is used as `key`.

        '''
        ...
    
    @staticmethod
    def get(category, key, default=...): # -> None:
        '''Get a object from the cache.

        :Parameters:
            `category`: str
                Identifier of the category.
            `key`: str
                Unique identifier of the object in the store.
            `default`: anything, defaults to None
                Default value to be returned if the key is not found.
        '''
        ...
    
    @staticmethod
    def get_timestamp(category, key, default=...): # -> None:
        '''Get the object timestamp in the cache.

        :Parameters:
            `category`: str
                Identifier of the category.
            `key`: str
                Unique identifier of the object in the store.
            `default`: anything, defaults to None
                Default value to be returned if the key is not found.
        '''
        ...
    
    @staticmethod
    def get_lastaccess(category, key, default=...): # -> None:
        '''Get the objects last access time in the cache.

        :Parameters:
            `category`: str
                Identifier of the category.
            `key`: str
                Unique identifier of the object in the store.
            `default`: anything, defaults to None
                Default value to be returned if the key is not found.
        '''
        ...
    
    @staticmethod
    def remove(category, key=...): # -> None:
        '''Purge the cache.

        :Parameters:
            `category`: str
                Identifier of the category.
            `key`: str (optional)
                Unique identifier of the object in the store. If this
                argument is not supplied, the entire category will be purged.
        '''
        ...
    
    @staticmethod
    def print_usage(): # -> None:
        '''Print the cache usage to the console.'''
        ...
    


if 'KIVY_DOC_INCLUDE' not in environ:
    ...
