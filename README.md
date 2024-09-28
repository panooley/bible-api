# bible-api
A python wrapper for the bible-api.com API provided by Tim Morgan

## Usage
Getting a single verse
```python
    from bible_api import BibleReader
    reader = BibleReader()
    # get_verse(book, chapter, verse)
    verse = reader.get_verse("genesis", 1, 1)
    print(verse)
```
```
In the beginning, God created the heavens and the earth.
 ```

Getting multiple verses
```python
    from bible_api import BibleReader
    reader = BibleReader()
    # get_verse_range(book, chapter, verse_start, verse_end)
    verse = reader.get_verse_range("john", 11, 35, 36)
    print(verse)
```
```text
Jesus wept.
The Jews therefore said, “See how much affection he had for him!”
```