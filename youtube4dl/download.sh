#!/bin/bash

# Check if youtube-dl is installed
if ! command -v youtube-dl &> /dev/null; then
    echo "youtube-dl is not installed. Please install it first."
    exit 1
fi

# Prompt user for YouTube URL
read -p "Enter the YouTube URL of the music video or playlist: " url

# Prompt user for download location
read -p "Enter the directory where you want to save the downloaded music: " directory

# Set download options
options="-x --audio-format mp3 --audio-quality 320K --embed-thumbnail --add-metadata"

# Download the music
youtube-dl --verbose $options -o "$directory/%(title)s.%(ext)s" $url
