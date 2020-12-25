import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE DWH_STAGE_EVENT_TBL;"
staging_songs_table_drop = "DROP TABLE DWH_STAGE_SONGS_TBL;"
songplay_table_drop = "DROP TABLE DWH_SONGPLAY_TBL;"
user_table_drop = "DROP TABLE DWH_USERS_TBL;"
song_table_drop = "DROP TABLE DWH_SONG_TBL;"
artist_table_drop = "DROP TABLE DWH_ARTIST_TBL;"
time_table_drop = "DROP TABLE DWH_TIME_TBL;"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS DWH_STAGE_EVENT_TBL
(
    artist text,
    auth text,
    firstName text,
    gender char(1),
    iteminSession smallint,
    lastName text,
    length numeric,
    level text,
    location text,
    method text,
    page text,
    registration numeric,
    sessionId smallint,
    song text,
    status smallint,
    ts bigint
    userAgent text,
    userId integer
)
""")

staging_songs_table_create = ("""
""")

songplay_table_create = ("""
""")

user_table_create = ("""
""")

song_table_create = ("""
""")

artist_table_create = ("""
""")

time_table_create = ("""
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
