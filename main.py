# Import the Flet library
import flet as ft

# Main function that starts the application
def main(page):
    # Create the application title
    titulo = ft.Text("Hashzap")
    page.add(titulo)  # Add the title to the interface

    # Function to send a message to all connected users
    def send_message_tunnel(message):
        text = ft.Text(message)  # Create a text object with the message
        chat.controls.append(text)  # Add the message to the chat
        page.update()  # Update the interface to show the new message

    # Subscribe the function to Flet's pubsub messaging system
    page.pubsub.subscribe(send_message_tunnel)

    # Function called when sending a message in the chat
    def send_message(event):
        user_name = name_box.value  # Get the user's name
        message_text = message_field.value  # Get the message text
        message = f"{user_name}: {message_text}"  # Format the message
        page.pubsub.send_all(message)  # Send the message to all users
        message_field.value = ""  # Clear the message input field
        page.update()  # Update the interface

    # Create the message input field and the send button
    message_field = ft.TextField(label="Type your message here")
    send_button = ft.ElevatedButton("Send", on_click=send_message)

    # Organize the message field and the button in a horizontal row
    send_row = ft.Row([message_field, send_button])
    chat = ft.Column()  # Chat area where messages will appear

    # Function called when clicking the "Join Chat" button
    def join_chat(event):
        popup.open = False  # Close the popup/modal
        page.remove(titulo)  # Remove the title from the initial screen
        page.remove(button)  # Remove the "Start Chat" button
        
        # Add the chat interface to the screen
        page.add(send_row)
        page.add(chat)
        
        username = name_box.value  # Get the user's name

        # Send a message informing that the user has joined the chat
        message2 = f"{username} joined the chat"
        page.pubsub.send_all(message2)

        page.update()  # Update the interface

    # Create the popup/modal for user entry into the chat
    popup_title = ft.Text("Welcome to Hashzap")
    name_box = ft.TextField(label="Enter your name")  # Field to enter the name
    popup_button = ft.ElevatedButton("Join Chat", on_click=join_chat)  # Button to join the chat

    # Configure the popup
    popup = ft.AlertDialog(title=popup_title, content=name_box, actions=[popup_button])

    # Function called when clicking the "Start Chat" button
    def open_popup(event):
        page.dialog = popup  # Set the popup/modal on the page
        popup.open = True  # Open the popup
        page.update()  # Update the interface
        
    # Initial button to open the popup
    button = ft.ElevatedButton("Start Chat", on_click=open_popup)
    page.add(button)  # Add the button to the initial interface

# Run the application in the browser
ft.app(main, view=ft.WEB_BROWSER)