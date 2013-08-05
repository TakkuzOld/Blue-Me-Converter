import sys
import eyeD3

tag = eyeD3.Tag()
tag.link(sys.argv[1])

print "Artista: " + tag.getArtist().encode("utf-8")
print "Album: " + tag.getAlbum().encode("utf-8")
print "Titolo: " + tag.getTitle().encode("utf-8")
print "Traccia: " + str( tag.getTrackNum()[0] ).encode("utf-8")
print "Genere: " + tag.getGenre().getName().encode("utf-8")
print "Anno: " + tag.getYear().encode("utf-8")

