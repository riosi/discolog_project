from discolog.core import get_albums_from_database, add_album_to_database

# assert -> assegurar que a chamada da função é verdadeira
def test_add_album_to_database():
    assert add_album_to_database("Alone in the City", "Dreamcatcher", 2019, 9, "O problema é que acaba")


def test_get_albums_from_database():
    # Arrange
    add_album_to_database("Alone in the City", "Dreamcatcher", 2019, 9, "O problema é que acaba")
    # Act
    results = get_albums_from_database()
    # Assert
    assert len(results) > 0
