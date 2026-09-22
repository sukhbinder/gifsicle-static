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

### Common Use Cases

| Description | Command | Notes |
|---|---|---|
| **Optimize for smaller size** | `gif -O3 input.gif -o output.gif` | `-O3` tries several methods to shrink the file without losing quality. Use `--lossy=80` for even smaller files with some quality loss. |
| **Resize a GIF** | `gif --resize 320x240 input.gif -o output.gif` | Use `--resize-width 320` to preserve the aspect ratio. `--scale` is another option for scaling. |
| **Create an animation from images** | `gif --delay=10 --loopcount=forever frame*.gif -o animation.gif` | Combines multiple image files into a single looping animation. `--delay` sets the speed. |
| **Select specific frames** | `gif input.gif '#0-9' -o frames.gif` | Extracts a range of frames (e.g., the first 10 frames) into a new file. Use `#-1` for the last frame. |
| **Change animation speed** | `gif --delay=5 input.gif -o faster.gif` | Decreasing the delay value speeds up the GIF. |
| **Reduce the color palette** | `gif --colors 64 input.gif -o output.gif` | Limits the number of colors, which can significantly reduce file size. |
| **Inspect GIF information** | `gif --info input.gif` | Displays details like frame count, delays, and dimensions. |
| **Edit files in place** | `gif -bO3 *.gif` | The `--batch` (`-b`) option modifies the original files instead of creating new ones. |
| **Apply image transformations** | `gif --rotate-90 input.gif -o rotated.gif` | Supports cropping (`--crop`), flipping (`--flip-*`), and rotating (`--rotate-*`). |

## Development

To run the script directly without installing:

```bash
python gif.py --version
```

## License

This project is licensed under the MIT License.
