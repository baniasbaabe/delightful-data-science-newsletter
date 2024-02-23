install-pyenv:
	@echo "Installing pyenv"
	curl https://pyenv.run | bash
	@echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
	@echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
	@echo 'eval "$(pyenv init -)"' >> ~/.bashrc

install-poetry:
	@echo "Installing poetry"
	curl -sSL https://install.python-poetry.org | python3 -
	