# Media Converter

Media Converter is a Django-based web application for converting media files to different formats using FFmpeg.

## Features

- **File Upload**: Users can upload multiple media files simultaneously.
- **Format Conversion**: Convert media files to various formats such as MP3 and MP4.
- **Bitrate Options**: Choose different bitrate options for audio files (e.g., 128 kbps, 192 kbps).
- **Download Converted Files**: Download the converted files after processing.

## Technologies Used

- **Django**: Web framework for building the application.
- **FFmpeg**: Tool for handling multimedia data, used for converting media files.
- **SQLite**: Database for storing file metadata.
- **HTML/CSS**: Frontend for user interaction.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/converter-master.git
    cd converter-master
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Start the development server**:
    ```bash
    python manage.py runserver 0.0.0.0:8123
    ```

    **Build docker image**
    ```bash
    docker build -t media-converter .
    ```

    **Run container**
    ```bash
    docker run -d -p 8123:8123 -v /path/to/local/media:/app/media
    ```

    **Save image**
    ```bash
    docker save -o media-converter.tar media-converter
    ```

6. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8123`.

## Usage

1. **Upload Files**:
    - Navigate to the upload page.
    - Select the files you want to upload.
    - Choose the desired output format and bitrate.
    - Click the upload button to start the conversion process.

2. **Download Converted Files**:
    - After the conversion is complete, a link to download the converted files will be provided on the result page.

