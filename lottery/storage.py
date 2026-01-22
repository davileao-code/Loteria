from pathlib import Path
import json

class BancoJSON:
    def __init__(self, arquivo):
        self.path = Path(arquivo)
        self.dados = self._carregar()

    def _carregar(self):
        """Carrega o conteúdo do arquivo JSON ou cria lista vazia."""
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as arq:
                return json.load(arq)
        return []

    def adicionar(self, registro):
        """Adiciona um novo item ao 'banco'."""
        self.dados.append(registro)
        self._salvar()

    def apagar(self):
        if self.dados:
            self.dados.clear()
            self._salvar()
            return 'Todos os dados foram apagados'
        return 'Sem dados no sistema para apagar!'

    def _salvar(self):
        """Salva os dados no arquivo JSON"""
        with self.path.open("w", encoding="utf-8") as arq:
            json.dump(self.dados, arq, indent=4, ensure_ascii=False)




# class BancoJSON:
#     def __init__(self, arquivo):
#         self.path = Path(arquivo)
#         self.dados = self._carregar()

#     def _carregar(self):
#         """Carrega o conteúdo do arquivo JSON ou cria lista vazia."""
#         if self.path.exists():
#             texto = self.path.read_text(encoding="utf-8")
#             return json.loads(texto)
#         return []
    
#     def adicionar(self, registro):
#         """"Adiciona um novo item ao 'banco'.""" 
#         self.dados.append(registro)
#         self._salvar()

#     def apagar(self):
#         if self.dados:
#             self.dados.clear()
#             self._salvar()
#             return 'Todos os dados foram apagados'
#         return 'Sem dados no sistema para apagar!'


#     def _salvar(self):
#         """Salva os dados no arquivo JSON"""
#         texto = json.dumps(self.dados,indent=4, ensure_ascii=False)
#         self.path.write_text(texto, encoding="utf-8")