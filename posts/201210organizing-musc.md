<!--
 .. title: Organizing Music
 .. date: 2012/10/01
 .. slug:
-->

Do want to reorganize your music collection, but Amarok or other players are to
hard wired? I got this problem with LP from different artists, that would be
spread other the whole collection. So here is a little script for reorganizing
music collection, based on the database written by rhythmbox.


It tries to determine, if an album is a anthology of different artists and put this in:

> $music/<album>/$track - $artist - $album - $title.$suffix

rather than albums from one artists:

> $music/&lt;artist&gt;/<album>/$track - $artist - $album - $title.$suffix

Feel free to modify. This version do not copy or move the files. It creates hard links.

    #!/usr/bin/python3
    # -*- encoding: utf-8 -*- 

    __author__  = "Alexander Weigl <alexweigl@gmail.com>"

    __license__ = "cc-by-sa 3.0"
    __date__    = "2012-10-02"

    import os , os.path
    import sys

    from string import Template
    from urllib.parse import unquote
    from lxml import etree

    PREFIX = "file://"
    RHYTHMDB = os.path.expanduser("~/.local/share/rhythmbox/rhythmdb.xml")
    MUSIC_PATH = os.path.expanduser("~/tmp/musc")
    TEMPLATE = Template("$track - $artist - $album - $title.$suffix")
    VERBOSE = True

    def mkdir(p):
    """
        save wrapper for os.mkdir
    """
    try: 
        os.makedirs(p)
    except OSError as e:
    print(e)
	return

	COUNTER = 0

	def link(old,new):
	"wrapper for os.link"
	global COUNTER
	try:
	if VERBOSE: print("Link '%s' to '%s'" %( old, new)) 
			os.link(old,new)
			COUNTER += 1
	except OSError as e:
	#print(e)
	pass


	def entry_to_dict(lis):
	"translate an enty from rhymthmdb to a dictionary"
		d = {}
	for ele in lis:
			d[ele.tag] = ele.text

		d['album'] = "Unbekannt " if d['album'] in (None, "") else d['album']
		d['file'] = unquote( d['location'][len(PREFIX):] )
		d['track'] = "%02d" % int(d.get('track-number',0)) #for templating
		d['suffix'] = d['file'][-3:]
	return d

	def format_song(s):
	"return the filename for the given song"
	return TEMPLATE.substitute(**s)

	def handleCollection(album, songs):
	"handle the complete collection"
		albumRoot = os.path.join(MUSIC_PATH, album)
		mkdir(albumRoot)
	for s in songs:
			new  =   os.path.join(albumRoot, format_song(s))
			old  =   s["file"]        
			link(old,new)


	def handleNormalAlbum(album,songs):
	    "handle the complete album"
		artist = songs[0]["artist"]
		albumRoot = os.path.join(MUSIC_PATH, artist, album)
		mkdir(albumRoot)
        for s in songs:
			new  =   os.path.join(albumRoot, format_song(s))
			old  =   s["file"]
			link(old,new)

	def is_collection(songs):
        "True iff. the songs belong to a collection iff. the artists are different"
		artists = [s["artist"] for s in songs]
        for i in range(len(artists)-1):
            if artists[i] != artists[i+1]:
                return True
        return False


	print("Reading %s" % RHYTHMDB)
	tree = etree.parse(RHYTHMDB)

	ALBUM = dict()

	#build up album index
	for entry in tree.getroot().getchildren():
		song = entry_to_dict(entry)
	try:
			ALBUM[song["album"]].append( song )
	except KeyError:
			ALBUM[song["album"]] = [ song ]


	mkdir(MUSIC_PATH)

	#for each album, handle it appropriate
	for k in list(ALBUM.keys()):
		songs = ALBUM[k]
	if is_collection(songs):
			handleCollection(k,songs)
	else:
			handleNormalAlbum(k,songs)

	print("Linked %d files" % COUNTER)
