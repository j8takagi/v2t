# v2t

A tool for transcribing audio files using OpenAI Whisper, optimized for macOS. Clean, readable Python code distributed under the MIT License.

## Prerequisites

Before running the tool, ensure you have the following installed on your system:

- **Python**: 3.10 or higher
- **FFmpeg**: Required by Whisper for audio decoding.
  ```bash
  brew install ffmpeg
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/j8takagi/v2t.git
   cd v2t
   ```

2. Install the required Python packages:
   ```bash
   pip install openai-whisper torch
   ```

## Usage

Run the script by passing the target audio file as an argument. To save the transcription to a text file while viewing progress in your terminal, use standard output redirection:

```bash
python3 v2t.py sample.mp3 > sample.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
