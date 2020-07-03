<h1 style="color: #1db954; background-color: #000000;">Botify</h1>

## PURPOSE

This repository serves several purposes:

1) A sandbox to investigate the [`spotipy`](https://spotipy.readthedocs.io/en/2.13.0/#) library in Python
2) Automate repetitive Spotify tasks
3) Save/store code that enables Spotify interaction between a user and the Spotify API

## REQUIREMENTS

The following packages are required to run this library:

- `spotipy`

## ORGANIZATION

The repository will maintain a copy of all local variables once cloned, which are provided by the operator. The `botifunctions.py` file contains the relevant files, while each individual action of the bot is separately controlled in its own container file (e.g. `move_discover_weekly_botify.py`).

## INSTALLATION

1) Clone this repository
2) Create a [Spotify](www.spotify.com) account
3) Create and register an application [here](https://developer.spotify.com/dashboard/applications)
    - When registering the application, set the Redirect URI to be `http://localhost:8888/callback/`
4) Make sure to note the Client ID and Client Secret provided by Spotify
5) Run the following in a Python interpreter:
```{python}
from botifunctions import authorize

authorize()
```

This should prompt for the Client ID, Client Secret, and a Spotify username. Supply the appropriate information when prompted

6) A web browser should open up and ask for authorization to allow the application to make changes for the user. Grant permission

7) Code away!

## CONTRIBUTORS

- @github/rossdrucker9