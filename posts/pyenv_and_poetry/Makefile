install-pyenv-linux-mac:
	@echo "Installing pyenv"
	curl https://pyenv.run | bash
	@echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
	@echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
	@echo 'eval "$(pyenv init -)"' >> ~/.bashrc

install-pyenv-windows:
	@echo "Installing pyenv"
	Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

install-poetry-linux-mac:
	@echo "Installing poetry"
	curl -sSL https://install.python-poetry.org | python3 -
	
install-poetry-windows:
	@echo "Installing poetry"
	(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -