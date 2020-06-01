# Minecraft Sound Exporter

## About
V1.0

This utility was designed to export sounds and music from Minecraft.

You can run this program from the command line. If you don't have python installed, a .exe file is available which might be flagged by antivirus programs. Unfortunately you'll just have to take my word on it that this isn't a virus. ¯\\\_(ツ)_/¯

## Usage
Running this program, it will scan your Minecraft directory for indexes of installed versions and then ask you which version you would like to use for extraction. Type in the version, for example, `1.15` for Minecraft 1.15, and hit Enter to continue.

Next, you will need to specify whether you want to extract music only, sounds only, or both music and sounds. Type in `music`, `sfx`, or `both`, respectively.

The program will then extract the files and copy them to `/out/<version>/minecraft/sounds/`. The directory and sub-directories will be created automatically from the folder where the application was run.

Music files will be extracted to `/out/<version>/minecraft/sounds/music`.

Enjoy!
