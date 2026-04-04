# 🔐 Gerador de Senhas Seguras

Um gerador de senhas simples, seguro e personalizável desenvolvido em Python.  
Permite criar senhas fortes com diferentes combinações de caracteres, garantindo maior segurança para o usuário.

---

## 🚀 Funcionalidades

- Definição personalizada do tamanho da senha
- Opção de inclusão de:
  - Letras maiúsculas (A–Z)
  - Letras minúsculas (a–z)
  - Números (0–9)
  - Símbolos seguros (`!@#$%&*-_+=`)
- Geração rápida e aleatória
- Interface simples via terminal
- Utiliza apenas bibliotecas nativas do Python

---

## 🧠 Como funciona

O sistema permite ao usuário escolher quais tipos de caracteres deseja incluir na senha.  
Com base nessas escolhas, a aplicação monta um conjunto de caracteres válidos e gera uma senha aleatória com o tamanho definido.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Bibliotecas nativas:
  - `random`
  - `string`

---

## 📦 Estrutura do projeto


.
├── main.py # Script principal do gerador de senhas


---

## 🖥️ Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/chkawan/password-generator.git
cd password-generator ;
```

### 2. Executar o projeto
```bash
python main.py
```

## 💡 Exemplo de uso


### === Gerador de Senhas Seguras ===

- Tamanho da senha: 12
- Incluir letras maiúsculas? (s/n): s
- Incluir letras minúsculas? (s/n): s
- Incluir números? (s/n): s
- Incluir símbolos? (s/n): s
- Senha gerada: A@7kL2#pQ9!


## 🔐 Boas práticas de segurança


- Utilize senhas com no mínimo 12 caracteres
- Combine letras, números e símbolos
- Evite reutilizar senhas
- Não compartilhe suas senhas


Este projeto é de uso livre para fins educacionais e pode ser adaptado conforme necessário.

👨‍💻 Autor

Desenvolvido por Christopher Kawan
