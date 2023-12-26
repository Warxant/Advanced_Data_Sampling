import time
import sqlite3
import psycopg2

conn = psycopg2.connect(database = 'mybd', user = 'postgres', password = 'psql1488')
with conn.cursor() as cur:

### Задание №2

    #  longest_track = cur.execute("""SELECT track.name, track.duration
    #                     FROM Track
    #                     WHERE track.duration = (SELECT MAX(track.duration)
    #                     FROM Track)
    #                     """);
    #  longest_track = cur.fetchall()
    #  print(f'Самый длинные треки: ', end='')
    #  for i in longest_track:
    #      for s in i:
    #         print(f'{s} ', end='')
#----------------------------------------------------------------------------------------------------------------
    # track_longer_x = cur.execute("""SELECT track.name, track.duration
    #                             FROM Track
    #                             WHERE duration>= '00:03:50'
    #                             LIMIT 33
    #                             """);                                       
    # track_longer_x = cur.fetchall()
    # print(f'Треки длиннее 3,5 минут: ', end='')
    # for i in track_longer_x:
    #     print(f'{i[0]} = {i[1]}, ', end='')
#-----------------------------------------------------------------------------------------------------------------
    # collections_released = cur.execute("""SELECT collection.name
    #                                 FROM Collection
    #                                 WHERE releasealbum >= '20180101' AND releasealbum <='20230101'       
    #                                 """)
    # collections_released = cur.fetchall()
    # print('Названия сборников, вышедших в период с 2018 по 2023 год включительно: ', end='')
    # for i in collections_released:
    #     print(f'{i[0]}', end=' ')
#-----------------------------------------------------------------------------------------------------------------
    # artist_with_one_word = cur.execute("""SELECT name
    #                                 FROM Artist
    #                                 where name not like '%% %%'             
    #                                 """)                                                              
    # artist_with_one_word = cur.fetchall()
    # print('Исполнители, чьё имя состоит из одного слова: ', end='')
    # for i in artist_with_one_word:
    #     print(f'{i[0]}', end=' ')
#-----------------------------------------------------------------------------------------------------------------
    # name_track_my = cur.execute("""SELECT name
    #                         FROM track
    #                         WHERE name LIKE '%%My%%'""")                    
    # name_track_my = cur.fetchall()
    # print('Название треков, которые содержат слово «мой» или «my»: ', end='')
    # for i in name_track_my:
    #     print(i[0], end='')
#-----------------------------------------------------------------------------------------------------------------

### Задание №3

    # artist_count_genre = cur.execute('''SELECT genres.name, COUNT(*)
    #                 FROM genres
    #                 JOIN artistgenre ON artistgenre.genreid = genres.id
    #                 JOIN artist ON artistgenre.artistid = artist.id
    #                 GROUP BY genres.name''')
    
    # artist_count_genre = cur.fetchall()
    # print('Количество исполнителей в каждом жанре = ', end='')
    # for i in artist_count_genre:
    #     print(f'{i[0]} - {i[1]}, ', end=' ')
#----------------------------------------------------------------------------------------------------------------
    # tracks_year_count = cur.execute(f"""SELECT COUNT(*)
    #                 FROM track
    #                 JOIN album ON album.id = track.albumid
    #                 WHERE album.releasealbum BETWEEN '20190101' AND '20200101'
    #                 """)
    
    # tracks_year_count = cur.fetchall()
    # for i in tracks_year_count:
    #     for s in i:
    #         print(f'Количество треков вошедших в альбомы 2019-2020 годов = {s}')
#----------------------------------------------------------------------------------------------------------------
    # avrg_duration_all_tracks = cur.execute("""SELECT album.name, AVG(track.duration) FROM track
    #                                  JOIN album ON album.id = track.albumid
    #                                  GROUP BY album.id
    #                                  ORDER BY AVG(track.duration);""")                   
    # avrg_duration_all_tracks = cur.fetchall()
    # print('Средняя продолжительность треков по каждому альбому: ', end='')
    # for i in avrg_duration_all_tracks:
    #     print(f'{i[0]} = {i[1]}', end=' ')
