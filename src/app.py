from interface import *

registroUsuario = {
    'user': 'Luan',
    'psw': '123#'
}

class LoginFunctions():

    def getCredentials(self):
        user = str(self.user_textbox.get())
        psw = str(self.senha_textbox.get())
        credentialis = {
            'user': user,
            'psw':psw
        }
        return credentialis

    def login(self):
        credentials = self.getCredentials()
        if credentials == registroUsuario:
            print(credentials)

        else:
            print('erro')

        # if(user)

def main():
    LoginGUI()

if __name__ == '__main__':
    main()