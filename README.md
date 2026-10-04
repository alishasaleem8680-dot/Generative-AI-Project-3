# Multimodal Image Generation Studio

## Project Overview

Multimodal Image Generation Studio is a Python-based Generative AI application that converts natural language prompts into digital artwork using an image generation API.

The application allows users to enter a text prompt, select an aspect ratio, choose the number of images to generate, and save the generated images locally.

## Project Goal

The goal of this project is to build a visual application that converts natural language descriptions into digital artwork while providing control over image format and generation count.

## Key Features

- Text-to-image generation
- Natural language prompt input
- Aspect ratio selection
- Image resolution handling
- Multiple image generation
- Local image saving
- Image integrity verification
- Retry handling
- Secure API token management using environment variables

## Technologies Used

- Python
- Hugging Face Inference API
- FLUX.1-schnell
- Hugging Face Hub
- Pillow
- python-dotenv

## Supported Aspect Ratios

- 1:1 Square
- 16:9 Landscape
- 9:16 Vertical

## Project Structure

```text
Generative_AI_Project_3/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── generated_images/
└── .venv/