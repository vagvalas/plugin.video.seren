[![Kodi version](https://img.shields.io/badge/kodi%20versions-18--19-blue)](https://kodi.tv/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![CI](https://github.com/SerenKodi/SerenDevelopment/workflows/CI/badge.svg?branch=v2-Development)
[![codecov](https://codecov.io/gh/SerenKodi/SerenDevelopment/branch/v2-Development/graph/badge.svg?token=LCX9WOPJ2M)](https://codecov.io/gh/SerenKodi/SerenDevelopment)
[![License: GPL3](https://img.shields.io/badge/License-GPL3-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

# Seren (plugin.video.seren)

Seren is a multi-source addon for Kodi with the added ability to install custom provider modules. Unlike other Kodi addons which are generally built for a single service use, Seren allows users to connect to multiple online/offline services at once for their viewing with a single click.

## Fixes for Python-2 Version of Seren 2.2.4 (by vagvalas)

Tried a sketchy fix inspired by the Python-3 fix with new RD's API implementation, as described here:
https://github.com/nixgates/plugin.video.seren/issues/949#issuecomment-2498755711
For some reason a lot of people still needed a Seren with Python-2 suppport for Nvidia Shields or old tv-boxes

2.2.6 Fixes the behaviour of not playing , non playable sources, by skipping them, should work faster now
2.2.5 Fixes this but its a bit slow

## BUGS

~~Found out that if the source selected is not playable (as you cant know before selecting it) it hangs there, as no prompt appearing 
as the new 3.0.1 version for selecting manually a playable file (as there isn't any playable files :P) and had to be skipped.~~
-Working right now on a fix for that behaviour :P
FIXED. 2.2.6

## License

Licensed under The GPL License.