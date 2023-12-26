import psycopg2
artist_name = ['Агата Кристи', 'Король и Шут', 'Disturbed', 'Сплин', 'Katty Parry']

alboms = [['Опиум', '19950116'], ['Ураган', '19970310'],
          ['Тень клоуна', '20081120'],['Продавец кошмаров', '20061205'], 
          ['Believe', '20020917'], ['Indestructible', '20080603'],
          ['Сигнал Из Космоса', '20090922'], ['Обман Зрения', '20121008'],
          ['Katy Hudson', '20010306'], ['One of the Boys', '20080617']]

track = [['Чёрная луна', '00:03:58', 1], ['Сказочная тайга', '00:02:55', 1], ['Вечная любовь', '00:03:36', 1], ['Опиум для никого', '00:04:12', 1],
        ['Два корабля', '00:04:30', 2], ['Ураган', '00:03:56', 2], ['Грязь', '00:03:36', 2], ['Извращение', '00:05:30', 2],
        ['Тень 6 — Фред', '00:03:21', 3], ['Тень 14 — Клеймённый огнём', '00:04:36', 3], ['Тень 2 — Дагон', '00:02:17', 3], ['Тень 8 — Кода', '00:03:54', 3],
        ['Марионетки', '00:03:36', 4], ['Гробовщик', '00:03:55', 4], ['Отражение', '00:05:32', 4], ['Джокер', '00:03:16', 4],
        ['Prayer', '00:03:41', 5], ['Awaken', '00:04:29', 5], ['Devour', '00:03:52', 5], ['Intoxication', '00:03:14', 5],
        ['Indestructible', '00:04:38', 6], ['Deceiver', '00:03:49', 6], ['Enough', '00:04:20', 6], ['Criminal', '00:04:16', 6],
        ['Настройка звука', '00:02:40', 7], ['Вниз головой', '00:03:05', 7], ['Без тормозов', '00:03:14', 7], ['Всё так странно', '00:02:03', 7],
        ['Увертюра', '00:01:43', 8], ['Лестница', '00:02:18', 8], ['Дочь самурая', '00:03:36', 8], ['Чудак', '00:02:29', 8],
        ['Trust in Me', '00:04:46', 9], ['Search Me', '00:05:00', 9], ['My Own Monster', '00:05:25', 9],
        ['One of the Boys', '00:04:07', 10], ['Mannequin', '00:03:17', 10], ['Lost', '00:04:16', 10], ['Fingerprints', '00:03:44', 10]]

genre = ['punk-rock', 'horror-punk', 'gothic-rock',
        'art-rock',  'New wave', 'Alternative metal',
        'nu-metal', 'hard-rock', 'Folk rock', 'post-punk',
        'psychedelic rock', 'pop rock', 'electronic dance pop music']



conn = psycopg2.connect(database = 'mybd', user = 'postgres', password = 'psql1488')
with conn.cursor() as cur:

    
    id_num = 0
    for artists in artist_name:
        id_num += 1
        cur.execute(f"""INSERT INTO Artist (Id, Name) 
                   VALUES ('{id_num}', '{artists}') 
                   ON CONFLICT DO NOTHING""");
    
    cur.execute('''DELETE FROM Album''');



    id_num = 0
    for alb in alboms:
        id_num+=1
        cur.execute(f'''INSERT INTO Album (Id, Name, ReleaseAlbum)
                    VALUES ('{id_num}', '{alb[0]}', '{alb[1]}')
                    ON CONFLICT DO NOTHING''');

    id_num = 0
    for tracks in track:
        id_num+=1
        cur.execute(f'''INSERT INTO Track (Id, Name, Duration, AlbumId)
                    VALUES ('{id_num}', '{tracks[0]}', '{tracks[1]}', '{tracks[2]}')
                    ON CONFLICT DO NOTHING''');
    
    id_num = 0
    for genres in genre:
        id_num+=1
        cur.execute(f'''INSERT INTO Genres (Id, Name)
                    VALUES ('{id_num}', '{genres}')
                    ON CONFLICT DO NOTHING''');        

    
    
    
    cur.execute(f'''INSERT INTO ArtistGenre (ArtistId, GenreId)
                VALUES (1, 4),
                (1, 10),
                (2, 1),
                (2, 2),
                (3, 6),
                (3, 7),
                (4, 9),
                (4, 12),
                (5, 12),
                (5, 13)
                ON CONFLICT DO NOTHING''');

   
    cur.execute(f'''INSERT INTO ArtistAlbum (ArtistId, AlbumId)
                VALUES (1, 1),
                (1, 2),
                (2, 3),
                (2, 4),
                (3, 5),
                (3, 6),
                (4, 7),
                (4, 8),
                (5, 9),
                (5, 10)
                ON CONFLICT DO NOTHING''');

    cur.execute(f'''INSERT INTO Collection (Id, Name, ReleaseAlbum)
                VALUES (1, 'collection_1', '20220115'),
                (2, 'collection_2', '20160322'),
                (3, 'collection_3', '20111003'),
                (4, 'collection_4', '20210506'),
                (5, 'collection_5', '20231121')
                ON CONFLICT DO NOTHING''');                

    cur.execute(f'''INSERT INTO CollectionTrack (CollectionId, TrackId)
                VALUES (1, 2),
                (1, 4),
                (2, 5),
                (2, 3),
                (3, 12),
                (3, 22),
                (4, 40),
                (4, 32),
                (5, 19),
                (5, 27)            
                ON CONFLICT DO NOTHING''');                
    

    conn.commit()

conn.close()       
    
    
    
