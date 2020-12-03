 # MindOverCNC Mill

QtPyVCP based Virtual Control Panel for LinuxCNC, optimized for 1366 x 768px (15 inch wide) touch screens.
This is intended for mills only.

## Applying this VCP

1) Navigate to your machine home directory.
2) Clone it to your local machine:
  `git clone https://github.com/85vmh/mindovercncmill.git`
3) Install with pip:
  `pip install -e .`
4) Copy the font file /mindovercncmill/fonts/BebasKai.tff into your home directory /home/{yourUserName}/.local/share/fonts/
5) Edit the .ini file of the machine configuration on which you wish to apply this VCP and add the following lines in the [DISPLAY] section:
`
[DISPLAY]
DISPLAY = qtpyvcp
VCP = mindovercncmill
`