#----------------------------------------------------------------------------------------------------------------
    # artists_with_no_albums_at_year = cur.execute("""SELECT artist.name FROM artist
    #                                             LEFT JOIN
    #                                                 (SELECT DISTINCT artist.id, artist.name FROM artist
    #                                                 JOIN artistalbum ON artistalbum.artistid = artist.id
    #                                                 JOIN album ON album.id = artistalbum.albumid
    #                                                 WHERE album.releasealbum >= '2020-01-01' and album.releasealbum <= '2020-12-31')
    #                                                 AS ty
    #                                             ON artist.id = ty.id
    #                                             WHERE ty.id IS NULL""")
    # artists_with_no_albums_at_year = cur.fetchall()
    # print(f'Артисты не выпустившие альбомы в 2020 году: ', end='')
    # for i in artists_with_no_albums_at_year:
    #     for s in i:
    #         print(f'{s}, ', end='')
#----------------------------------------------------------------------------------------------------------------
    # artist_in_collection = cur.execute(f"""SELECT DISTINCT collection.name FROM collection
    #                                      JOIN collectiontrack ON collectiontrack.collectionid = collection.id
    #                                      JOIN track ON track.id = collectiontrack.trackid
    #                                      JOIN album ON track.albumid = album.id
    #                                      JOIN artistalbum ON album.id = artistalbum.albumid
    #                                      JOIN artist ON artist.id = artistalbum.artistid
    #                                      WHERE artist.id = (SELECT id FROM artist
    #                                                            WHERE name = 'Агата Кристи');""")
       
    # artist_in_collection = cur.fetchall()
    # print('Названия сборников, в которых присутствует конкретный исполнитель: ', end='')
    # for i in artist_in_collection:
    #     print(i[0], end=' ')
#----------------------------------------------------------------------------------------------------------------
### Задание №4
    # artist_two_genres = cur.execute("""select album.name, count(genres.name) 
    #                 FROM album
    #                 JOIN ArtistAlbum on Album.id = ArtistAlbum.albumid
    #                 JOIN Artist on ArtistAlbum.albumid = Artist.id
    #                 JOIN ArtistGenre on Artist.id = ArtistGenre.artistid
    #                 JOIN GenreS on GenreS.id = ArtistGenre.artistid 
    #                 GROUP BY album.name 
    #                 having count(genres.name) > 1""")
    # artist_two_genres = cur.fetchall()
    # print('Названия альбомов, в которых присутствуют исполнители более чем одного жанра: ', end='')
    # for i in artist_two_genres:
    #     print(f'{i[0]} = {i[1]}. ', end='')
#----------------------------------------------------------------------------------------------------------------
    # track_out_collection = cur.execute("""select track.name 
    #                 from Track
    #                 left join CollectionTrack on Track.id = CollectionTrack.trackid
    #                 where collectiontrack.collectionid is null""")                        
    # track_out_collection = cur.fetchall()
    # print('Наименования треков, которые не входят в сборники: ', end='')
    # for i in track_out_collection:
    #            print(f'{i[0]}. ', end='')
#---------------------------------------------------------------------------------------------------------------
    cur.execute("""select artist.name, track.duration from Track
                join Album on Track.albumid = Album.id
                join ArtistAlbum on ArtistAlbum.albumid = Album.id
                join Artist on ArtistAlbum.artistid = Artist.id
                where track.duration = (select min(track.duration) from track)
                
                """)
    the_shortest_track = cur.fetchall()
    print('Исполнитель или исполнители, написавшие самый короткий по продолжительности трек: ', end='')   
    for i in the_shortest_track:
        for s in i:
            print(f'{s} ', end='')
#---------------------------------------------------------------------------------------------------------------
    # smallest_album = cur.execute("""SELECT album.name, COUNT(track.name) track_count FROM album 
    #             JOIN track ON album.id = track.albumid
    #             GROUP BY album.id
    #             HAVING COUNT(track.name) = (  
	#             SELECT COUNT(track.name) FROM album
	#             JOIN track ON album.id = track.albumid
	#             GROUP BY album.id
	#             ORDER BY COUNT(track.name)
	#             LIMIT 1);""")
    # smallest_album = cur.fetchone()
    # print('Названия альбомов, содержащих наименьшее количество треков: ', end='')
    # for i in smallest_album:
    #     print(f'{i}', end=' ')
   




    cur.execute("""select artist.name, track.duration from Track
                join Album on Track.albumid = Album.id
                join ArtistAlbum on ArtistAlbum.albumid = Album.id
                join Artist on ArtistAlbum.artistid = Artist.id
                where track.duration = (select min(track.duration) from track)
                
                """)
    the_shortest_track = cur.fetchall()
    print('Исполнитель или исполнители, написавшие самый короткий по продолжительности трек: ', end='')   
    for i in the_shortest_track:
        for s in i:
            print(f'{s} ', end='')


    








    conn.commit()
conn.close()