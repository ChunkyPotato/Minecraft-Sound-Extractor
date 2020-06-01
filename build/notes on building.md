Install pyinstaller: `pip install pyinstaller` or `py -m pip install pyinstaller`, depending on configuration.

Then navigate to the build directory: `cd [...]/Minecraft Sound Extractor/exe`, replacing `[...]` with the appropriate path.

Then run this command: `pyinstaller --onefile --icon=dia_pick.ico MinecraftSoundExtractor.py` or `py -m PyInstaller --onefile --icon=dia_pick.ico MinecraftSoundExtractor.py`, depending on configuration.

The .exe will be in `/dist/`

Done!