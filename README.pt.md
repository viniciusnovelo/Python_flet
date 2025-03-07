# Chat em Tempo Real com Flet

Este projeto implementa um chat simples em tempo real utilizando a biblioteca Flet. O sistema permite que os usuários entrem com seus nomes e enviem mensagens dentro de um ambiente compartilhado.

## Funcionalidades

- Tela inicial com título e botão para iniciar o chat.
- Popup/modal para inserção do nome do usuário antes de entrar no chat.
- Área de chat onde mensagens são exibidas em tempo real.
- Campo de entrada para digitação de mensagens.
- Botão de envio de mensagens que limpa automaticamente o campo após o envio.

## Tecnologias Utilizadas

- Python
- Flet

## Pré-requisitos

Antes de executar o projeto, instale a biblioteca necessária com o seguinte comando:

```bash
pip install flet
```

## Como Executar

1. Certifique-se de que tem o Python instalado em sua máquina.
2. Execute o script principal:
   ```bash
   python main.py
   ```
3. O chat será aberto no navegador e estará pronto para uso.

## Estrutura do Projeto

```
/
|-- main.py      # Script principal do chat
|-- README.md      # Documentação do projeto
```

## Como Funciona

1. O usuário clica no botão "Iniciar Chat" na tela inicial.
2. Um popup/modal aparece pedindo para inserir o nome.
3. Ao clicar em "Entrar no Chat":
   - O título e o botão inicial desaparecem.
   - O chat e o campo de envio de mensagens são carregados.
   - Uma mensagem de entrada do usuário é exibida.
4. O usuário pode digitar mensagens e enviá-las.
5. Todas as mensagens aparecem no chat em tempo real.

## Autor

Vinícius Vilela Novelo