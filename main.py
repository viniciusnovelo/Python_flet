#importa a biblioteca Flet
import flet as ft

# Função principal que inicia o aplicativo
def main(pagina):
    # Criando o título da aplicação
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)  # Adiciona o título à interface

    # Função para enviar mensagem para todos os usuários conectados
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)  # Cria um objeto de texto com a mensagem
        chat.controls.append(texto)  # Adiciona a mensagem ao chat
        pagina.update()  # Atualiza a interface para mostrar a nova mensagem

    # Inscreve a função no sistema de mensagens do Flet (pubsub)
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # Função chamada ao enviar uma mensagem no chat
    def enviar_mensagem(evento):
        nome_user = caixa_nome.value  # Obtém o nome do usuário
        texto_campo_mensagem = campo_enviar_mensagem.value  # Obtém o texto da mensagem
        mensagem = f"{nome_user}: {texto_campo_mensagem}"  # Formata a mensagem
        pagina.pubsub.send_all(mensagem)  # Envia a mensagem para todos os usuários
        campo_enviar_mensagem.value = ""  # Limpa o campo de entrada de mensagem
        pagina.update()  # Atualiza a interface

    # Cria o campo de entrada de mensagem e o botão de envio
    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # Organiza o campo de mensagem e o botão em uma linha horizontal
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    chat = ft.Column()  # Área do chat onde as mensagens aparecerão

    # Função chamada ao clicar no botão "Entrar no Chat"
    def entrar_chat(evento):
        popup.open = False  # Fecha o popup/modal
        pagina.remove(titulo)  # Remove o título da tela inicial
        pagina.remove(botao)  # Remove o botão "Iniciar Chat"
        
        # Adiciona a interface do chat na tela
        pagina.add(linha_enviar)
        pagina.add(chat)
        
        nome_usuario = caixa_nome.value  # Obtém o nome do usuário

        # Envia uma mensagem informando que o usuário entrou no chat
        mensagem2 = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem2)

        pagina.update()  # Atualiza a interface

    # Criando o popup/modal de entrada do usuário no chat
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")  # Campo para inserir o nome
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)  # Botão para entrar no chat

    # Configuração do popup
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    # Função chamada ao clicar no botão "Iniciar Chat"
    def abrir_popup(evento):
        pagina.dialog = popup  # Define o popup/modal na página
        popup.open = True  # Abre o popup
        pagina.update()  # Atualiza a interface
        
    # Botão inicial para abrir o popup
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    pagina.add(botao)  # Adiciona o botão na interface inicial

# Executa a aplicação no navegador
ft.app(main, view=ft.WEB_BROWSER)
