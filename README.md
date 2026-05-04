# gifsicle-cli

A Python wrapper for the `gifsicle` command-line tool.

This package provides a `gif` command that acts as a direct passthrough to the `gifsicle.exe` executable.

## Installation

1.  Ensure you have Python 3.6 or higher installed.
2.  Clone this repository:
    ```bash
    git clone https://github.com/yourusername/gifsicle-cli.git
    cd gifsicle-cli
    ```
3.  Install the package:
    ```bash
    pip install .
    ```

## Usage

Once installed, you can use the `gif` command directly from your terminal, followed by any arguments you would normally pass to `gifsicle`.

```bash
gif --version
gif -o output.gif input.gif --optimize=3
```

## Development

To run the script directly without installing:

```bash
python gif.py --version
```

## License

This project is licensed under the MIT License.
