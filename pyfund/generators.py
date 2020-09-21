# generators.py
# Collection of utility methods for iterables using generators.

def take(count, iterable):
    """
    Extract items from front of an iterable.
    
    Args:
        count: The maximum number of items to retrieve.
        iterable: The source of the items.
    
    Yields:
        At most 'count' items from 'iterable'.
    """
    
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def distinct(iterable):
    """
    Return unique items from iterable by removing duplicates.
    
    Args:
        iterable: The source of the items.
    
    Yields:
        Unique elements, in order, from 'iterable'.
    """
    
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)
        
def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b
