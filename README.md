"""
    DECAPTCHER API
    	SUBMIT IMAGES TO THE DECAPTCHER API TO OBTAIN A RESPONSE
	FROM THE IMAGE SUBMITTED.

"""

---Requirements---
requests

API using requests package for making http requests with the 
        Decaptcher API


--- example ---
```python
from decaptcher_api import decaptcher
import requests

the_user = "a_user"
the_passwd = "a_password"
#SET SOME URL TO DOWNLOAD AN IMAGE IF YOU DONT HAVE ONE TO TEST.
the_image_url = "https://some_captcha_url"
#THE PATH IN CASE YOU WANT 
captcha_path = "file_path"

#Download and save an image from a url
def save_captcha(url, file_path):
    response = requests.get(url)
    with open(file_path, "wb+") as f:
	for chunk in response:
		f.write(chunk)

#USE IF YOU WANT TO DOWNLOAD THE PREVIOUS DEFINED URL
save_captcha(the_image_url, captcha_path)

#LOGIN, SENDS THE CAPTCHA TO THE SERVICE AND CHECKS THE RESPONSE...
decaptcherapi = decaptcher.Decaptcher(the_user, the_passwd)
decaptcherapi.get_captcha_response(captcha_path)
response_captcha = decaptcherapi.parse_response()
print response_captcha
```



