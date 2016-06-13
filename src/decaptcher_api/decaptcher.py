# -*- encoding: utf-8 -*-

from decaptcher_api_codes import RESPONSE_CODES, RESPONSE_TIMEOUTS
import requests


class DecaptcherAPI():
    """A class for consuming the decaptcher api\
    
    """


    def __init__(self, username, password, secure=None, claim=None):
        """Inits the class with username and password for making valid calls\

        """
        self.username = username
        self.password = password
        self.secure = False
        if secure:
            self.secure = True
        if claim:
            self.claim = True
        self.response = None
        pass


    def get_host(self):
        """Returns the host to the correct protocol according to the secure attribute\
        
        """
        if self.secure:
            return "https://poster.de-captcher.com"  
        return "http://poster.de-captcher.com"
        pass


    def set_claim(self, claim):
        """Sets the claim attribute to the paramater passed.\


        """
        self.claim = claim


    def set_secure(self , secure):
        """Sets the secure attribute to the parameter passed.\
        """
        self.secure = secure


    def add_credentials(self, data):
        """Adds the credentials to the data dict that will be send\

        """
        data["username"] = self.username
        data["password"] = self.password
        return data


    def get_captcha_response(self, file_path, question=None):
        """Sends an image and Gets the captcha response\
    
        """
        f = open(file_path, "rb+")
        host = "http://poster.de-captcher.com"
        if self.secure:
            host = "https://poster.de-captcher.com/"
        data={
            "function": "picture2",
            "pict_type": "0",
            "submit": "Send"
        }
        if question:
            data["question"] = question
        
        data = self.add_credentials(data)

        response = requests.post(
                host,
                data = data,
                files={
                        "pict": f
                }
        )
        f.close()
        self.response = response
        #os.remove(captchafile)


    def parse_response(self):
        """ Parse the response from the response attribute of the class\

        If claim is set to True and a claim applies it is submitted automatically.
        """
        if not self.response:
            return None
        self.parsed_response = self.response.text.split("|")
        response_code = int(self.parsed_response[0])
        if response_code != 0:
            if response_code == -9:
                if self.claim:
                    self.claim_bad()
            return RESPONSE_CODES[response_code]
        self.response = None
        return self.parsed_response[-1]


    def claim_bad(self):
        """Submits the data for claiming a not recognized picture.

        returns True if response had code 200, else returns False.
        """
        if not self.response:
            return None
        minor_id = self.parsed_response[2]
        major_id = self.parsed_response[1]
        function = "picture_bad2"
        data = {
            "function": function, 
            "major_id": major_id,
            "minor_id": minor_id,
            "submit": "Send"
        }
        self.add_credentials(data)
        response = request.post(
            self.get_host(),
            data,
        )
        if response.ok:
            print response.text
            return True
        return False




