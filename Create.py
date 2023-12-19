import psycopg2

conn = psycopg2.connect(database = 'mybd', user = 'postgres', password = 'postgres')
with conn.cursor() as cur:

	cur.execute("""CREATE TABLE IF NOT EXISTS Genres (
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(120) NOT NULL
	);
    """)
	cur.execute("""CREATE TABLE IF NOT EXISTS Artist (
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(120) NOT NULL UNIQUE
	);
    """)
	cur.execute("""CREATE TABLE IF NOT EXISTS Album (
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(120) NOT NULL,
	ReleaseAlbum DATE NOT NULL
	);
    """)
	cur.execute("""CREATE TABLE IF NOT EXISTS Track (
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(120) NOT NULL,
	Duration TIME NOT NULL,
	Albumid INTEGER REFERENCES Album(Id)
	);
	""")
	cur.execute("""CREATE TABLE IF NOT EXISTS ArtistGenre (
	ArtistId INTEGER REFERENCES Artist,
	GenreId INTEGER REFERENCES Genres,
	constraint pk PRIMARY KEY (ArtistId, GenreId)
	);
	""")
	cur.execute("""CREATE TABLE IF NOT EXISTS ArtistAlbum (
	ArtistId INTEGER REFERENCES Artist,
	AlbumId INTEGER REFERENCES Album,
	PRIMARY KEY (ArtistId, AlbumId)
	);
	""")
	cur.execute("""CREATE TABLE IF NOT EXISTS Collection (
	Id SERIAL PRIMARY KEY,
	Name VARCHAR(120) NOT NULL,
	ReleaseAlbum DATE NOT NULL
	);
	""")
	cur.execute("""CREATE TABLE IF NOT EXISTS CollectionTrack (
	CollectionId INTEGER REFERENCES Collection,
	TrackId INTEGER REFERENCES Track,
	PRIMARY KEY (CollectionId, TrackId)
	);
	""")
	conn.commit()
conn.close()