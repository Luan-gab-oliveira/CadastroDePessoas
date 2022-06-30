from modules import *
from app import LoginFunctions
get_dir = os.path.dirname(__file__)

palette = {
    'cor1': '#017f74',
    'cor2': '#158ca2',
    'cor3': '#A3A5A5',
    'cor4': '#23395b',
    'cor5': '#ffffff',
}

icon = {
    'login': f'{get_dir}\images\\personal.ico',
    'system': f'{get_dir}\images\\people.ico',
}


def geometry_root(root, width, height):
    width_screnn = root.winfo_screenwidth()
    height_screnn = root.winfo_screenheight()
    pos_x = width_screnn/2 - width/2
    pos_y = height_screnn/2 - height/2
    geometry_root = '%dx%d+%d+%d' % (width,height,pos_x,pos_y)
    return geometry_root
    
# Criação da tela de login
class LoginGUI(LoginFunctions):
    def __init__(self):
        self.root = tk.Tk()
        self.make_root()
        self.widhts()
        self.root.mainloop()

    def make_root(self):
        self.root.title('Login - Cadastro')
        self.root.iconbitmap(default=  icon['login'])
        #  icon['login'])
        self.root.geometry(geometry_root(self.root,300,350))
        self.root.resizable(False, False)
        self.root.config(background=palette['cor5'])
    
    def widhts(self):
        self.label = Label(self.root, text='Usuário')
        self.label.config(
            font=('Helvetica', 14),
            background=palette['cor5'],
            anchor='nw'
        )
        self.label.place(relx=0.1, rely=0.14, relwidth=0.8)

        #campo usuário
        self.user_textbox = Entry(self.root,highlightthickness=2)
        self.user_textbox.config(
            font=('Helvetica', 14), justify='left',
            background=palette['cor5'], bd=2,
            relief='flat',
            highlightbackground=palette['cor3'], highlightcolor=palette['cor3']
            )
        self.user_textbox.place(relx=0.1, rely=0.24, relwidth=0.8)

        self.label = Label(self.root, text='Senha')
        self.label.config(
            font=('Helvetica', 14),
            background=palette['cor5'],
            anchor='nw'
        )
        self.label.place(relx=0.1, rely=0.4, relwidth=0.8)

        # campo senha
        self.senha_textbox = Entry(self.root,highlightthickness=2)
        self.senha_textbox.config(
            textvariable=StringVar(),show='*',
            font=('Helvetica', 14), justify='left',
            background=palette['cor5'], bd=2,
            relief='flat',
            highlightbackground=palette['cor3'], highlightcolor=palette['cor3']
            )
        self.senha_textbox.place(relx=0.1, rely=0.5, relwidth=0.8)

        # button login
        self.button_continue = Button(self.root, text='Continuar')
        self.button_continue.config(
            font=('Helvetica', 14), justify='center',foreground=palette['cor5'],
            background=palette['cor4'], bd=0,
            cursor='hand2',
            highlightbackground=palette['cor3'], highlightcolor=palette['cor3'], activebackground=palette['cor3'], 
            highlightthickness=0,
            command=self.login
            )
        self.button_continue.place(relx=0.1, rely=0.7, relwidth=0.8)

class CadasdroGUI():
    def __init__(self):
        self.root = tk.Tk()  
        self.root.bind("<F11>", self.toggleFullScreen)
        self.make_root()
        self.make_frame()
        # self.widhts()
        self.root.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)

    def make_root(self):
        self.root.title('Cadastro de pessoas')
        self.root.iconbitmap(default=icon['system'])
        self.root.geometry(geometry_root(self.root,1000,600))
        # self.root.maxsize(width=width_screnn, height=height_screnn)
        self.root.minsize(width=800, height=600)
        self.root.resizable(True, True)
        self.root.config(background=palette['cor5'])
        self.fullScreenState = False

    def make_frame(self):
        self.frame1 = Frame(self.root)
        self.frame1.config(background=palette['cor2'])
        self.frame1.place(relx=0,rely=0,relwidth=1,relheight=.3)
