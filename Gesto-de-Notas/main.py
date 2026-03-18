import tkinter as tk
from ui.menu import criar_menu
from ui.escolar_screen import criar_tela_escolar
from ui.faculdade_screen import criar_tela_faculdade
from ui.forms_cadastrar_disciplina import criar_tela_cadastro_disciplina
from ui.forms_cadastrar_dis_faculdade import criar_tela_cadastro_disciplina_faculdade
from ui.duvidas import criar_tela_duvida

COLORS = {
    'bg_primary': '#121212',
    'bg_secondary': '#1e1e1e',
    'card_bg': '#1f1f1f',
    'text_primary': '#ffffff',
    'text_secondary': '#aaaaaa',
}

class AppManager:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Gestor de Notas Acadêmicas')
        self.janela.geometry('700x700')
        self.janela.configure(bg=COLORS['bg_primary'])

  
        self.janela.grid_rowconfigure(0, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)


        self.frame_menu = criar_menu(self.janela, COLORS, self) 
        self.frame_escolar = criar_tela_escolar(self.janela, COLORS, self)
        self.frame_faculdade = criar_tela_faculdade(self.janela, COLORS, self)
        self.frame_cadastro = criar_tela_cadastro_disciplina(self.janela, COLORS, self)
        self.frame_cadastro_faculdade = criar_tela_cadastro_disciplina_faculdade(self.janela, COLORS, self)
        self.frame_duvida = criar_tela_duvida(self.janela, COLORS, self)
        

        self.mostrar_menu()

    
    def mostrar_menu(self):
        self.esconder_todos_frames()
        self.frame_menu.grid(row=0, column=0, sticky='nsew')

    def mostrar_med_escolar(self):
        self.esconder_todos_frames()
        self.frame_escolar.grid(row=0, column=0, sticky='nsew')

        if hasattr(self.frame_escolar, "renderizar"):
                self.frame_escolar.renderizar()

    def mostrar_med_faculdade(self):
        self.esconder_todos_frames()
        self.frame_faculdade.grid(row=0, column=0, sticky='nsew')

        if hasattr(self.frame_escolar, "renderizar"):
                self.frame_faculdade.renderizar()
    
    def mostrar_cadastro_disciplina(self):
        self.esconder_todos_frames()
        self.frame_cadastro.grid(row=0, column=0, sticky='nsew')
    
    def mostrar_cadastro_disciplina_faculdade(self):
        self.esconder_todos_frames()
        self.frame_cadastro_faculdade.grid(row=0, column=0, sticky='nsew')

    def mostrar_duvidas(self):
        self.esconder_todos_frames()
        self.frame_duvida.grid(row=0, column=0, sticky='nsew')

    def esconder_todos_frames(self):
        for f in [self.frame_menu, self.frame_escolar, self.frame_faculdade, self.frame_cadastro, self.frame_cadastro_faculdade, self.frame_duvida]:
            f.grid_forget()

    def rodar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = AppManager()
    app.rodar()