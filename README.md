# ImgScripts

A collection of scripts for imgflip

## Getting Started

Follow these steps to set up the project and run `main.py` from a fresh environment.

### 1. Prerequisites

- **Python 3.8 or later**  
  Download from [python.org](https://www.python.org/downloads/) if needed.

- **Google Chrome**
  Download from [google.com/chrome](https://google.com/chrome).

- (Optional but recommended) **Git**  
  Download from [git-scm.com](https://git-scm.com/downloads).

### 2. Clone the Repository

Open a terminal (Command Prompt, PowerShell, or Terminal app) and run:

```sh
git clone https://github.com/ArmadilloMike/ImgScripts.git
cd ImgScripts
```

Alternatively, [download the ZIP](https://github.com/ArmadilloMike/ImgScripts/archive/refs/heads/main.zip) and extract it, then open a terminal in that folder.

### 3. Create a Virtual Environment (Recommended)

This keeps dependencies isolated.

```sh
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

This project uses pydoll-python and faker libraries

```sh
pip install -m pydoll-python
pip install -m faker
```


### 5. Run `main.py`

```sh
# Windows
python main.py

# macOS/Linux
python3 main.py
```

## Additional Notes

- If you encounter errors about missing packages or permissions, ensure your virtual environment is activated and Python is installed correctly.
- For more advanced usage or configuration, see comments in `main.py` or other project files.

## Contributing

Pull requests and suggestions are welcome! Please open an issue to discuss changes.

## License

[MIT](LICENSE)
