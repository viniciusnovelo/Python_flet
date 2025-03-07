# Real-Time Chat with Flet

This project implements a simple real-time chat using the Flet library. The system allows users to enter their names and send messages within a shared environment.

## Features

- Initial screen with a title and a button to start the chat.
- Popup/modal for entering the user's name before joining the chat.
- Chat area where messages are displayed in real-time.
- Input field for typing messages.
- Send button that automatically clears the input field after sending.

## Technologies Used

- Python
- Flet

## Prerequisites

Before running the project, install the necessary library with the following command:

```bash
pip install flet
```

## How to Run

1. Ensure that Python is installed on your machine.
2. Run the main script:
   ```bash
   python main.py
   ```
3. The chat will open in your browser and be ready for use.

## Project Structure

```
/
|-- main.py      # Main chat script
|-- README.md    # Project documentation
```

## How It Works

1. The user clicks the "Start Chat" button on the initial screen.
2. A popup/modal appears asking for the user's name.
3. Upon clicking "Join Chat":
   - The title and initial button disappear.
   - The chat and message input field are loaded.
   - A user entry message is displayed.
4. The user can type and send messages.
5. All messages appear in the chat in real-time.

## Author

Vinícius Vilela Novelo