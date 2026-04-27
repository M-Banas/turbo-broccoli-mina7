# turbo-broccoli-mina7

A test repository demonstrating how to work with `.env` files.

## Environment Variables

This project uses a `.env` file to manage configuration and secrets. The `.env` file is **not committed to version control** (it is listed in `.gitignore`) to keep sensitive values like passwords and API keys out of the repository.

A `.env.example` file is provided as a template showing which environment variables are required.

### Getting Started

1. Copy the example file to create your own `.env`:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` and fill in the values appropriate for your environment.

3. Never commit `.env` to version control — it is already excluded via `.gitignore`.

## Notes

- Always share `.env.example` (with placeholder values) when adding new environment variables.
- Keep real secrets out of `.env.example`.
