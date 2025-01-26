# MediTranslateAI
## Final Year Project - Noy Tsafrir & Shachar Felman

MediTranslateAI is an advanced medical translation application designed to accurately translate medical leaflets from Hebrew to English. 
It leverages state-of-the-art language models and evaluation metrics to ensure high-quality translations of complex medical terminology and information.

## Features

- Translate medical leaflets from Hebrew to English
- Utilize multiple advanced language models for translation
- Evaluate translations using various metrics (BLEU, CHRF, WER)
- Store and manage translation history
- Generate downloadable DOCX files of translations
- User-friendly web interface for easy interaction

## System Architecture

![Block Diagram](https://github.com/user-attachments/assets/43e27695-402a-481f-8340-9968e52ac921)

## ScreenShots - Web Interface

![full](https://github.com/user-attachments/assets/e4b69b4d-f472-4480-a64c-8d5ad2f371e9)
![Translating](https://github.com/user-attachments/assets/b9530efc-cbd0-4e04-afe8-530b2b959a05)
![file downloaded](https://github.com/user-attachments/assets/47426944-a2f9-45b2-ba9d-541116ba0f0c)

## Technologies Stack

- User Interface - React.js
- Server - Python, Flask
- Database - MongoDB
- Containerization - Docker
- Environment -  VSCode
- LLM Framework- LangChain

## Usage

1. Navigate to the web interface
2. Enter the Hebrew text from a medical leaflet
3. Click "Translate" to get the English translation
4. View, save, or download the translated content

## Project Structure

- `flask_backend/`: Python Flask backend
  - `app.py`: Main Flask application
  - `routes/`: API route definitions
  - `services/`: Core translation and evaluation services
  - `utils/`: Utility functions and helpers
- `react_frontend/`: React frontend application
- `docker-compose.dev.yml`: Docker Compose configuration for development
- `docker-compose.test.yml`: Docker Compose configuration for testing

## Testing

To run the test suite:

```
./test.ps1
```

This will build and run the test environment using Docker.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). This means:

- You are free to use, modify, and distribute this software.
- If you distribute this software or any derivative works, you must do so under the same GPL-3.0 license.
- You must make the source code available when you distribute the software.
- Changes made to the code must be documented.

For more details, see the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
