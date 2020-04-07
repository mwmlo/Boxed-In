# Boxed In

Boxed In is a "virtual care package" platform for students and teachers to connect virtually while classes are moved online. The aim of this web app is to encourage community spirit and support people during school closures.

## How it works

Boxed In allows users to share funny stories, recommend memes and videos, listen to meditations and add supportive comments. 

1. Users create an account using a username and password.
2. Users can upload and link content into a virtual care box. When submitted, the box's contents will be  sent to another random user.
3. When the receiver opens the box, the contents of the box will also be shared publicly on the respective feeds (#ZoomLife, Memes and Support).

## File system

- `requirements.txt`: Flask requirements needed
- `boxedin.db`: SQLite3 Database (not included for security reasons)
- **`app`**
    - `__init__.py`: main Flask file, initialises databases and home page
    - `user.py`: Flask file for sign up and login
    - `feeds.py`: Flask file for #ZoomLife, Memes, Meditations and Support feeds
    - `delivery.py`: Flask file for sending and receiving boxes
    - `helpers.py`: Flask file of helper functions
    - ** `static` **: stored files, CSS and JS
        - *`image-uploads`*: photos and memes
        - *`meditation-audios`*: soundtracks for mediations
        - *`meditation-img`*: images for meditation cards
        - *`vectors`*: vector graphics for icons and backgrounds
        - `animations.js`: animations for home pages
        - `hoverAnimations.js`: animations for sidebar
        - `meditation.js`: control playback of audios
        - `index.css`: CSS for home page
        - `userForms.css`: CSS for sign up, login and welcome pages
        - `feed.css`: CSS for #ZoomLife, Memes and Support feeds
        - `meditations.css`: CSS for Meditation screen
        - `send.css`: CSS for send and receive package screens
    - ** `templates` **: HTML Layouts
        - `index.html`: home page
        - `user-layout.html`: layout for registering and logging in users, base for `login.html`. `register.html`, `introduction.html` and `error.html`
        - `main-layout.html`: layout for feeds, base for `zoomlife.html`, `memes.html`, `meditations.html`, `support.html`
        - `box-layout.html`: layout for sending and receiving boxes, base for `send.html` and `receive.html`

Frameworks used: Flask (Python, HTML), Bootstrap (CSS), Animate.css (CSS, JS)

## Misc

** TO DO LIST **

- [x] Build home screen
- [x] Configure sign up
- [x] Configure log in
- [x] Build basic layout for feed
- [x] Implement four feeds
- [x] Build send package screen
- [x] Configure add items to box
- [x] Configure post boxes
- [x] Build receive package screen
- [x] Configure received boxes
- [x] Configure uploads of boxes to feed
- [x] Jazz up the CSS
- [x] Add transitions
- [x] Add an intro screen
- [x] Reconfigure code styling

*Credits: Michelle Lo*