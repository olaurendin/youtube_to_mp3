# Youtube to MP3 API downloader

## Prerequisites

```bash
conda create -n youtube_to_mp3
conda activate youtube_to_mp3
conda install -c conda-forge -n youtube_to_mp3 moviepy pytube pandas openpyxl
pip install pytubefix
```

Python and librairies version are available in the environment.yml file.

## Usage

Lookup album playlist on YouTube. Copy the playlist URL on the [Export YouTube Playlist Website](https://export-youtube-playlist.vercel.app/) and export the playlist contents as an excel file. Rename the excel file as "urls.xlsx" on this project root folder and launch the following command from terminal :

```bash
python main.py
```

The MP3 files are located in the audios folder. You can delete the videos folder afterwards.

## Credits

- [Original Medium article](https://medium.com/@oluyaled/youtube-to-mp3-api-service-in-python-536c712f03b9)
- [StackOverFlow pytube fix](https://stackoverflow.com/questions/78160027/how-to-solve-http-error-400-bad-request-in-pytube)