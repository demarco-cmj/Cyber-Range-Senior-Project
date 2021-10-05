import tornado.ioloop
import tornado.web
from os import path
import pw_generator
import settings
import jwt
from tornado_http_auth import BasicAuthMixin

#Run this code separately in terminal, and then  have the user write their client in jupyter

encoded_jwt = jwt.encode({"secret phrase": settings.phrase}, "secret", algorithm="HS256")

file = open("pw_file.txt", "r")
correct_pw = file.read()
file.close()
credentials = {'user': correct_pw}

class SensitiveDataHandler(tornado.web.RequestHandler):
    def get(self):
        correct_token = encoded_jwt
        input_token = self.get_argument("token")

        #Validate token. If successful return data
        if (input_token == correct_token):
            self.write(jwt.decode(encoded_jwt, "secret", algorithms=["HS256"]))
        else:
            self.write("403 Forbidden")

class NewLoginHandler(BasicAuthMixin, tornado.web.RequestHandler):
    #Have a login requirement pop up in the browser
    def prepare(self):
        self.get_authenticated_user(check_credentials_func=credentials.get, realm='Protect')
    
    #Give the user a 200 status code and print the token
    def get(self):
        self.write("200 OK. token=" + encoded_jwt)

def make_app():
    return tornado.web.Application([
        (r"/user/login", NewLoginHandler),
        (r"/token", SensitiveDataHandler)
    ])

if __name__ == "__main__":
    pw_generator.create_pw_list() 
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()