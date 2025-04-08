import urllib.request
url = 'https://data.wprdc.org/api/3/action/datastore_search?resource_id=dc85da67-b32f-4408-acef-b763d08b5bf0&limit=5&q=title:jones'  
fileobj = urllib.request.urlopen(url)
print(fileobj.read())