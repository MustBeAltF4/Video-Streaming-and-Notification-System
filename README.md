## README.md

### Video Streaming and Monitoring System

This repository contains a Python application for streaming video from a webcam and monitoring its status. The application uses Flask for web server implementation, OpenCV for video capture, and Telebot for Telegram bot integration.

#### Prerequisites

- Python 3.6 or later
- Required Python packages can be installed using the following command:

    ```bash
    pip install Flask opencv-python Flask-APScheduler python-telegram-bot fasteners
    ```

#### Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/MustBeAltF4/Video-Streaming-and-Notification-System.git
    cd Video-Streaming-and-Notification-System.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up a Telegram bot and replace the `bot_token` variable in the code with your bot's token.

4. Replace the `user_ids` variable with your Telegram user IDs.

5. Run the application:

    ```bash
    python your_app_name.py
    ```

6. Access the video stream by visiting `http://localhost:2020` in your web browser.

#### Features

- Video streaming from a webcam using OpenCV.
- Integration with Telegram bot for status notifications.
- Real-time clock overlay on the video feed.
- Red circle flashing on the video feed.
- Automatic notification if the application is not running.

#### Configuration

- Change the `bot_token` variable to your Telegram bot token.
- Replace the `user_ids` list with your Telegram user IDs.
- Customize the streaming link and other settings as needed.

#### Known Issues

- No known issues.

#### Compatibility

The code has been tested with Python 3.6 and later.

#### Acknowledgments

- Special thanks to the authors of the libraries used in this project.

#### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
