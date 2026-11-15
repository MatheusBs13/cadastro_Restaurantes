# 🍽️ Cadastro de Restaurantes (Sabor Express)

Aplicação de **terminal em Python** para cadastrar restaurantes, listá-los e ativar/desativar cada um. Feita como projeto de estudo de lógica, funções, listas e dicionários em Python.

## 📒 Funcionalidades

Menu interativo com as opções:

1. **Cadastrar restaurante**: informa nome e categoria; o restaurante entra como *inativo*
2. **Listar restaurantes**: mostra nome, categoria e status (`True` = ativo, `False` = inativo)
3. **Ativar restaurante**: alterna o estado de um restaurante pelo nome (ativo ↔ inativo)
4. **Sair**

O programa já começa com três restaurantes de exemplo (Praça, Pizza supresa e Marcone).

## 🛠️ Tecnologias

- Python 3
- Biblioteca padrão (`os`) para o app principal
- [`psutil`](https://pypi.org/project/psutil/) e [`fpdf2`](https://pypi.org/project/fpdf2/) apenas para o script de monitoramento

## 📁 Estrutura

```
├── app.py                        # aplicação principal (menu de restaurantes)
├── monitoramento.py              # monitora CPU/RAM e gera um relatório em PDF
├── system_monitoring_report.pdf  # exemplo de relatório gerado
├── main.py                       # script de teste: lista arquivos de uma pasta
└── Teste.py                      # script de teste: abrir um programa no Windows
```

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/MatheusBs13/cadastro_Restaurantes.git
   cd cadastro_Restaurantes
   ```
2. Rode o app principal:
   ```bash
   python app.py
   ```

> O app usa `os.system('cls')` para limpar a tela, então foi pensado para **Windows**. No Linux/macOS troque por `'clear'`.

### Monitoramento de sistema (opcional)

```bash
pip install psutil fpdf2
python monitoramento.py
```

Mede CPU e RAM por 10 segundos (1 medição por segundo), mostra no terminal e salva em `system_monitoring_report.pdf`. Requer Python 3.12 ou superior.

## 🚧 Próximos passos

- Salvar os restaurantes em arquivo (JSON/CSV) ou banco de dados; hoje os dados ficam só na memória e se perdem ao fechar
- Mostrar "Ativo"/"Inativo" em vez de `True`/`False` na listagem
- Fazer a opção **Sair** encerrar o programa
- Deixar a limpeza de tela compatível com qualquer sistema operacional

## 👤 Autor

[MatheusBs13](https://github.com/MatheusBs13)
