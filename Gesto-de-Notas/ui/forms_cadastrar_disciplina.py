import tkinter as tk
from data.data_manager import carregar_dados, salvar_dados
from ui.splash_screen import show_transition
from tkinter import messagebox

def criar_tela_cadastro_disciplina(janela, COLORS, app_manager):
    frame = tk.Frame(janela, bg=COLORS['bg_primary'])
    frame.grid(row=0, column=0, sticky='nsew')

    frame.grid_columnconfigure(0, weight=1)

    # ================= HEADER =================
    header = tk.Frame(frame, bg=COLORS['card_bg'])
    header.grid(row=0, column=0, sticky='ew', padx=40, pady=(30, 10))
    header.grid_columnconfigure(0, weight=1)

    tk.Frame(header, bg=COLORS['text_primary'], height=2).grid(row=0, column=0, sticky='ew')

    tk.Label(
        header,
        text="📚 Cadastrar Disciplina",
        bg=COLORS['card_bg'],
        fg=COLORS['text_primary'],
        font=('Segoe UI', 22, 'bold')
    ).grid(row=1, column=0, pady=(15, 5))

    tk.Label(
        header,
        text="Insira o nome da disciplina e as notas",
        bg=COLORS['card_bg'],
        fg=COLORS['text_secondary'],
        font=('Segoe UI', 11)
    ).grid(row=2, column=0, pady=(0, 15))

    tk.Frame(header, bg=COLORS['text_primary'], height=2).grid(row=3, column=0, sticky='ew')

    # ================= CONTAINER =================
    container = tk.Frame(frame, bg=COLORS['card_bg'])
    container.grid(row=1, column=0, sticky='nsew', padx=40, pady=10)
    container.grid_columnconfigure(0, weight=1)

    # Nome disciplina
    tk.Label(
        container,
        text="Nome da disciplina",
        bg=COLORS['card_bg'],
        fg=COLORS['text_primary'],
        font=('Segoe UI', 11, 'bold')
    ).grid(row=0, column=0, pady=(10, 5))

    entry_nome = tk.Entry(container, font=('Segoe UI', 12), justify='center')
    entry_nome.grid(row=1, column=0, pady=(0, 15))

    # Notas
    notas_frame = tk.Frame(container, bg=COLORS['card_bg'])
    notas_frame.grid(row=2, column=0, pady=10)

    entradas_notas = []

    for i in range(4):
        tk.Label(
            notas_frame,
            text=f"{i+1}º Bim",
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary']
        ).grid(row=0, column=i, padx=10)

        entry = tk.Entry(notas_frame, width=8, justify='center')
        entry.grid(row=1, column=i, padx=10, pady=5)

        entradas_notas.append(entry)

    # ================= FUNÇÕES =================
    def receber_nota(entry):
        texto = entry.get().strip()

        if texto == "":
            return None

        try:
            nota = float(texto.replace(",", "."))
            if nota < 0 or nota > 10:
                raise ValueError
            return nota
        except:
            messagebox.showerror("Erro", "Nota inválida (0 a 10)")
            return None

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        for entry in entradas_notas:
            entry.delete(0, tk.END)

    def salvar():
        nome = entry_nome.get().strip()

        if not nome:
            messagebox.showerror("Erro", "Digite o nome da disciplina")
            return

        notas = []

        for entry in entradas_notas:
            nota = receber_nota(entry)
            if entry.get().strip() != "" and nota is None:
                return
            if nota is not None:
                notas.append(nota)

        dados = carregar_dados()

        dados["escola"].append({
            "disciplina": nome,
            "notas": notas
        })

        salvar_dados(dados)

        limpar_campos()

        janela.after(100, lambda: show_transition(janela, app_manager.mostrar_med_escolar))

    def voltar():
        limpar_campos()
        janela.after(100, lambda: show_transition(janela, app_manager.mostrar_med_escolar))

    # ================= BOTÕES =================
    botoes = tk.Frame(container, bg=COLORS['card_bg'])
    botoes.grid(row=3, column=0, pady=20)

    tk.Button(
        botoes,
        text="💾 Salvar",
        command=salvar,
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary'],
        font=('Segoe UI', 10, 'bold'),
        cursor='hand2'
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        botoes,
        text="◀ Voltar",
        command=voltar,
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary'],
        font=('Segoe UI', 10, 'bold'),
        cursor='hand2'
    ).grid(row=0, column=1, padx=10)

    return frame