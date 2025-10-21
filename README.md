# Mental-Health-Chatbot

## Overview
The Mental Health Chatbot is an interactive web-based platform designed to provide users with a safe and supportive environment to discuss their thoughts and emotions. Powered by Ollama as the core conversational engine, the chatbot engages users in empathetic, human-like conversations to promote mental wellness and emotional support.

## Repository
This project is hosted on GitHub: [Mental Health Chatbot Repository](https://github.com/Karri001/Mental-Health-Chatbot)

## Features
- **Conversational AI (Ollama Integration)**: The chatbot uses Ollama’s local large language model as its “brain” to understand and respond naturally to user inputs.
- **Chat History**: Each user’s previous conversations are securely stored and retrievable, allowing continuity and personalization in future sessions.
- **User Authentication**:
  - Signup: Create a new account with secure credentials.
  - Login: Access personalized chat experiences.
  - Forgot Password: Reset password securely using email verification or token-based recovery.
- **Responsive UI**: Built with React, the interface is intuitive, user-friendly, and optimized for both desktop and mobile use.
- **Backend & Database**:
  - Python (Flask/FastAPI): Handles communication with Ollama, authentication, and chat data management.
  - MongoDB: Stores user data, chat histories, and authentication details.

## How It Works
1. **User Authentication**: 
   - Users sign up or log in using their email and password.
   - The system verifies credentials (stored securely in MongoDB) and creates a session using tokens.
2. **Chat Interface**: 
   - Once logged in, users access the chat screen built with React.
   - They can send messages to the chatbot through a simple, responsive UI.
3. **Backend Processing**: 
   - Each message is sent from the frontend to the Python backend (Flask/FastAPI).
   - The backend forwards the user’s input to Ollama, which serves as the AI “brain.”
4. **Ollama Response Generation**: 
   - Ollama processes the input using its local large language model.
   - It generates a natural, empathetic reply suitable for mental health support conversations.
5. **Chat History Management**: 
   - The backend stores both user messages and bot replies in MongoDB.
   - When users return, the chatbot loads their previous chat history for context and continuity.
6. **Optional Password Recovery**: 
   - If a user forgets their password, a secure token or email-based reset process is triggered.

## Setup and Installation
Follow these steps to set up the project:

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Karri001/Mental-Health-Chatbot.git
   cd Mental-Health-Chatbot
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Download Ollama:
   - Ollama can be downloaded from this site (https://ollama.com/download)
4. Open Three Different Terminals and Open the Three folders Shown Below in Those Terminals to Run the Application :
   - To Start Chatbot of the Application
    
      ```bash
      cd Cbot
      python app.py
      ```
   - To Start Frontend of the Application
    
      ```bash
      cd frontend
      npm start
      ```
   - To Start Backend of the Application
    
      ```bash
      cd backend
      npm start
      ```

### Run the Application
Start the Gradio interface:
```bash
python app.py
```
The Gradio interface will launch, and you can access it via the displayed URL.

## Usage
### Using the Gradio Interface
1. **Upload an Image or Video**: Drag and drop a file into the provided input box.
2. **Real-Time Classification**: Select the webcam option to perform live traffic sign detection.
3. **View Results**: Detected traffic signs will be displayed with bounding boxes and class labels.

### Command-Line Interface (Optional)
For advanced users, inference can also be performed via the command line:
```bash
python detect.py --source <path_to_input> --weights models/best.pt
```

## Screenshots
### Gradio Interface
![Gradio Interface](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/Screenshot%20(279).png)


### Detection Result
![Detection Result](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/Screenshot%20(281).png)
![Detection Result](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/Screenshot%20(282).png)
![Detection Result](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/Screenshot%20(283).png)

### Video Demonstration
![Video Demonstration](https://github.com/Karri001/Traffic-sign-classification/blob/main/Screenshots/video/WIN_20241130_00_07_38_Pro.mp4)

## Custom Dataset
The model is trained on a custom dataset that includes diverse traffic signs observed in Indian road conditions. The dataset contains:
- **Traffic Sign Types**: Speed limits, warning signs, mandatory signs, and more.
- **Environmental Variations**: Urban, rural, day, and night scenarios.

## Real-Time Performance
This system supports real-time traffic sign detection with minimal latency, making it suitable for applications such as:
- Autonomous vehicles
- Traffic monitoring systems
- Driver assistance tools

## Future Enhancements
- Adding more traffic sign classes for enhanced coverage.
- Improving performance for extreme weather and lighting conditions.
- Extending support for other road conditions beyond Indian scenarios.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or additional features.

## License
This project is licensed under the [MIT License](LICENSE).

---

**Author**: K.Sai Sri Venkata Reddy

For questions or suggestions, please contact: [venkatreddykarri001@gmail.com.com]
