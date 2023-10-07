class UsuarioLogado:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UsuarioLogado, cls).__new__(cls)
            cls._instance.id = None
            cls._instance.nome = None
            cls._instance.perfil = None
        return cls._instance
