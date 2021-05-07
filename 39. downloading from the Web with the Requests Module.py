# The requests module: a third-party module for downloading web pages and files/ 
import requests
res = requests.get ('https://automatetheboringstuff.com/files/rj.txt') # returns a response object
print(res.status_code) 
print(len(res.text))
print(res.text[:500])

res.raise_for_status() # raises an exception if the download failed. 
badRes = requests.get ('https://automatetheboringstuff.com/a;lksjnreivpekmxjxhoer')
print(badRes.raise_for_status)

# write-binary mode: open (filename, 'wb')
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):  # lets me to save a downloaded file to my hard drive
    playFile.write(chunk)
playFile.close()

# http://bit.ly/unipain

# More info available from https://requests.readthedocs.org/en/latest/
