# YT to Spotify Converter

Convert your YouTube playlists to Spotify with ease!

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

YT to Spotify Converter is a web application that allows users to seamlessly convert their YouTube playlists into Spotify playlists. By simply providing a YouTube playlist link, the app fetches the playlist's song titles and creates a corresponding Spotify playlist with the matching tracks. This tool is perfect for users who enjoy their music across both platforms and want to maintain consistency in their playlists.

## Features

- **Easy Conversion**: Input a YouTube playlist link and generate a Spotify playlist effortlessly.
- **User Authentication**: Securely authenticate with Spotify to create and manage playlists.
- **Automated Search**: Automatically searches for songs on Spotify based on YouTube titles.
- **Responsive Design**: Clean and intuitive web interface for a smooth user experience.
- **Extensible**: Open-source project welcoming contributions and enhancements.

## Demo

*Coming Soon!*

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **APIs**:
  - [YouTube Data API](https://developers.google.com/youtube/v3)
  - [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- **Libraries**:
  - [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) for Spotify API interactions
  - [Requests](https://docs.python-requests.org/en/latest/) for HTTP requests
  - [Flask](https://flask.palletsprojects.com/) for the web framework

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.7+** installed on your machine. You can download it from [here](https://www.python.org/downloads/).
- **Git** installed on your machine. Download it from [here](https://git-scm.com/downloads).
- **Spotify Developer Account**: Register and create an application to obtain `client_id` and `client_secret`. [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
- **YouTube Data API Key**: Obtain an API key from the [Google Developers Console](https://console.developers.google.com/).

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/yt-to-spotify.git
   cd yt-to-spotify
