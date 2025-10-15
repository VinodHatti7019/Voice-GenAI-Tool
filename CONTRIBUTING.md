# Contributing to Voice-GenAI-Tool

Thank you for your interest in contributing to Voice-GenAI-Tool! We welcome contributions from the community to help make this project better.

## How to Contribute

### Reporting Issues

- Check if the issue already exists in the [Issues](https://github.com/VinodHatti7019/Voice-GenAI-Tool/issues) section
- Use a clear and descriptive title
- Provide detailed steps to reproduce the issue
- Include your environment details (OS, Python version, etc.)

### Submitting Pull Requests

1. **Fork the Repository**
   - Click the "Fork" button at the top right of the repository page

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Voice-GenAI-Tool.git
   cd Voice-GenAI-Tool
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Follow the coding standards below
   - Add tests for new features
   - Update documentation as needed

5. **Test Your Changes**
   ```bash
   pytest tests/
   ```

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

7. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch and provide a clear description

## Coding Standards

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Write unit tests for new features

## Commit Message Guidelines

Use conventional commit messages:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Adding or updating tests
- `refactor:` - Code refactoring
- `style:` - Code style changes (formatting, etc.)
- `chore:` - Maintenance tasks

Example: `feat: add speech-to-text functionality`

## Development Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your API keys

3. Run tests:
   ```bash
   pytest tests/
   ```

## Code Review Process

- All pull requests require review before merging
- Address review comments promptly
- Keep pull requests focused on a single feature/fix
- Maintain backward compatibility when possible

## Questions?

Feel free to open an issue for questions or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.
