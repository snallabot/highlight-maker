# highlight-maker

snallabot highlight maker for Madden 24.

## Developing

I am using pyenv with version 3.12.2. I created my own virtual env and installed the packages in `requirements.txt`. The other key piece is `youtube-dl` which you can find https://github.com/ytdl-org/youtube-dl

Download Test Video
```
youtube-dl -o test-videos/test-gameplay.mp4 https://www.youtube.com/watch\?v\=oEmk-gIOoDU
```

this is a gameplay of mine that I have been using for testing.

if you want to create your own virtual env:

```
# if you need to install python 3.12.2
# pyenv install 3.12.2
pyenv virtualenv 3.12.2 highlight-maker
pyenv activate highlight-maker
pip install -r requirements.txt
```

Then you can run the file

```
python highlight.py
```
