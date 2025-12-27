[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![image](https://img.shields.io/pypi/v/uv.svg)](https://pypi.python.org/pypi/uv)
[![image](https://img.shields.io/pypi/l/uv.svg)](https://pypi.python.org/pypi/uv)
[![image](https://img.shields.io/pypi/pyversions/uv.svg)](https://pypi.python.org/pypi/uv)



# Alpha-Beta Algorithm

A Connect 4 game implementation featuring **Minimax** and **Alpha-Beta pruning** algorithms for AI decision-making.

## Package Manager

This project uses [uv](https://github.com/astral-sh/uv) An extremely fast Python package and project manager, written in Rust.

<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
    <img alt="Shows a bar chart with benchmark results." src="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
  </picture>
</p>

🚀 **A single tool to replace ```pip```, ```pip-tools```, ```pipx```, ```poetry```, ```pyenv```, ```twine```, ```virtualenv```, and more.**

⚡️ **10-100x faster than pip.**




## Getting Started

### Option 1: Run with Docker (Recommended)

Simply run the provided script (templates from [Astral documentation](https://docs.astral.sh/uv/guides/integration/docker/)):

```bash
./run.sh
```

### Option 2: Manual Installation

1. **Install uv**

   Unix/macOS:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Windows:
   ```powershell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Sync dependencies**

   ```bash
   uv sync
   ```

3. **Run the project**

   ```bash
   uv run src/main.py
   ```

## Features

- 🎮 Connect 4 game with graphical interface
- 🤖 AI opponents with two algorithms:
  - **Minimax**: Simple recursive search
  - **Alpha-Beta**: Optimized search with pruning
- 📊 Adjustable AI difficulty levels (1-42)

## License

See [LICENSE](LICENSE) for details.