from bible_api import BibleReader

reader = BibleReader()
verse = reader.get_verse("genesis", 1, 1)
verses = reader.get_verse_range("john", 11, 35, 36)

print(verses)