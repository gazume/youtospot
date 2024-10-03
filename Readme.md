# YT to Spotify Converter

Convert your YouTube playlists to Spotify

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Contributing](#contributing)
- [License](#license)

## Introduction

YT to Spotify Converter is a web application that allows users to seamlessly convert their YouTube playlists into Spotify playlists. By simply providing a YouTube playlist link, the app fetches the playlist's song titles and creates a corresponding Spotify playlist with the matching tracks. This tool is perfect for users who enjoy their music across both platforms and want to maintain consistency in their playlists.

## Technologies Used

- Python, Flask
- **APIs**:
  - [YouTube Data API](https://developers.google.com/youtube/v3)
  - [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- **Libraries**:
  - [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) for Spotify API interactions
  - [Requests](https://docs.python-requests.org/en/latest/) for HTTP requests
  - [Flask](https://flask.palletsprojects.com/) for the web framework

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Spotify Developer Account**: Register and create an application to obtain `client_id` and `client_secret`. [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
- **Spotify Developer client and secret keys**: from Spotify Developer Dashboard 
- **YouTube Data API Key**: Obtain an API key from the [Google Developers Console](https://console.developers.google.com/).
