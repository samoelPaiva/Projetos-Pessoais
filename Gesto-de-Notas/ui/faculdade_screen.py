import tkinter as tk
from data.data_manager import carregar_dados, salvar_dados
from logic.faculdade_logic import status_universitario, objetivo_ou_final
from ui.splash_screen import show_transition
from tkinter import messagebox

def criar_tela_faculdade(janela, COLORS, app_manager):
    frame = tk.Frame(janela, bg=COLORS['bg_primary'])
    frame.grid(row=0, column=0, sticky='nsew')

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    main_container = tk.Frame(frame, bg=COLORS['bg_primary'])
    main_container.grid(row=0, column=0, sticky='nsew')

    main_container.grid_rowconfigure(0, weight=1)
    main_container.grid_rowconfigure(1, weight=4)
    main_container.grid_rowconfigure(2, weight=1)
    main_container.grid_columnconfigure(0, weight=1)

    header = tk.Frame(main_container, bg=COLORS['card_bg'])
    header.grid(row=0, column=0, sticky='ew', padx=40, pady=(30, 15))
    header.grid_columnconfigure(0, weight=1)

    tk.Frame(header, bg=COLORS['text_primary'], height=2).grid(row=0, column=0, sticky='ew')

    tk.Label(
        header,
        text="🎓 Planejador Universitário",
        bg=COLORS['card_bg'],
        fg=COLORS['text_primary'],
        font=('Segoe UI', 22, 'bold')
    ).grid(row=1, column=0, pady=(15, 5))

    tk.Label(
        header,
        text="Planeje, cadastre e gerencie suas notas da faculdade",
        bg=COLORS['card_bg'],
        fg=COLORS['text_secondary'],
        font=('Segoe UI', 11),
        justify='center'
    ).grid(row=2, column=0, pady=(0, 15))

    tk.Frame(header, bg=COLORS['text_primary'], height=2).grid(row=3, column=0, sticky='ew')

    card = tk.Frame(main_container, bg=COLORS['card_bg'])
    card.grid(row=1, column=0, sticky='nsew', padx=40, pady=10)

    tk.Frame(card, bg=COLORS['text_primary'], height=2).grid(row=0, column=0, sticky='ew')
    tk.Frame(card, bg=COLORS['text_primary'], height=2).grid(row=2, column=0, sticky='ew')

    card.grid_rowconfigure(1, weight=1)
    card.grid_columnconfigure(0, weight=1)

    inner = tk.Frame(card, bg=COLORS['card_bg'])
    inner.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

    inner.grid_rowconfigure(1, weight=1)
    inner.grid_columnconfigure(0, weight=1)

    buttons_wrapper = tk.Frame(inner, bg=COLORS['card_bg'])
    buttons_wrapper.grid(row=0, column=0, pady=10)

    buttons_wrapper.grid_columnconfigure(0, weight=1)
    buttons_wrapper.grid_columnconfigure(1, weight=1)

    def criar_botao(texto, comando, row, col):
        btn = tk.Label(
            buttons_wrapper,
            text=texto,
            bg="#E0E0E0",
            fg=COLORS['bg_primary'],
            font=('Segoe UI', 11, 'bold'),
            width=20,
            height=2,
            cursor='hand2'
        )
        btn.grid(row=row, column=col, padx=10, pady=10)

        def on_enter(e):
            btn.config(bg="#D5D5D5")

        def on_leave(e):
            btn.config(bg="#E0E0E0")

        def on_click(e):
            comando()

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.bind("<Button-1>", on_click)

    tabela_container = tk.Frame(inner, bg=COLORS['card_bg'])
    tabela_container.grid(row=1, column=0, sticky='nsew')

    def renderizar():
        for widget in tabela_container.winfo_children():
            widget.destroy()
        for i in range(10):
            tabela_container.grid_rowconfigure(i, weight=1)

        dados = carregar_dados()

        tabela_container.grid_columnconfigure(0, weight=2)
        tabela_container.grid_columnconfigure(1, weight=2)
        tabela_container.grid_columnconfigure(2, weight=2)
        tabela_container.grid_columnconfigure(3, weight=2)

        headers = ["Matéria", "Notas", "Status", "Média ou Objetivo"]

        for col, text in enumerate(headers):
            tk.Label(
                tabela_container,
                text=text,
                bg=COLORS['card_bg'],
                fg=COLORS['text_primary'],
                relief="solid",
                bd=1,
                anchor='center'
            ).grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

        for i, disc in enumerate(dados["faculdade"]):
            row_index = i + 1

            tk.Label(
                tabela_container,
                text=disc['disciplina'],
                bg=COLORS['card_bg'],
                fg=COLORS['text_primary'],
                relief="solid",
                bd=1,
                anchor='w',
                wraplength=120
            ).grid(row=row_index, column=0, sticky="nsew", padx=1, pady=1)

            notas_texto = "  ".join(str(n) for n in disc['notas'])

            tk.Label(
                tabela_container,
                text=notas_texto if notas_texto else "-",
                bg=COLORS['bg_secondary'],
                fg=COLORS['text_primary'],
                relief="solid",
                bd=1,
                anchor='center'
            ).grid(row=row_index, column=1, sticky="nsew", padx=1, pady=1)

            status = status_universitario(disc['notas'])

            tk.Label(
                tabela_container,
                text=status,
                bg=COLORS['card_bg'],
                fg=COLORS['text_secondary'],
                relief="solid",
                bd=1,
                anchor='center'
            ).grid(row=row_index, column=2, sticky="nsew", padx=1, pady=1)

            obj = objetivo_ou_final(disc['notas'])

            texto = ""
            for k, v in obj.items():
                if isinstance(v, float):
                    v = round(v, 2)
                texto = f"{k}: {v}"

            tk.Label(
                tabela_container,
                text=texto,
                bg=COLORS['card_bg'],
                fg=COLORS['text_secondary'],
                relief="solid",
                bd=1,
                anchor='center',
                wraplength=150
            ).grid(row=row_index, column=3, sticky="nsew", padx=1, pady=1)

    def abrir_remocao():
        popup = tk.Toplevel(janela)
        popup.title("Remover Disciplina")
        popup.geometry("350x500")
        popup.configure(bg=COLORS['bg_primary'])

        tk.Label(
            popup,
            text="Selecione a disciplina",
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 12, 'bold')
        ).pack(pady=10)

        dados = carregar_dados()

        container_lista = tk.Frame(popup, bg=COLORS['bg_primary'])
        container_lista.pack(expand=True, fill='both')

        lista = tk.Listbox(
            container_lista,
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 11),
            selectbackground="#555",
            relief="flat",
            highlightthickness=0,
            justify='center'
        )

        lista.pack(padx=20, pady=10, ipadx=10, ipady=5, expand=True, fill='both')

        for disc in dados["faculdade"]:
            lista.insert(tk.END, disc['disciplina'])

        for i in range(lista.size()):
            lista.itemconfig(i, {'bg': COLORS['card_bg']})

        def remover():
            selecionado = lista.curselection()

            if not selecionado:
                messagebox.showerror("Erro", "Selecione uma disciplina")
                return

            index = selecionado[0]

            confirmar = messagebox.askyesno("Confirmar", "Deseja remover?")

            if not confirmar:
                return

            del dados["faculdade"][index]
            salvar_dados(dados)

            popup.destroy()
            renderizar()

        botoes_frame = tk.Frame(popup, bg=COLORS['bg_primary'])
        botoes_frame.pack(pady=10)

        inner_frame = tk.Frame(botoes_frame, bg=COLORS['bg_primary'])
        inner_frame.pack()

        tk.Button(
            inner_frame,
            text="⬅ Voltar",
            command=popup.destroy,
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2'
        ).pack(side='left', pady=10)

        tk.Button(
            inner_frame,
            text="🗑 Remover",
            command=remover,
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2'
        ).pack(side='right', pady=10)

    def abrir_edicao():
        popup = tk.Toplevel(janela)
        popup.title("Selecionar disciplina")
        popup.geometry("350x500")
        popup.configure(bg=COLORS['bg_primary'])

        tk.Label(
            popup,
            text="Selecione a disciplina",
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 12, 'bold')
        ).pack(pady=10)

        dados = carregar_dados()

        container_lista = tk.Frame(popup, bg=COLORS['bg_primary'])
        container_lista.pack(expand=True, fill='both')

        lista = tk.Listbox(
            container_lista,
            bg=COLORS['card_bg'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 11),
            selectbackground="#555",
            relief="flat",
            highlightthickness=0,
            justify='center'
        )
        lista.pack(padx=20, pady=10, ipadx=10, ipady=5, expand=True, fill='both')

        for disc in dados["faculdade"]:
            lista.insert(tk.END, disc['disciplina'])

        for i in range(lista.size()):
            lista.itemconfig(i, {'bg': COLORS['card_bg']})

        def continuar():
            selecionado = lista.curselection()

            if not selecionado:
                messagebox.showerror("Erro", "Selecione uma disciplina")
                return

            index = selecionado[0]
            popup.destroy()
            abrir_form_edicao(index)

        botoes_frame = tk.Frame(popup, bg=COLORS['bg_primary'])
        botoes_frame.pack(pady=10)

        inner_frame = tk.Frame(botoes_frame, bg=COLORS['bg_primary'])
        inner_frame.pack()

        tk.Button(
            inner_frame,
            text="⬅ Voltar",
            command=popup.destroy,
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2'
        ).pack(side='left', pady=10)

        tk.Button(
            inner_frame,
            text="✏ Editar",
            command=continuar,
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2'
        ).pack(side='right', pady=10)

    def abrir_form_edicao(index):
        dados = carregar_dados()
        disc = dados["faculdade"][index]

        popup = tk.Toplevel(janela)
        popup.title("Editar Disciplina")
        popup.geometry("350x500")
        popup.configure(bg=COLORS['bg_primary'])

        tk.Label(
            popup,
            text="Editar disciplina",
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 12, 'bold')
        ).pack(pady=10)

        entry_nome = tk.Entry(popup, justify='center')
        entry_nome.pack(pady=10)
        entry_nome.insert(0, disc["disciplina"])

        entradas_notas = []

        notas_frame = tk.Frame(popup, bg=COLORS['bg_primary'])
        notas_frame.pack(pady=10)

        for i in range(3):
            entry = tk.Entry(notas_frame, width=8, justify='center')
            entry.grid(row=0, column=i, padx=5)

            if i < len(disc["notas"]):
                entry.insert(0, disc["notas"][i])

            entradas_notas.append(entry)

        def salvar():
            nome = entry_nome.get().strip()

            if not nome:
                messagebox.showerror("Erro", "Digite o nome")
                return

            notas = []
            for e in entradas_notas:
                valor = e.get().strip()
                if valor:
                    try:
                        notas.append(float(valor.replace(",", ".")))
                    except:
                        messagebox.showerror("Erro", "Nota inválida")
                        return

            dados["faculdade"][index] = {
                "disciplina": nome,
                "notas": notas
            }

            salvar_dados(dados)

            popup.destroy()
            renderizar()

        tk.Button(
            popup,
            text="💾 Salvar",
            command=salvar,
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary'],
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2'
        ).pack(pady=15)

    def voltar_menu():
        show_transition(janela=janela, callback=app_manager.mostrar_menu)

    def cadastrar_disciplina():
        show_transition(janela, app_manager.mostrar_cadastro_disciplina_faculdade)

    criar_botao("Cadastrar disciplina", cadastrar_disciplina, 0, 0)
    criar_botao("Remover disciplina", abrir_remocao, 0, 1)
    criar_botao("Adicionar/Editar nota", abrir_edicao, 1, 0)
    criar_botao("⬅ Voltar ao menu", voltar_menu, 1, 1)

    frame.renderizar = renderizar
    renderizar()

    return frame