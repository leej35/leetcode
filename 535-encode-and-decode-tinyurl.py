class Codec:
    def __init__(self):
        self.map={}
        self.mapid={}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if self.map.has_key(longUrl):
            return self.map[longUrl]
        else:
            shortUrl = str(len(self.map.keys()))
            self.map[longUrl] = shortUrl
            self.mapid[shortUrl] = longUrl
            return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if self.mapid.has_key(shortUrl):
            return self.mapid[shortUrl]
        else:
            return 'NOT FOUND.'

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
