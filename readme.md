# Fenômenos de Transporte 2 — UFS

Este repositório contém o programa `q1.py` e sua versão equivalente em JavaScript, `q1.js`, ambos desenvolvidos para a disciplina de **Fenômenos de Transporte 2** da Universidade Federal de Sergipe (UFS).

> **Observação:**  
> Os dois arquivos implementam o mesmo cálculo, porém em linguagens diferentes (Python e JavaScript).  
> No caso do JavaScript, os valores de entrada estão fixos no código para facilitar a execução no navegador.

## Como executar

O programa calcula parâmetros de transferência de calor em um tubo, a partir de dados fornecidos via linha de comando (Python) ou fixos no código (JavaScript).

### Requisitos

- Para Python: Python 3 instalado no sistema.
- Para JavaScript: Qualquer navegador moderno.

### Execução em Python

No terminal, navegue até a pasta do projeto e execute:

```sh
python3 q1.py 8.3e-3 60 100 150 1.6 54.6 0.092 0.42 3.96e-4 6.5
```

#### Observação

- **No Ubuntu (Linux):**  
  Use o terminal padrão e o comando acima normalmente.
- **No Windows (CMD):**  
  Use o prompt de comando e execute:
  ```
  python q1.py 8.3e-3 60 100 150 1.6 54.6 0.092 0.42 3.96e-4 6.5
  ```
  (Certifique-se de que o Python está instalado e configurado no PATH.)

---

### Execução em JavaScript (no navegador)

1. Abra o arquivo `q1.js` em um editor de texto.
2. Copie todo o conteúdo do arquivo.
3. Abra o navegador de sua preferência.
4. Pressione `F12` para abrir o console de desenvolvedor.
5. Cole o código copiado no console e pressione `Enter`.

Os resultados dos cálculos aparecerão diretamente no console do navegador.

---