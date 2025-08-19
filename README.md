# DELETEME AKellner

[![PyPI version](https://badge.fury.io/py/deleteme-akellner.svg)](https://badge.fury.io/py/deleteme-akellner)
[![CI Status](https://github.com/AlonKellner-RedHat/deleteme_akellner/actions/workflows/ci-orchestrator.yml/badge.svg)](https://github.com/AlonKellner-RedHat/deleteme_akellner/actions/workflows/ci-orchestrator.yml)
[![Docs Status](https://github.com/AlonKellner-RedHat/deleteme_akellner/actions/workflows/docs.yml/badge.svg)](https://github.com/AlonKellner-RedHat/deleteme_akellner/actions/workflows/docs.yml)
[![All time downloads](https://static.pepy.tech/badge/deleteme-akellner)](https://pepy.tech/project/deleteme-akellner)
[![Weekly Downloads](https://static.pepy.tech/badge/deleteme-akellner/week)](https://pepy.tech/project/deleteme-akellner)  

[![Python versions](https://img.shields.io/pypi/pyversions/deleteme-akellner.svg)](https://pypi.org/project/deleteme-akellner/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Py Stack: astral.sh](https://img.shields.io/badge/py%20stack-astral.sh-30173d.svg)](https://github.com/astral-sh)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=devcontainer&message=Open&color=blue)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/AlonKellner-RedHat/deleteme_akellner)
[![Cursor](https://img.shields.io/static/v1?label=-&message=Cursor&color=black)](https://cursor.com/downloads)
[![Claude Code](https://img.shields.io/static/v1?label=-&message=Claude%20Code&color=d77253)](https://www.anthropic.com/claude-code)


Python Boilerplate contains all the boilerplate you need to create a Python package.

## Features

* TODO
## 🚀 Quick Start

### Installation

```bash
# Install from PyPI
pip install deleteme-akellner

# Or install from source
git clone https://github.com/AlonKellner-RedHat/deleteme_akellner.git
cd deleteme-akellner
pip install -e .
```

### Basic Usage

* TODO

## 📖 Documentation

- [User Guide](docs/user-guide.md) - Complete usage instructions
- [Examples](docs/examples.md) - Common use cases and examples

## 🤝 Contributing

We welcome contributions! Please see our
[Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

#### Prerequisites
- [Docker](https://www.docker.com/get-started/)
- [VSCode](https://code.visualstudio.com/download)/[Cursor](https://cursor.com/downloads) (or any IDE with [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) support)

#### Steps

Either click the badge (VSCode only)  
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/AlonKellner-RedHat/deleteme_akellner)  
or (Cursor/VSCode)

1. `git clone https://github.com/AlonKellner-RedHat/deleteme_akellner.git`
2. Open the repository in your IDE of choice
3. `cmd+shift+p`/`ctrl+shift+p`
4. Type "reopen"
5. Choose "Dev Containers: Reopen in Container"

   This will automatically:

   - Build and start a devcontainer with binary requirements
   - Install the `pre-commit` hooks
   - Use `uv` to install python and all python dependencies into a local `.venv`
   - Install a few MCP servers

   The first time it will fail and prompt you for 3 things:

- Add a [github access token](https://github.com/settings/personal-access-tokens) to ./.devcontainer/.env:

  ```sh
  GITHUB_PERSONAL_ACCESS_TOKEN=<your_personal_access_token_here>
  ```

- [Generate a GPG key and add it to github](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key)
- [Configure a GPG key as your signing key](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key)

#### MCP

The current MCP servers that this repo supports are:
1. [`github-mcp-server`](https://github.com/github/github-mcp-server) (Remote)
2. [`repomix`](https://github.com/yamadashy/repomix) (Local)
3. [`mcp-language-server`](https://github.com/isaacphi/mcp-language-server)

#### [Claude Code](https://www.anthropic.com/claude-code)

The `pre-commit` setup in this repo uses `claude` code to
automatically review changes.  
By default, `claude` will not be configured and will automatically
pass in the `pre-commit`.  

If you want to use `claude` to review changes, you can read about
[Claude Code Deployment](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations).

## 📝 License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with modern Python tooling ([astral.sh stack](https://github.com/astral-sh), [tox stack](https://github.com/tox-dev))
- Created with [Cookiecutter](https://github.com/audreyfeldroy/cookiecutter) and the [AlonKellner/cookiecutter-pypackage-2025](https://github.com/AlonKellner/cookiecutter-pypackage-2025) project template (fork of [AlonKellner/cookiecutter-pypackage-2025](https://github.com/AlonKellner/cookiecutter-pypackage-2025))


## 📊 Project Status

- **Development Status**: Alpha
- **Python Support**: 3.10+
- **License**: MIT
- **Maintainer**: [Alon Kellner](mailto:akellner@redhat.com)

---

## Made with ❤️ by the DELETEME AKellner community
