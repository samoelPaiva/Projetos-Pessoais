import tkinter as tk
from ui.splash_screen import show_transition


def criar_menu(janela, COLORS, app_manager):
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
        text="📊 Gestor de Notas",
        bg=COLORS['card_bg'],
        fg=COLORS['text_primary'],
        font=('Segoe UI', 22, 'bold')
    ).grid(row=1, column=0, pady=(15, 5))

    tk.Label(
        header,
        text="Planeje suas notas e garanta a aprovação conosco",
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

    inner.grid_columnconfigure(0, weight=1)
    inner.grid_columnconfigure(1, weight=1)

    
    descricao = tk.Label(
        inner,
        text="Escolha o modo de cálculo.\nSimule resultados, entenda suas notas e descubra exatamente o que precisa para passar sem surpresas.",
        bg=COLORS['card_bg'],
        fg=COLORS['text_secondary'],
        font=('Segoe UI', 11),
        justify='center',
        wraplength=500
    )
    descricao.grid(row=0, column=0, columnspan=2, pady=(10, 10))

    
    buttons_wrapper = tk.Frame(inner, bg=COLORS['card_bg'])
    buttons_wrapper.grid(row=1, column=0, columnspan=2, pady=20)

    def abrir_escolar():
        app_manager.mostrar_med_escolar()

    def abrir_faculdade():
        app_manager.mostrar_med_faculdade()
    
    def abrir_duvidas():
        app_manager.mostrar_duvidas()

    def criar_botao(texto, comando):
        btn = tk.Label(
            buttons_wrapper,
            text=texto,
            bg="#E0E0E0",
            fg=COLORS['bg_primary'],
            font=('Segoe UI', 12, 'bold'),
            width=18,
            height=4,
            cursor='hand2'
        )
        btn.pack(side='left', padx=25)

        def on_enter(e):
            btn.config(bg="#D5D5D5")

        def on_leave(e):
            btn.config(bg="#E0E0E0")

        def on_click(e):
            show_transition(janela, comando)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.bind("<ButtonRelease-1>", on_click)

    criar_botao("📋Modo Escolar", abrir_escolar)
    criar_botao("🎓 Modo Faculdade", abrir_faculdade)

    
    buttons_duvidas = tk.Frame(inner, bg=COLORS['card_bg'])
    buttons_duvidas.grid(row=2, column=0, columnspan=2, pady=15)

    btn_duvidas = tk.Label(
        buttons_duvidas,
        text="📝 Dúvidas",
        bg="#E0E0E0",
        fg=COLORS['bg_primary'],
        font=('Segoe UI', 12, 'bold'),
        width=20,
        height=4,
        cursor='hand2'
    )
    btn_duvidas.pack()

    def on_enter(e):
        btn_duvidas.config(bg="#D5D5D5")

    def on_leave(e):
        btn_duvidas.config(bg="#E0E0E0")

    def on_click(e):
        show_transition(janela, abrir_duvidas)

    btn_duvidas.bind("<Enter>", on_enter)
    btn_duvidas.bind("<Leave>", on_leave)
    btn_duvidas.bind("<ButtonRelease-1>", on_click)

    
    tk.Label(
        main_container,
        text="Created by BakaDev\nSistema modular escalável",
        bg=COLORS['bg_primary'],
        fg=COLORS['text_secondary'],
        font=('Consolas', 10, 'bold'),
        justify='center'
    ).grid(row=2, column=0, pady=(10, 25))

    return frame