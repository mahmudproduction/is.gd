import gdshortener
def is_gd(url):
	s = gdshortener.ISGDShortener()
	return s.shorten(url, log_stat = True, custom_url = 'sdlkjkalsjdlksajd')
print(is_gd('http://www.google.com'))

# import gdshortener

# s = gdshortener.ISGDShortener()
# print s.shorten('http://www.google.com')
# If you want statistic usage on a URL use:

# print s.shorten(url = 'http://www.google.com', log_stat = True)
# If you want a custom URL use:

# print s.shorten(url = 'http://www.google.com', custom_url = 'Pippus')
# If you want to ignore SSL certificate (for older version of OpenSSL):

# print s.shorten(url = 'https://expired.badssl.com', verify_ssl = False)
# If you have an already shortened URL and want a reverse lookup:

# print s.lookup('http://is.gd/Pippus')
