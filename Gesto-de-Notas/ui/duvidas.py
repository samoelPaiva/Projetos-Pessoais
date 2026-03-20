import tkinter as tk

from ui.splash_screen import show_transition

def criar_tela_duvida(janela, COLORS, app_manager):
    frame_duvida = tk.Frame(janela, bg=COLORS['bg_primary'])
    frame_duvida.grid(row=0, column=0, sticky='nsew')

    frame_duvida.grid_rowconfigure(0, weight=1)
    frame_duvida.grid_columnconfigure(0, weight=1)

    main_container = tk.Frame(frame_duvida, bg=COLORS['bg_primary'])
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
        text="📋 Dúvidas Frequentes",
        bg=COLORS['card_bg'],
        fg=COLORS['text_primary'],
        font=('Segoe UI', 22, 'bold')
    ).grid(row=1, column=0, pady=(15, 5))

    tk.Label(
        header,
        text="Aqui você encontra respostas rápidas para suas dúvidas sobre o aplicativo",
        bg=COLORS['card_bg'],
        fg=COLORS['text_secondary'],
        font=('Segoe UI', 11),
        justify='center',
        wraplength=500
    ).grid(row=2, column=0, pady=(0, 15))

    tk.Frame(header, bg=COLORS['text_primary'], height=2).grid(row=3, column=0, sticky='ew')

    card = tk.Frame(main_container, bg=COLORS['card_bg'])
    card.grid(row=1, column=0, sticky='nsew', padx=40, pady=10)
    card.grid_rowconfigure(0, weight=1)
    card.grid_columnconfigure(0, weight=1)

    inner = tk.Frame(card, bg=COLORS['card_bg'])
    inner.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)
    inner.grid_columnconfigure(0, weight=1)

    duvidas = [
        {
            "pergunta": "Por que o aplicativo não tem uma quarta prova ou recuperação?",
            "resposta": "Acreditamos no potencial dos alunos, então focamos no planejamento de notas e feedback rápido e pratico."
        },
        {
            "pergunta": "Como faço para adicionar ou editar minhas disciplinas?",
            "resposta": "Escolha o modo escolar ou faculdade, e selecione a opção clicando nos botões e preenchendo o que se pede!."
        },
        {
            "pergunta": "Posso simular diferentes cenários de notas?",
            "resposta": "Sim! Use os modos Escolar ou Faculdade para testar diferentes médias e objetivos."
        },
        {
            "pergunta": "Posso cadrastrar uma disciplina sem notas?",
            "resposta": "Sim, e fique atento ao objetivo indicado nela!"
        }
    ]

    def toggle_resposta(frame_resposta):
        if frame_resposta.winfo_viewable():
            frame_resposta.grid_remove()
        else:
            frame_resposta.grid()

    for i, item in enumerate(duvidas):
        faq_frame = tk.Frame(inner, bg=COLORS['bg_secondary'], bd=1, relief='solid')
        faq_frame.pack(fill='x', pady=5)

        pergunta_btn = tk.Button(
            faq_frame,
            text=item["pergunta"],
            font=('Segoe UI', 11, 'bold'),
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_primary'],
            bd=0,
            relief='flat',
            anchor='w',
            cursor='hand2',
            wraplength=500,
            justify='left'
        )
        pergunta_btn.pack(fill='x', padx=10, pady=5)

        resposta_frame = tk.Frame(faq_frame, bg=COLORS['bg_secondary'])
        resposta_frame.pack(fill='x', padx=10)
        resposta_label = tk.Label(
            resposta_frame,
            text=item["resposta"],
            font=('Segoe UI', 10),
            bg=COLORS['bg_secondary'],
            fg=COLORS['text_secondary'],
            wraplength=480,
            justify='left'
        )
        resposta_label.pack(fill='x', pady=(0,5))
        resposta_frame.grid_remove()  

        pergunta_btn.config(command=lambda f=resposta_frame: toggle_resposta(f))

    
    botoes_frame = tk.Frame(inner, bg=COLORS['card_bg'])
    botoes_frame.pack(pady=15)

    def voltar_menu():
            show_transition(janela=janela, callback=app_manager.mostrar_menu)

    tk.Button(
        botoes_frame,
        text="⬅ Voltar",
        command=voltar_menu,
        bg=COLORS['bg_secondary'],
        fg=COLORS['text_primary'],
        font=('Segoe UI', 10, 'bold'),
        cursor='hand2',
        width=12
    ).pack()

    return frame_duvida