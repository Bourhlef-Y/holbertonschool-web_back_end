# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

```
Basic_authentication
├─ README.md
├─ api
│  ├─ .DS_Store
│  ├─ __init__.py
│  ├─ __pycache__
│  │  └─ __init__.cpython-312.pyc
│  └─ v1
│     ├─ .DS_Store
│     ├─ __init__.py
│     ├─ __pycache__
│     │  ├─ __init__.cpython-312.pyc
│     │  └─ app.cpython-312.pyc
│     ├─ app.py
│     ├─ auth
│     │  ├─ __init__.py
│     │  ├─ __pycache__
│     │  │  ├─ __init__.cpython-312.pyc
│     │  │  └─ auth.cpython-312.pyc
│     │  ├─ auth.py
│     │  └─ basic_auth.py
│     └─ views
│        ├─ .DS_Store
│        ├─ __init__.py
│        ├─ __pycache__
│        │  ├─ __init__.cpython-312.pyc
│        │  ├─ index.cpython-312.pyc
│        │  └─ users.cpython-312.pyc
│        ├─ index.py
│        └─ users.py
├─ clean_pyc_zone.sh
├─ main_0.py
├─ main_1.py
├─ models
│  ├─ .DS_Store
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-312.pyc
│  │  ├─ base.cpython-312.pyc
│  │  └─ user.cpython-312.pyc
│  ├─ base.py
│  └─ user.py
├─ requirements.txt
└─ venv
   ├─ bin
   │  ├─ Activate.ps1
   │  ├─ activate
   │  ├─ activate.csh
   │  ├─ activate.fish
   │  ├─ chardetect
   │  ├─ flask
   │  ├─ pip
   │  ├─ pip3
   │  ├─ pip3.12
   │  ├─ pycodestyle
   │  ├─ python
   │  ├─ python3
   │  └─ python3.12
   ├─ lib
   │  └─ python3.12
   │     └─ site-packages
   │        ├─ Flask-2.0.3.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE.rst
   │        │  ├─ LICENSE.rst:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ REQUESTED
   │        │  ├─ REQUESTED:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ entry_points.txt
   │        │  ├─ entry_points.txt:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ Flask_Cors-3.0.8.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE
   │        │  ├─ LICENSE:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ REQUESTED
   │        │  ├─ REQUESTED:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ MarkupSafe-2.0.1.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE.rst
   │        │  ├─ LICENSE.rst:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ REQUESTED
   │        │  ├─ REQUESTED:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ Werkzeug-2.0.3.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE.rst
   │        │  ├─ LICENSE.rst:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ REQUESTED
   │        │  ├─ REQUESTED:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ __pycache__
   │        │  ├─ pycodestyle.cpython-312.pyc
   │        │  └─ six.cpython-312.pyc
   │        ├─ certifi
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __main__.py
   │        │  ├─ __main__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ __main__.cpython-312.pyc
   │        │  │  └─ core.cpython-312.pyc
   │        │  ├─ cacert.pem
   │        │  ├─ cacert.pem:Zone.Identifier
   │        │  ├─ core.py
   │        │  ├─ core.py:Zone.Identifier
   │        │  ├─ py.typed
   │        │  └─ py.typed:Zone.Identifier
   │        ├─ certifi-2025.1.31.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE
   │        │  ├─ LICENSE:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ chardet
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ big5freq.cpython-312.pyc
   │        │  │  ├─ big5prober.cpython-312.pyc
   │        │  │  ├─ chardistribution.cpython-312.pyc
   │        │  │  ├─ charsetgroupprober.cpython-312.pyc
   │        │  │  ├─ charsetprober.cpython-312.pyc
   │        │  │  ├─ codingstatemachine.cpython-312.pyc
   │        │  │  ├─ compat.cpython-312.pyc
   │        │  │  ├─ cp949prober.cpython-312.pyc
   │        │  │  ├─ enums.cpython-312.pyc
   │        │  │  ├─ escprober.cpython-312.pyc
   │        │  │  ├─ escsm.cpython-312.pyc
   │        │  │  ├─ eucjpprober.cpython-312.pyc
   │        │  │  ├─ euckrfreq.cpython-312.pyc
   │        │  │  ├─ euckrprober.cpython-312.pyc
   │        │  │  ├─ euctwfreq.cpython-312.pyc
   │        │  │  ├─ euctwprober.cpython-312.pyc
   │        │  │  ├─ gb2312freq.cpython-312.pyc
   │        │  │  ├─ gb2312prober.cpython-312.pyc
   │        │  │  ├─ hebrewprober.cpython-312.pyc
   │        │  │  ├─ jisfreq.cpython-312.pyc
   │        │  │  ├─ jpcntx.cpython-312.pyc
   │        │  │  ├─ langbulgarianmodel.cpython-312.pyc
   │        │  │  ├─ langcyrillicmodel.cpython-312.pyc
   │        │  │  ├─ langgreekmodel.cpython-312.pyc
   │        │  │  ├─ langhebrewmodel.cpython-312.pyc
   │        │  │  ├─ langhungarianmodel.cpython-312.pyc
   │        │  │  ├─ langthaimodel.cpython-312.pyc
   │        │  │  ├─ langturkishmodel.cpython-312.pyc
   │        │  │  ├─ latin1prober.cpython-312.pyc
   │        │  │  ├─ mbcharsetprober.cpython-312.pyc
   │        │  │  ├─ mbcsgroupprober.cpython-312.pyc
   │        │  │  ├─ mbcssm.cpython-312.pyc
   │        │  │  ├─ sbcharsetprober.cpython-312.pyc
   │        │  │  ├─ sbcsgroupprober.cpython-312.pyc
   │        │  │  ├─ sjisprober.cpython-312.pyc
   │        │  │  ├─ universaldetector.cpython-312.pyc
   │        │  │  ├─ utf8prober.cpython-312.pyc
   │        │  │  └─ version.cpython-312.pyc
   │        │  ├─ big5freq.py
   │        │  ├─ big5freq.py:Zone.Identifier
   │        │  ├─ big5prober.py
   │        │  ├─ big5prober.py:Zone.Identifier
   │        │  ├─ chardistribution.py
   │        │  ├─ chardistribution.py:Zone.Identifier
   │        │  ├─ charsetgroupprober.py
   │        │  ├─ charsetgroupprober.py:Zone.Identifier
   │        │  ├─ charsetprober.py
   │        │  ├─ charsetprober.py:Zone.Identifier
   │        │  ├─ cli
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  └─ chardetect.cpython-312.pyc
   │        │  │  ├─ chardetect.py
   │        │  │  └─ chardetect.py:Zone.Identifier
   │        │  ├─ codingstatemachine.py
   │        │  ├─ codingstatemachine.py:Zone.Identifier
   │        │  ├─ compat.py
   │        │  ├─ compat.py:Zone.Identifier
   │        │  ├─ cp949prober.py
   │        │  ├─ cp949prober.py:Zone.Identifier
   │        │  ├─ enums.py
   │        │  ├─ enums.py:Zone.Identifier
   │        │  ├─ escprober.py
   │        │  ├─ escprober.py:Zone.Identifier
   │        │  ├─ escsm.py
   │        │  ├─ escsm.py:Zone.Identifier
   │        │  ├─ eucjpprober.py
   │        │  ├─ eucjpprober.py:Zone.Identifier
   │        │  ├─ euckrfreq.py
   │        │  ├─ euckrfreq.py:Zone.Identifier
   │        │  ├─ euckrprober.py
   │        │  ├─ euckrprober.py:Zone.Identifier
   │        │  ├─ euctwfreq.py
   │        │  ├─ euctwfreq.py:Zone.Identifier
   │        │  ├─ euctwprober.py
   │        │  ├─ euctwprober.py:Zone.Identifier
   │        │  ├─ gb2312freq.py
   │        │  ├─ gb2312freq.py:Zone.Identifier
   │        │  ├─ gb2312prober.py
   │        │  ├─ gb2312prober.py:Zone.Identifier
   │        │  ├─ hebrewprober.py
   │        │  ├─ hebrewprober.py:Zone.Identifier
   │        │  ├─ jisfreq.py
   │        │  ├─ jisfreq.py:Zone.Identifier
   │        │  ├─ jpcntx.py
   │        │  ├─ jpcntx.py:Zone.Identifier
   │        │  ├─ langbulgarianmodel.py
   │        │  ├─ langbulgarianmodel.py:Zone.Identifier
   │        │  ├─ langcyrillicmodel.py
   │        │  ├─ langcyrillicmodel.py:Zone.Identifier
   │        │  ├─ langgreekmodel.py
   │        │  ├─ langgreekmodel.py:Zone.Identifier
   │        │  ├─ langhebrewmodel.py
   │        │  ├─ langhebrewmodel.py:Zone.Identifier
   │        │  ├─ langhungarianmodel.py
   │        │  ├─ langhungarianmodel.py:Zone.Identifier
   │        │  ├─ langthaimodel.py
   │        │  ├─ langthaimodel.py:Zone.Identifier
   │        │  ├─ langturkishmodel.py
   │        │  ├─ langturkishmodel.py:Zone.Identifier
   │        │  ├─ latin1prober.py
   │        │  ├─ latin1prober.py:Zone.Identifier
   │        │  ├─ mbcharsetprober.py
   │        │  ├─ mbcharsetprober.py:Zone.Identifier
   │        │  ├─ mbcsgroupprober.py
   │        │  ├─ mbcsgroupprober.py:Zone.Identifier
   │        │  ├─ mbcssm.py
   │        │  ├─ mbcssm.py:Zone.Identifier
   │        │  ├─ sbcharsetprober.py
   │        │  ├─ sbcharsetprober.py:Zone.Identifier
   │        │  ├─ sbcsgroupprober.py
   │        │  ├─ sbcsgroupprober.py:Zone.Identifier
   │        │  ├─ sjisprober.py
   │        │  ├─ sjisprober.py:Zone.Identifier
   │        │  ├─ universaldetector.py
   │        │  ├─ universaldetector.py:Zone.Identifier
   │        │  ├─ utf8prober.py
   │        │  ├─ utf8prober.py:Zone.Identifier
   │        │  ├─ version.py
   │        │  └─ version.py:Zone.Identifier
   │        ├─ chardet-3.0.4.dist-info
   │        │  ├─ DESCRIPTION.rst
   │        │  ├─ DESCRIPTION.rst:Zone.Identifier
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ entry_points.txt
   │        │  ├─ entry_points.txt:Zone.Identifier
   │        │  ├─ metadata.json
   │        │  ├─ metadata.json:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ click
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ _compat.cpython-312.pyc
   │        │  │  ├─ _termui_impl.cpython-312.pyc
   │        │  │  ├─ _textwrap.cpython-312.pyc
   │        │  │  ├─ _winconsole.cpython-312.pyc
   │        │  │  ├─ core.cpython-312.pyc
   │        │  │  ├─ decorators.cpython-312.pyc
   │        │  │  ├─ exceptions.cpython-312.pyc
   │        │  │  ├─ formatting.cpython-312.pyc
   │        │  │  ├─ globals.cpython-312.pyc
   │        │  │  ├─ parser.cpython-312.pyc
   │        │  │  ├─ shell_completion.cpython-312.pyc
   │        │  │  ├─ termui.cpython-312.pyc
   │        │  │  ├─ testing.cpython-312.pyc
   │        │  │  ├─ types.cpython-312.pyc
   │        │  │  └─ utils.cpython-312.pyc
   │        │  ├─ _compat.py
   │        │  ├─ _compat.py:Zone.Identifier
   │        │  ├─ _termui_impl.py
   │        │  ├─ _termui_impl.py:Zone.Identifier
   │        │  ├─ _textwrap.py
   │        │  ├─ _textwrap.py:Zone.Identifier
   │        │  ├─ _winconsole.py
   │        │  ├─ _winconsole.py:Zone.Identifier
   │        │  ├─ core.py
   │        │  ├─ core.py:Zone.Identifier
   │        │  ├─ decorators.py
   │        │  ├─ decorators.py:Zone.Identifier
   │        │  ├─ exceptions.py
   │        │  ├─ exceptions.py:Zone.Identifier
   │        │  ├─ formatting.py
   │        │  ├─ formatting.py:Zone.Identifier
   │        │  ├─ globals.py
   │        │  ├─ globals.py:Zone.Identifier
   │        │  ├─ parser.py
   │        │  ├─ parser.py:Zone.Identifier
   │        │  ├─ py.typed
   │        │  ├─ py.typed:Zone.Identifier
   │        │  ├─ shell_completion.py
   │        │  ├─ shell_completion.py:Zone.Identifier
   │        │  ├─ termui.py
   │        │  ├─ termui.py:Zone.Identifier
   │        │  ├─ testing.py
   │        │  ├─ testing.py:Zone.Identifier
   │        │  ├─ types.py
   │        │  ├─ types.py:Zone.Identifier
   │        │  ├─ utils.py
   │        │  └─ utils.py:Zone.Identifier
   │        ├─ click-8.1.8.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE.txt
   │        │  ├─ LICENSE.txt:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  └─ WHEEL:Zone.Identifier
   │        ├─ flask
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __main__.py
   │        │  ├─ __main__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ __main__.cpython-312.pyc
   │        │  │  ├─ app.cpython-312.pyc
   │        │  │  ├─ blueprints.cpython-312.pyc
   │        │  │  ├─ cli.cpython-312.pyc
   │        │  │  ├─ config.cpython-312.pyc
   │        │  │  ├─ ctx.cpython-312.pyc
   │        │  │  ├─ debughelpers.cpython-312.pyc
   │        │  │  ├─ globals.cpython-312.pyc
   │        │  │  ├─ helpers.cpython-312.pyc
   │        │  │  ├─ logging.cpython-312.pyc
   │        │  │  ├─ scaffold.cpython-312.pyc
   │        │  │  ├─ sessions.cpython-312.pyc
   │        │  │  ├─ signals.cpython-312.pyc
   │        │  │  ├─ templating.cpython-312.pyc
   │        │  │  ├─ testing.cpython-312.pyc
   │        │  │  ├─ typing.cpython-312.pyc
   │        │  │  ├─ views.cpython-312.pyc
   │        │  │  └─ wrappers.cpython-312.pyc
   │        │  ├─ app.py
   │        │  ├─ app.py:Zone.Identifier
   │        │  ├─ blueprints.py
   │        │  ├─ blueprints.py:Zone.Identifier
   │        │  ├─ cli.py
   │        │  ├─ cli.py:Zone.Identifier
   │        │  ├─ config.py
   │        │  ├─ config.py:Zone.Identifier
   │        │  ├─ ctx.py
   │        │  ├─ ctx.py:Zone.Identifier
   │        │  ├─ debughelpers.py
   │        │  ├─ debughelpers.py:Zone.Identifier
   │        │  ├─ globals.py
   │        │  ├─ globals.py:Zone.Identifier
   │        │  ├─ helpers.py
   │        │  ├─ helpers.py:Zone.Identifier
   │        │  ├─ json
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  └─ tag.cpython-312.pyc
   │        │  │  ├─ tag.py
   │        │  │  └─ tag.py:Zone.Identifier
   │        │  ├─ logging.py
   │        │  ├─ logging.py:Zone.Identifier
   │        │  ├─ py.typed
   │        │  ├─ py.typed:Zone.Identifier
   │        │  ├─ scaffold.py
   │        │  ├─ scaffold.py:Zone.Identifier
   │        │  ├─ sessions.py
   │        │  ├─ sessions.py:Zone.Identifier
   │        │  ├─ signals.py
   │        │  ├─ signals.py:Zone.Identifier
   │        │  ├─ templating.py
   │        │  ├─ templating.py:Zone.Identifier
   │        │  ├─ testing.py
   │        │  ├─ testing.py:Zone.Identifier
   │        │  ├─ typing.py
   │        │  ├─ typing.py:Zone.Identifier
   │        │  ├─ views.py
   │        │  ├─ views.py:Zone.Identifier
   │        │  ├─ wrappers.py
   │        │  └─ wrappers.py:Zone.Identifier
   │        ├─ flask_cors
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ core.cpython-312.pyc
   │        │  │  ├─ decorator.cpython-312.pyc
   │        │  │  ├─ extension.cpython-312.pyc
   │        │  │  └─ version.cpython-312.pyc
   │        │  ├─ core.py
   │        │  ├─ core.py:Zone.Identifier
   │        │  ├─ decorator.py
   │        │  ├─ decorator.py:Zone.Identifier
   │        │  ├─ extension.py
   │        │  ├─ extension.py:Zone.Identifier
   │        │  ├─ version.py
   │        │  └─ version.py:Zone.Identifier
   │        ├─ idna
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ codec.cpython-312.pyc
   │        │  │  ├─ compat.cpython-312.pyc
   │        │  │  ├─ core.cpython-312.pyc
   │        │  │  ├─ idnadata.cpython-312.pyc
   │        │  │  ├─ intranges.cpython-312.pyc
   │        │  │  ├─ package_data.cpython-312.pyc
   │        │  │  └─ uts46data.cpython-312.pyc
   │        │  ├─ codec.py
   │        │  ├─ codec.py:Zone.Identifier
   │        │  ├─ compat.py
   │        │  ├─ compat.py:Zone.Identifier
   │        │  ├─ core.py
   │        │  ├─ core.py:Zone.Identifier
   │        │  ├─ idnadata.py
   │        │  ├─ idnadata.py:Zone.Identifier
   │        │  ├─ intranges.py
   │        │  ├─ intranges.py:Zone.Identifier
   │        │  ├─ package_data.py
   │        │  ├─ package_data.py:Zone.Identifier
   │        │  ├─ uts46data.py
   │        │  └─ uts46data.py:Zone.Identifier
   │        ├─ idna-2.6.dist-info
   │        │  ├─ DESCRIPTION.rst
   │        │  ├─ DESCRIPTION.rst:Zone.Identifier
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ metadata.json
   │        │  ├─ metadata.json:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ itsdangerous
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ _json.cpython-312.pyc
   │        │  │  ├─ encoding.cpython-312.pyc
   │        │  │  ├─ exc.cpython-312.pyc
   │        │  │  ├─ serializer.cpython-312.pyc
   │        │  │  ├─ signer.cpython-312.pyc
   │        │  │  ├─ timed.cpython-312.pyc
   │        │  │  └─ url_safe.cpython-312.pyc
   │        │  ├─ _json.py
   │        │  ├─ _json.py:Zone.Identifier
   │        │  ├─ encoding.py
   │        │  ├─ encoding.py:Zone.Identifier
   │        │  ├─ exc.py
   │        │  ├─ exc.py:Zone.Identifier
   │        │  ├─ py.typed
   │        │  ├─ py.typed:Zone.Identifier
   │        │  ├─ serializer.py
   │        │  ├─ serializer.py:Zone.Identifier
   │        │  ├─ signer.py
   │        │  ├─ signer.py:Zone.Identifier
   │        │  ├─ timed.py
   │        │  ├─ timed.py:Zone.Identifier
   │        │  ├─ url_safe.py
   │        │  └─ url_safe.py:Zone.Identifier
   │        ├─ itsdangerous-2.2.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE.txt
   │        │  ├─ LICENSE.txt:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  └─ WHEEL:Zone.Identifier
   │        ├─ jinja2
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ _identifier.cpython-312.pyc
   │        │  │  ├─ async_utils.cpython-312.pyc
   │        │  │  ├─ bccache.cpython-312.pyc
   │        │  │  ├─ compiler.cpython-312.pyc
   │        │  │  ├─ constants.cpython-312.pyc
   │        │  │  ├─ debug.cpython-312.pyc
   │        │  │  ├─ defaults.cpython-312.pyc
   │        │  │  ├─ environment.cpython-312.pyc
   │        │  │  ├─ exceptions.cpython-312.pyc
   │        │  │  ├─ ext.cpython-312.pyc
   │        │  │  ├─ filters.cpython-312.pyc
   │        │  │  ├─ idtracking.cpython-312.pyc
   │        │  │  ├─ lexer.cpython-312.pyc
   │        │  │  ├─ loaders.cpython-312.pyc
   │        │  │  ├─ meta.cpython-312.pyc
   │        │  │  ├─ nativetypes.cpython-312.pyc
   │        │  │  ├─ nodes.cpython-312.pyc
   │        │  │  ├─ optimizer.cpython-312.pyc
   │        │  │  ├─ parser.cpython-312.pyc
   │        │  │  ├─ runtime.cpython-312.pyc
   │        │  │  ├─ sandbox.cpython-312.pyc
   │        │  │  ├─ tests.cpython-312.pyc
   │        │  │  ├─ utils.cpython-312.pyc
   │        │  │  └─ visitor.cpython-312.pyc
   │        │  ├─ _identifier.py
   │        │  ├─ _identifier.py:Zone.Identifier
   │        │  ├─ async_utils.py
   │        │  ├─ async_utils.py:Zone.Identifier
   │        │  ├─ bccache.py
   │        │  ├─ bccache.py:Zone.Identifier
   │        │  ├─ compiler.py
   │        │  ├─ compiler.py:Zone.Identifier
   │        │  ├─ constants.py
   │        │  ├─ constants.py:Zone.Identifier
   │        │  ├─ debug.py
   │        │  ├─ debug.py:Zone.Identifier
   │        │  ├─ defaults.py
   │        │  ├─ defaults.py:Zone.Identifier
   │        │  ├─ environment.py
   │        │  ├─ environment.py:Zone.Identifier
   │        │  ├─ exceptions.py
   │        │  ├─ exceptions.py:Zone.Identifier
   │        │  ├─ ext.py
   │        │  ├─ ext.py:Zone.Identifier
   │        │  ├─ filters.py
   │        │  ├─ filters.py:Zone.Identifier
   │        │  ├─ idtracking.py
   │        │  ├─ idtracking.py:Zone.Identifier
   │        │  ├─ lexer.py
   │        │  ├─ lexer.py:Zone.Identifier
   │        │  ├─ loaders.py
   │        │  ├─ loaders.py:Zone.Identifier
   │        │  ├─ meta.py
   │        │  ├─ meta.py:Zone.Identifier
   │        │  ├─ nativetypes.py
   │        │  ├─ nativetypes.py:Zone.Identifier
   │        │  ├─ nodes.py
   │        │  ├─ nodes.py:Zone.Identifier
   │        │  ├─ optimizer.py
   │        │  ├─ optimizer.py:Zone.Identifier
   │        │  ├─ parser.py
   │        │  ├─ parser.py:Zone.Identifier
   │        │  ├─ py.typed
   │        │  ├─ py.typed:Zone.Identifier
   │        │  ├─ runtime.py
   │        │  ├─ runtime.py:Zone.Identifier
   │        │  ├─ sandbox.py
   │        │  ├─ sandbox.py:Zone.Identifier
   │        │  ├─ tests.py
   │        │  ├─ tests.py:Zone.Identifier
   │        │  ├─ utils.py
   │        │  ├─ utils.py:Zone.Identifier
   │        │  ├─ visitor.py
   │        │  └─ visitor.py:Zone.Identifier
   │        ├─ jinja2-3.1.5.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE.txt
   │        │  ├─ LICENSE.txt:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ entry_points.txt
   │        │  └─ entry_points.txt:Zone.Identifier
   │        ├─ markupsafe
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  └─ _native.cpython-312.pyc
   │        │  ├─ _native.py
   │        │  ├─ _native.py:Zone.Identifier
   │        │  ├─ _speedups.c
   │        │  ├─ _speedups.c:Zone.Identifier
   │        │  ├─ _speedups.cpython-312-x86_64-linux-gnu.so
   │        │  ├─ _speedups.cpython-312-x86_64-linux-gnu.so:Zone.Identifier
   │        │  ├─ _speedups.pyi
   │        │  ├─ _speedups.pyi:Zone.Identifier
   │        │  ├─ py.typed
   │        │  └─ py.typed:Zone.Identifier
   │        ├─ pip
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __main__.py
   │        │  ├─ __main__.py:Zone.Identifier
   │        │  ├─ __pip-runner__.py
   │        │  ├─ __pip-runner__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ __main__.cpython-312.pyc
   │        │  │  └─ __pip-runner__.cpython-312.pyc
   │        │  ├─ _internal
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  ├─ build_env.cpython-312.pyc
   │        │  │  │  ├─ cache.cpython-312.pyc
   │        │  │  │  ├─ configuration.cpython-312.pyc
   │        │  │  │  ├─ exceptions.cpython-312.pyc
   │        │  │  │  ├─ main.cpython-312.pyc
   │        │  │  │  ├─ pyproject.cpython-312.pyc
   │        │  │  │  ├─ self_outdated_check.cpython-312.pyc
   │        │  │  │  └─ wheel_builder.cpython-312.pyc
   │        │  │  ├─ build_env.py
   │        │  │  ├─ build_env.py:Zone.Identifier
   │        │  │  ├─ cache.py
   │        │  │  ├─ cache.py:Zone.Identifier
   │        │  │  ├─ cli
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ autocompletion.cpython-312.pyc
   │        │  │  │  │  ├─ base_command.cpython-312.pyc
   │        │  │  │  │  ├─ cmdoptions.cpython-312.pyc
   │        │  │  │  │  ├─ command_context.cpython-312.pyc
   │        │  │  │  │  ├─ index_command.cpython-312.pyc
   │        │  │  │  │  ├─ main.cpython-312.pyc
   │        │  │  │  │  ├─ main_parser.cpython-312.pyc
   │        │  │  │  │  ├─ parser.cpython-312.pyc
   │        │  │  │  │  ├─ progress_bars.cpython-312.pyc
   │        │  │  │  │  ├─ req_command.cpython-312.pyc
   │        │  │  │  │  ├─ spinners.cpython-312.pyc
   │        │  │  │  │  └─ status_codes.cpython-312.pyc
   │        │  │  │  ├─ autocompletion.py
   │        │  │  │  ├─ autocompletion.py:Zone.Identifier
   │        │  │  │  ├─ base_command.py
   │        │  │  │  ├─ base_command.py:Zone.Identifier
   │        │  │  │  ├─ cmdoptions.py
   │        │  │  │  ├─ cmdoptions.py:Zone.Identifier
   │        │  │  │  ├─ command_context.py
   │        │  │  │  ├─ command_context.py:Zone.Identifier
   │        │  │  │  ├─ index_command.py
   │        │  │  │  ├─ index_command.py:Zone.Identifier
   │        │  │  │  ├─ main.py
   │        │  │  │  ├─ main.py:Zone.Identifier
   │        │  │  │  ├─ main_parser.py
   │        │  │  │  ├─ main_parser.py:Zone.Identifier
   │        │  │  │  ├─ parser.py
   │        │  │  │  ├─ parser.py:Zone.Identifier
   │        │  │  │  ├─ progress_bars.py
   │        │  │  │  ├─ progress_bars.py:Zone.Identifier
   │        │  │  │  ├─ req_command.py
   │        │  │  │  ├─ req_command.py:Zone.Identifier
   │        │  │  │  ├─ spinners.py
   │        │  │  │  ├─ spinners.py:Zone.Identifier
   │        │  │  │  ├─ status_codes.py
   │        │  │  │  └─ status_codes.py:Zone.Identifier
   │        │  │  ├─ commands
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ cache.cpython-312.pyc
   │        │  │  │  │  ├─ check.cpython-312.pyc
   │        │  │  │  │  ├─ completion.cpython-312.pyc
   │        │  │  │  │  ├─ configuration.cpython-312.pyc
   │        │  │  │  │  ├─ debug.cpython-312.pyc
   │        │  │  │  │  ├─ download.cpython-312.pyc
   │        │  │  │  │  ├─ freeze.cpython-312.pyc
   │        │  │  │  │  ├─ hash.cpython-312.pyc
   │        │  │  │  │  ├─ help.cpython-312.pyc
   │        │  │  │  │  ├─ index.cpython-312.pyc
   │        │  │  │  │  ├─ inspect.cpython-312.pyc
   │        │  │  │  │  ├─ install.cpython-312.pyc
   │        │  │  │  │  ├─ list.cpython-312.pyc
   │        │  │  │  │  ├─ search.cpython-312.pyc
   │        │  │  │  │  ├─ show.cpython-312.pyc
   │        │  │  │  │  ├─ uninstall.cpython-312.pyc
   │        │  │  │  │  └─ wheel.cpython-312.pyc
   │        │  │  │  ├─ cache.py
   │        │  │  │  ├─ cache.py:Zone.Identifier
   │        │  │  │  ├─ check.py
   │        │  │  │  ├─ check.py:Zone.Identifier
   │        │  │  │  ├─ completion.py
   │        │  │  │  ├─ completion.py:Zone.Identifier
   │        │  │  │  ├─ configuration.py
   │        │  │  │  ├─ configuration.py:Zone.Identifier
   │        │  │  │  ├─ debug.py
   │        │  │  │  ├─ debug.py:Zone.Identifier
   │        │  │  │  ├─ download.py
   │        │  │  │  ├─ download.py:Zone.Identifier
   │        │  │  │  ├─ freeze.py
   │        │  │  │  ├─ freeze.py:Zone.Identifier
   │        │  │  │  ├─ hash.py
   │        │  │  │  ├─ hash.py:Zone.Identifier
   │        │  │  │  ├─ help.py
   │        │  │  │  ├─ help.py:Zone.Identifier
   │        │  │  │  ├─ index.py
   │        │  │  │  ├─ index.py:Zone.Identifier
   │        │  │  │  ├─ inspect.py
   │        │  │  │  ├─ inspect.py:Zone.Identifier
   │        │  │  │  ├─ install.py
   │        │  │  │  ├─ install.py:Zone.Identifier
   │        │  │  │  ├─ list.py
   │        │  │  │  ├─ list.py:Zone.Identifier
   │        │  │  │  ├─ search.py
   │        │  │  │  ├─ search.py:Zone.Identifier
   │        │  │  │  ├─ show.py
   │        │  │  │  ├─ show.py:Zone.Identifier
   │        │  │  │  ├─ uninstall.py
   │        │  │  │  ├─ uninstall.py:Zone.Identifier
   │        │  │  │  ├─ wheel.py
   │        │  │  │  └─ wheel.py:Zone.Identifier
   │        │  │  ├─ configuration.py
   │        │  │  ├─ configuration.py:Zone.Identifier
   │        │  │  ├─ distributions
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ base.cpython-312.pyc
   │        │  │  │  │  ├─ installed.cpython-312.pyc
   │        │  │  │  │  ├─ sdist.cpython-312.pyc
   │        │  │  │  │  └─ wheel.cpython-312.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ base.py:Zone.Identifier
   │        │  │  │  ├─ installed.py
   │        │  │  │  ├─ installed.py:Zone.Identifier
   │        │  │  │  ├─ sdist.py
   │        │  │  │  ├─ sdist.py:Zone.Identifier
   │        │  │  │  ├─ wheel.py
   │        │  │  │  └─ wheel.py:Zone.Identifier
   │        │  │  ├─ exceptions.py
   │        │  │  ├─ exceptions.py:Zone.Identifier
   │        │  │  ├─ index
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ collector.cpython-312.pyc
   │        │  │  │  │  ├─ package_finder.cpython-312.pyc
   │        │  │  │  │  └─ sources.cpython-312.pyc
   │        │  │  │  ├─ collector.py
   │        │  │  │  ├─ collector.py:Zone.Identifier
   │        │  │  │  ├─ package_finder.py
   │        │  │  │  ├─ package_finder.py:Zone.Identifier
   │        │  │  │  ├─ sources.py
   │        │  │  │  └─ sources.py:Zone.Identifier
   │        │  │  ├─ locations
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ _distutils.cpython-312.pyc
   │        │  │  │  │  ├─ _sysconfig.cpython-312.pyc
   │        │  │  │  │  └─ base.cpython-312.pyc
   │        │  │  │  ├─ _distutils.py
   │        │  │  │  ├─ _distutils.py:Zone.Identifier
   │        │  │  │  ├─ _sysconfig.py
   │        │  │  │  ├─ _sysconfig.py:Zone.Identifier
   │        │  │  │  ├─ base.py
   │        │  │  │  └─ base.py:Zone.Identifier
   │        │  │  ├─ main.py
   │        │  │  ├─ main.py:Zone.Identifier
   │        │  │  ├─ metadata
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ _json.cpython-312.pyc
   │        │  │  │  │  ├─ base.cpython-312.pyc
   │        │  │  │  │  └─ pkg_resources.cpython-312.pyc
   │        │  │  │  ├─ _json.py
   │        │  │  │  ├─ _json.py:Zone.Identifier
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ base.py:Zone.Identifier
   │        │  │  │  ├─ importlib
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  ├─ _compat.cpython-312.pyc
   │        │  │  │  │  │  ├─ _dists.cpython-312.pyc
   │        │  │  │  │  │  └─ _envs.cpython-312.pyc
   │        │  │  │  │  ├─ _compat.py
   │        │  │  │  │  ├─ _compat.py:Zone.Identifier
   │        │  │  │  │  ├─ _dists.py
   │        │  │  │  │  ├─ _dists.py:Zone.Identifier
   │        │  │  │  │  ├─ _envs.py
   │        │  │  │  │  └─ _envs.py:Zone.Identifier
   │        │  │  │  ├─ pkg_resources.py
   │        │  │  │  └─ pkg_resources.py:Zone.Identifier
   │        │  │  ├─ models
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ candidate.cpython-312.pyc
   │        │  │  │  │  ├─ direct_url.cpython-312.pyc
   │        │  │  │  │  ├─ format_control.cpython-312.pyc
   │        │  │  │  │  ├─ index.cpython-312.pyc
   │        │  │  │  │  ├─ installation_report.cpython-312.pyc
   │        │  │  │  │  ├─ link.cpython-312.pyc
   │        │  │  │  │  ├─ scheme.cpython-312.pyc
   │        │  │  │  │  ├─ search_scope.cpython-312.pyc
   │        │  │  │  │  ├─ selection_prefs.cpython-312.pyc
   │        │  │  │  │  ├─ target_python.cpython-312.pyc
   │        │  │  │  │  └─ wheel.cpython-312.pyc
   │        │  │  │  ├─ candidate.py
   │        │  │  │  ├─ candidate.py:Zone.Identifier
   │        │  │  │  ├─ direct_url.py
   │        │  │  │  ├─ direct_url.py:Zone.Identifier
   │        │  │  │  ├─ format_control.py
   │        │  │  │  ├─ format_control.py:Zone.Identifier
   │        │  │  │  ├─ index.py
   │        │  │  │  ├─ index.py:Zone.Identifier
   │        │  │  │  ├─ installation_report.py
   │        │  │  │  ├─ installation_report.py:Zone.Identifier
   │        │  │  │  ├─ link.py
   │        │  │  │  ├─ link.py:Zone.Identifier
   │        │  │  │  ├─ scheme.py
   │        │  │  │  ├─ scheme.py:Zone.Identifier
   │        │  │  │  ├─ search_scope.py
   │        │  │  │  ├─ search_scope.py:Zone.Identifier
   │        │  │  │  ├─ selection_prefs.py
   │        │  │  │  ├─ selection_prefs.py:Zone.Identifier
   │        │  │  │  ├─ target_python.py
   │        │  │  │  ├─ target_python.py:Zone.Identifier
   │        │  │  │  ├─ wheel.py
   │        │  │  │  └─ wheel.py:Zone.Identifier
   │        │  │  ├─ network
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ auth.cpython-312.pyc
   │        │  │  │  │  ├─ cache.cpython-312.pyc
   │        │  │  │  │  ├─ download.cpython-312.pyc
   │        │  │  │  │  ├─ lazy_wheel.cpython-312.pyc
   │        │  │  │  │  ├─ session.cpython-312.pyc
   │        │  │  │  │  ├─ utils.cpython-312.pyc
   │        │  │  │  │  └─ xmlrpc.cpython-312.pyc
   │        │  │  │  ├─ auth.py
   │        │  │  │  ├─ auth.py:Zone.Identifier
   │        │  │  │  ├─ cache.py
   │        │  │  │  ├─ cache.py:Zone.Identifier
   │        │  │  │  ├─ download.py
   │        │  │  │  ├─ download.py:Zone.Identifier
   │        │  │  │  ├─ lazy_wheel.py
   │        │  │  │  ├─ lazy_wheel.py:Zone.Identifier
   │        │  │  │  ├─ session.py
   │        │  │  │  ├─ session.py:Zone.Identifier
   │        │  │  │  ├─ utils.py
   │        │  │  │  ├─ utils.py:Zone.Identifier
   │        │  │  │  ├─ xmlrpc.py
   │        │  │  │  └─ xmlrpc.py:Zone.Identifier
   │        │  │  ├─ operations
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ check.cpython-312.pyc
   │        │  │  │  │  ├─ freeze.cpython-312.pyc
   │        │  │  │  │  └─ prepare.cpython-312.pyc
   │        │  │  │  ├─ build
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  ├─ build_tracker.cpython-312.pyc
   │        │  │  │  │  │  ├─ metadata.cpython-312.pyc
   │        │  │  │  │  │  ├─ metadata_editable.cpython-312.pyc
   │        │  │  │  │  │  ├─ metadata_legacy.cpython-312.pyc
   │        │  │  │  │  │  ├─ wheel.cpython-312.pyc
   │        │  │  │  │  │  ├─ wheel_editable.cpython-312.pyc
   │        │  │  │  │  │  └─ wheel_legacy.cpython-312.pyc
   │        │  │  │  │  ├─ build_tracker.py
   │        │  │  │  │  ├─ build_tracker.py:Zone.Identifier
   │        │  │  │  │  ├─ metadata.py
   │        │  │  │  │  ├─ metadata.py:Zone.Identifier
   │        │  │  │  │  ├─ metadata_editable.py
   │        │  │  │  │  ├─ metadata_editable.py:Zone.Identifier
   │        │  │  │  │  ├─ metadata_legacy.py
   │        │  │  │  │  ├─ metadata_legacy.py:Zone.Identifier
   │        │  │  │  │  ├─ wheel.py
   │        │  │  │  │  ├─ wheel.py:Zone.Identifier
   │        │  │  │  │  ├─ wheel_editable.py
   │        │  │  │  │  ├─ wheel_editable.py:Zone.Identifier
   │        │  │  │  │  ├─ wheel_legacy.py
   │        │  │  │  │  └─ wheel_legacy.py:Zone.Identifier
   │        │  │  │  ├─ check.py
   │        │  │  │  ├─ check.py:Zone.Identifier
   │        │  │  │  ├─ freeze.py
   │        │  │  │  ├─ freeze.py:Zone.Identifier
   │        │  │  │  ├─ install
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  ├─ editable_legacy.cpython-312.pyc
   │        │  │  │  │  │  └─ wheel.cpython-312.pyc
   │        │  │  │  │  ├─ editable_legacy.py
   │        │  │  │  │  ├─ editable_legacy.py:Zone.Identifier
   │        │  │  │  │  ├─ wheel.py
   │        │  │  │  │  └─ wheel.py:Zone.Identifier
   │        │  │  │  ├─ prepare.py
   │        │  │  │  └─ prepare.py:Zone.Identifier
   │        │  │  ├─ pyproject.py
   │        │  │  ├─ pyproject.py:Zone.Identifier
   │        │  │  ├─ req
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ constructors.cpython-312.pyc
   │        │  │  │  │  ├─ req_file.cpython-312.pyc
   │        │  │  │  │  ├─ req_install.cpython-312.pyc
   │        │  │  │  │  ├─ req_set.cpython-312.pyc
   │        │  │  │  │  └─ req_uninstall.cpython-312.pyc
   │        │  │  │  ├─ constructors.py
   │        │  │  │  ├─ constructors.py:Zone.Identifier
   │        │  │  │  ├─ req_file.py
   │        │  │  │  ├─ req_file.py:Zone.Identifier
   │        │  │  │  ├─ req_install.py
   │        │  │  │  ├─ req_install.py:Zone.Identifier
   │        │  │  │  ├─ req_set.py
   │        │  │  │  ├─ req_set.py:Zone.Identifier
   │        │  │  │  ├─ req_uninstall.py
   │        │  │  │  └─ req_uninstall.py:Zone.Identifier
   │        │  │  ├─ resolution
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  └─ base.cpython-312.pyc
   │        │  │  │  ├─ base.py
   │        │  │  │  ├─ base.py:Zone.Identifier
   │        │  │  │  ├─ legacy
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  └─ resolver.cpython-312.pyc
   │        │  │  │  │  ├─ resolver.py
   │        │  │  │  │  └─ resolver.py:Zone.Identifier
   │        │  │  │  └─ resolvelib
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __init__.py:Zone.Identifier
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-312.pyc
   │        │  │  │     │  ├─ base.cpython-312.pyc
   │        │  │  │     │  ├─ candidates.cpython-312.pyc
   │        │  │  │     │  ├─ factory.cpython-312.pyc
   │        │  │  │     │  ├─ found_candidates.cpython-312.pyc
   │        │  │  │     │  ├─ provider.cpython-312.pyc
   │        │  │  │     │  ├─ reporter.cpython-312.pyc
   │        │  │  │     │  ├─ requirements.cpython-312.pyc
   │        │  │  │     │  └─ resolver.cpython-312.pyc
   │        │  │  │     ├─ base.py
   │        │  │  │     ├─ base.py:Zone.Identifier
   │        │  │  │     ├─ candidates.py
   │        │  │  │     ├─ candidates.py:Zone.Identifier
   │        │  │  │     ├─ factory.py
   │        │  │  │     ├─ factory.py:Zone.Identifier
   │        │  │  │     ├─ found_candidates.py
   │        │  │  │     ├─ found_candidates.py:Zone.Identifier
   │        │  │  │     ├─ provider.py
   │        │  │  │     ├─ provider.py:Zone.Identifier
   │        │  │  │     ├─ reporter.py
   │        │  │  │     ├─ reporter.py:Zone.Identifier
   │        │  │  │     ├─ requirements.py
   │        │  │  │     ├─ requirements.py:Zone.Identifier
   │        │  │  │     ├─ resolver.py
   │        │  │  │     └─ resolver.py:Zone.Identifier
   │        │  │  ├─ self_outdated_check.py
   │        │  │  ├─ self_outdated_check.py:Zone.Identifier
   │        │  │  ├─ utils
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ _jaraco_text.cpython-312.pyc
   │        │  │  │  │  ├─ _log.cpython-312.pyc
   │        │  │  │  │  ├─ appdirs.cpython-312.pyc
   │        │  │  │  │  ├─ compat.cpython-312.pyc
   │        │  │  │  │  ├─ compatibility_tags.cpython-312.pyc
   │        │  │  │  │  ├─ datetime.cpython-312.pyc
   │        │  │  │  │  ├─ deprecation.cpython-312.pyc
   │        │  │  │  │  ├─ direct_url_helpers.cpython-312.pyc
   │        │  │  │  │  ├─ egg_link.cpython-312.pyc
   │        │  │  │  │  ├─ entrypoints.cpython-312.pyc
   │        │  │  │  │  ├─ filesystem.cpython-312.pyc
   │        │  │  │  │  ├─ filetypes.cpython-312.pyc
   │        │  │  │  │  ├─ glibc.cpython-312.pyc
   │        │  │  │  │  ├─ hashes.cpython-312.pyc
   │        │  │  │  │  ├─ logging.cpython-312.pyc
   │        │  │  │  │  ├─ misc.cpython-312.pyc
   │        │  │  │  │  ├─ packaging.cpython-312.pyc
   │        │  │  │  │  ├─ retry.cpython-312.pyc
   │        │  │  │  │  ├─ setuptools_build.cpython-312.pyc
   │        │  │  │  │  ├─ subprocess.cpython-312.pyc
   │        │  │  │  │  ├─ temp_dir.cpython-312.pyc
   │        │  │  │  │  ├─ unpacking.cpython-312.pyc
   │        │  │  │  │  ├─ urls.cpython-312.pyc
   │        │  │  │  │  ├─ virtualenv.cpython-312.pyc
   │        │  │  │  │  └─ wheel.cpython-312.pyc
   │        │  │  │  ├─ _jaraco_text.py
   │        │  │  │  ├─ _jaraco_text.py:Zone.Identifier
   │        │  │  │  ├─ _log.py
   │        │  │  │  ├─ _log.py:Zone.Identifier
   │        │  │  │  ├─ appdirs.py
   │        │  │  │  ├─ appdirs.py:Zone.Identifier
   │        │  │  │  ├─ compat.py
   │        │  │  │  ├─ compat.py:Zone.Identifier
   │        │  │  │  ├─ compatibility_tags.py
   │        │  │  │  ├─ compatibility_tags.py:Zone.Identifier
   │        │  │  │  ├─ datetime.py
   │        │  │  │  ├─ datetime.py:Zone.Identifier
   │        │  │  │  ├─ deprecation.py
   │        │  │  │  ├─ deprecation.py:Zone.Identifier
   │        │  │  │  ├─ direct_url_helpers.py
   │        │  │  │  ├─ direct_url_helpers.py:Zone.Identifier
   │        │  │  │  ├─ egg_link.py
   │        │  │  │  ├─ egg_link.py:Zone.Identifier
   │        │  │  │  ├─ entrypoints.py
   │        │  │  │  ├─ entrypoints.py:Zone.Identifier
   │        │  │  │  ├─ filesystem.py
   │        │  │  │  ├─ filesystem.py:Zone.Identifier
   │        │  │  │  ├─ filetypes.py
   │        │  │  │  ├─ filetypes.py:Zone.Identifier
   │        │  │  │  ├─ glibc.py
   │        │  │  │  ├─ glibc.py:Zone.Identifier
   │        │  │  │  ├─ hashes.py
   │        │  │  │  ├─ hashes.py:Zone.Identifier
   │        │  │  │  ├─ logging.py
   │        │  │  │  ├─ logging.py:Zone.Identifier
   │        │  │  │  ├─ misc.py
   │        │  │  │  ├─ misc.py:Zone.Identifier
   │        │  │  │  ├─ packaging.py
   │        │  │  │  ├─ packaging.py:Zone.Identifier
   │        │  │  │  ├─ retry.py
   │        │  │  │  ├─ retry.py:Zone.Identifier
   │        │  │  │  ├─ setuptools_build.py
   │        │  │  │  ├─ setuptools_build.py:Zone.Identifier
   │        │  │  │  ├─ subprocess.py
   │        │  │  │  ├─ subprocess.py:Zone.Identifier
   │        │  │  │  ├─ temp_dir.py
   │        │  │  │  ├─ temp_dir.py:Zone.Identifier
   │        │  │  │  ├─ unpacking.py
   │        │  │  │  ├─ unpacking.py:Zone.Identifier
   │        │  │  │  ├─ urls.py
   │        │  │  │  ├─ urls.py:Zone.Identifier
   │        │  │  │  ├─ virtualenv.py
   │        │  │  │  ├─ virtualenv.py:Zone.Identifier
   │        │  │  │  ├─ wheel.py
   │        │  │  │  └─ wheel.py:Zone.Identifier
   │        │  │  ├─ vcs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ bazaar.cpython-312.pyc
   │        │  │  │  │  ├─ git.cpython-312.pyc
   │        │  │  │  │  ├─ mercurial.cpython-312.pyc
   │        │  │  │  │  ├─ subversion.cpython-312.pyc
   │        │  │  │  │  └─ versioncontrol.cpython-312.pyc
   │        │  │  │  ├─ bazaar.py
   │        │  │  │  ├─ bazaar.py:Zone.Identifier
   │        │  │  │  ├─ git.py
   │        │  │  │  ├─ git.py:Zone.Identifier
   │        │  │  │  ├─ mercurial.py
   │        │  │  │  ├─ mercurial.py:Zone.Identifier
   │        │  │  │  ├─ subversion.py
   │        │  │  │  ├─ subversion.py:Zone.Identifier
   │        │  │  │  ├─ versioncontrol.py
   │        │  │  │  └─ versioncontrol.py:Zone.Identifier
   │        │  │  ├─ wheel_builder.py
   │        │  │  └─ wheel_builder.py:Zone.Identifier
   │        │  ├─ _vendor
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  └─ typing_extensions.cpython-312.pyc
   │        │  │  ├─ cachecontrol
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ _cmd.cpython-312.pyc
   │        │  │  │  │  ├─ adapter.cpython-312.pyc
   │        │  │  │  │  ├─ cache.cpython-312.pyc
   │        │  │  │  │  ├─ controller.cpython-312.pyc
   │        │  │  │  │  ├─ filewrapper.cpython-312.pyc
   │        │  │  │  │  ├─ heuristics.cpython-312.pyc
   │        │  │  │  │  ├─ serialize.cpython-312.pyc
   │        │  │  │  │  └─ wrapper.cpython-312.pyc
   │        │  │  │  ├─ _cmd.py
   │        │  │  │  ├─ _cmd.py:Zone.Identifier
   │        │  │  │  ├─ adapter.py
   │        │  │  │  ├─ adapter.py:Zone.Identifier
   │        │  │  │  ├─ cache.py
   │        │  │  │  ├─ cache.py:Zone.Identifier
   │        │  │  │  ├─ caches
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  ├─ file_cache.cpython-312.pyc
   │        │  │  │  │  │  └─ redis_cache.cpython-312.pyc
   │        │  │  │  │  ├─ file_cache.py
   │        │  │  │  │  ├─ file_cache.py:Zone.Identifier
   │        │  │  │  │  ├─ redis_cache.py
   │        │  │  │  │  └─ redis_cache.py:Zone.Identifier
   │        │  │  │  ├─ controller.py
   │        │  │  │  ├─ controller.py:Zone.Identifier
   │        │  │  │  ├─ filewrapper.py
   │        │  │  │  ├─ filewrapper.py:Zone.Identifier
   │        │  │  │  ├─ heuristics.py
   │        │  │  │  ├─ heuristics.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ py.typed:Zone.Identifier
   │        │  │  │  ├─ serialize.py
   │        │  │  │  ├─ serialize.py:Zone.Identifier
   │        │  │  │  ├─ wrapper.py
   │        │  │  │  └─ wrapper.py:Zone.Identifier
   │        │  │  ├─ certifi
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __main__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ __main__.cpython-312.pyc
   │        │  │  │  │  └─ core.cpython-312.pyc
   │        │  │  │  ├─ cacert.pem
   │        │  │  │  ├─ cacert.pem:Zone.Identifier
   │        │  │  │  ├─ core.py
   │        │  │  │  ├─ core.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  └─ py.typed:Zone.Identifier
   │        │  │  ├─ distlib
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ compat.cpython-312.pyc
   │        │  │  │  │  ├─ database.cpython-312.pyc
   │        │  │  │  │  ├─ index.cpython-312.pyc
   │        │  │  │  │  ├─ locators.cpython-312.pyc
   │        │  │  │  │  ├─ manifest.cpython-312.pyc
   │        │  │  │  │  ├─ markers.cpython-312.pyc
   │        │  │  │  │  ├─ metadata.cpython-312.pyc
   │        │  │  │  │  ├─ resources.cpython-312.pyc
   │        │  │  │  │  ├─ scripts.cpython-312.pyc
   │        │  │  │  │  ├─ util.cpython-312.pyc
   │        │  │  │  │  ├─ version.cpython-312.pyc
   │        │  │  │  │  └─ wheel.cpython-312.pyc
   │        │  │  │  ├─ compat.py
   │        │  │  │  ├─ compat.py:Zone.Identifier
   │        │  │  │  ├─ database.py
   │        │  │  │  ├─ database.py:Zone.Identifier
   │        │  │  │  ├─ index.py
   │        │  │  │  ├─ index.py:Zone.Identifier
   │        │  │  │  ├─ locators.py
   │        │  │  │  ├─ locators.py:Zone.Identifier
   │        │  │  │  ├─ manifest.py
   │        │  │  │  ├─ manifest.py:Zone.Identifier
   │        │  │  │  ├─ markers.py
   │        │  │  │  ├─ markers.py:Zone.Identifier
   │        │  │  │  ├─ metadata.py
   │        │  │  │  ├─ metadata.py:Zone.Identifier
   │        │  │  │  ├─ resources.py
   │        │  │  │  ├─ resources.py:Zone.Identifier
   │        │  │  │  ├─ scripts.py
   │        │  │  │  ├─ scripts.py:Zone.Identifier
   │        │  │  │  ├─ t32.exe
   │        │  │  │  ├─ t32.exe:Zone.Identifier
   │        │  │  │  ├─ t64-arm.exe
   │        │  │  │  ├─ t64-arm.exe:Zone.Identifier
   │        │  │  │  ├─ t64.exe
   │        │  │  │  ├─ t64.exe:Zone.Identifier
   │        │  │  │  ├─ util.py
   │        │  │  │  ├─ util.py:Zone.Identifier
   │        │  │  │  ├─ version.py
   │        │  │  │  ├─ version.py:Zone.Identifier
   │        │  │  │  ├─ w32.exe
   │        │  │  │  ├─ w32.exe:Zone.Identifier
   │        │  │  │  ├─ w64-arm.exe
   │        │  │  │  ├─ w64-arm.exe:Zone.Identifier
   │        │  │  │  ├─ w64.exe
   │        │  │  │  ├─ w64.exe:Zone.Identifier
   │        │  │  │  ├─ wheel.py
   │        │  │  │  └─ wheel.py:Zone.Identifier
   │        │  │  ├─ distro
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __main__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ __main__.cpython-312.pyc
   │        │  │  │  │  └─ distro.cpython-312.pyc
   │        │  │  │  ├─ distro.py
   │        │  │  │  ├─ distro.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  └─ py.typed:Zone.Identifier
   │        │  │  ├─ idna
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ codec.cpython-312.pyc
   │        │  │  │  │  ├─ compat.cpython-312.pyc
   │        │  │  │  │  ├─ core.cpython-312.pyc
   │        │  │  │  │  ├─ idnadata.cpython-312.pyc
   │        │  │  │  │  ├─ intranges.cpython-312.pyc
   │        │  │  │  │  ├─ package_data.cpython-312.pyc
   │        │  │  │  │  └─ uts46data.cpython-312.pyc
   │        │  │  │  ├─ codec.py
   │        │  │  │  ├─ codec.py:Zone.Identifier
   │        │  │  │  ├─ compat.py
   │        │  │  │  ├─ compat.py:Zone.Identifier
   │        │  │  │  ├─ core.py
   │        │  │  │  ├─ core.py:Zone.Identifier
   │        │  │  │  ├─ idnadata.py
   │        │  │  │  ├─ idnadata.py:Zone.Identifier
   │        │  │  │  ├─ intranges.py
   │        │  │  │  ├─ intranges.py:Zone.Identifier
   │        │  │  │  ├─ package_data.py
   │        │  │  │  ├─ package_data.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ py.typed:Zone.Identifier
   │        │  │  │  ├─ uts46data.py
   │        │  │  │  └─ uts46data.py:Zone.Identifier
   │        │  │  ├─ msgpack
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ exceptions.cpython-312.pyc
   │        │  │  │  │  ├─ ext.cpython-312.pyc
   │        │  │  │  │  └─ fallback.cpython-312.pyc
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ exceptions.py:Zone.Identifier
   │        │  │  │  ├─ ext.py
   │        │  │  │  ├─ ext.py:Zone.Identifier
   │        │  │  │  ├─ fallback.py
   │        │  │  │  └─ fallback.py:Zone.Identifier
   │        │  │  ├─ packaging
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ _elffile.cpython-312.pyc
   │        │  │  │  │  ├─ _manylinux.cpython-312.pyc
   │        │  │  │  │  ├─ _musllinux.cpython-312.pyc
   │        │  │  │  │  ├─ _parser.cpython-312.pyc
   │        │  │  │  │  ├─ _structures.cpython-312.pyc
   │        │  │  │  │  ├─ _tokenizer.cpython-312.pyc
   │        │  │  │  │  ├─ markers.cpython-312.pyc
   │        │  │  │  │  ├─ metadata.cpython-312.pyc
   │        │  │  │  │  ├─ requirements.cpython-312.pyc
   │        │  │  │  │  ├─ specifiers.cpython-312.pyc
   │        │  │  │  │  ├─ tags.cpython-312.pyc
   │        │  │  │  │  ├─ utils.cpython-312.pyc
   │        │  │  │  │  └─ version.cpython-312.pyc
   │        │  │  │  ├─ _elffile.py
   │        │  │  │  ├─ _elffile.py:Zone.Identifier
   │        │  │  │  ├─ _manylinux.py
   │        │  │  │  ├─ _manylinux.py:Zone.Identifier
   │        │  │  │  ├─ _musllinux.py
   │        │  │  │  ├─ _musllinux.py:Zone.Identifier
   │        │  │  │  ├─ _parser.py
   │        │  │  │  ├─ _parser.py:Zone.Identifier
   │        │  │  │  ├─ _structures.py
   │        │  │  │  ├─ _structures.py:Zone.Identifier
   │        │  │  │  ├─ _tokenizer.py
   │        │  │  │  ├─ _tokenizer.py:Zone.Identifier
   │        │  │  │  ├─ licenses
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  └─ _spdx.cpython-312.pyc
   │        │  │  │  │  ├─ _spdx.py
   │        │  │  │  │  └─ _spdx.py:Zone.Identifier
   │        │  │  │  ├─ markers.py
   │        │  │  │  ├─ markers.py:Zone.Identifier
   │        │  │  │  ├─ metadata.py
   │        │  │  │  ├─ metadata.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ py.typed:Zone.Identifier
   │        │  │  │  ├─ requirements.py
   │        │  │  │  ├─ requirements.py:Zone.Identifier
   │        │  │  │  ├─ specifiers.py
   │        │  │  │  ├─ specifiers.py:Zone.Identifier
   │        │  │  │  ├─ tags.py
   │        │  │  │  ├─ tags.py:Zone.Identifier
   │        │  │  │  ├─ utils.py
   │        │  │  │  ├─ utils.py:Zone.Identifier
   │        │  │  │  ├─ version.py
   │        │  │  │  └─ version.py:Zone.Identifier
   │        │  │  ├─ pkg_resources
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  └─ __pycache__
   │        │  │  │     └─ __init__.cpython-312.pyc
   │        │  │  ├─ platformdirs
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __main__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ __main__.cpython-312.pyc
   │        │  │  │  │  ├─ android.cpython-312.pyc
   │        │  │  │  │  ├─ api.cpython-312.pyc
   │        │  │  │  │  ├─ macos.cpython-312.pyc
   │        │  │  │  │  ├─ unix.cpython-312.pyc
   │        │  │  │  │  ├─ version.cpython-312.pyc
   │        │  │  │  │  └─ windows.cpython-312.pyc
   │        │  │  │  ├─ android.py
   │        │  │  │  ├─ android.py:Zone.Identifier
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ api.py:Zone.Identifier
   │        │  │  │  ├─ macos.py
   │        │  │  │  ├─ macos.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ py.typed:Zone.Identifier
   │        │  │  │  ├─ unix.py
   │        │  │  │  ├─ unix.py:Zone.Identifier
   │        │  │  │  ├─ version.py
   │        │  │  │  ├─ version.py:Zone.Identifier
   │        │  │  │  ├─ windows.py
   │        │  │  │  └─ windows.py:Zone.Identifier
   │        │  │  ├─ pygments
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __main__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ __main__.cpython-312.pyc
   │        │  │  │  │  ├─ cmdline.cpython-312.pyc
   │        │  │  │  │  ├─ console.cpython-312.pyc
   │        │  │  │  │  ├─ filter.cpython-312.pyc
   │        │  │  │  │  ├─ formatter.cpython-312.pyc
   │        │  │  │  │  ├─ lexer.cpython-312.pyc
   │        │  │  │  │  ├─ modeline.cpython-312.pyc
   │        │  │  │  │  ├─ plugin.cpython-312.pyc
   │        │  │  │  │  ├─ regexopt.cpython-312.pyc
   │        │  │  │  │  ├─ scanner.cpython-312.pyc
   │        │  │  │  │  ├─ sphinxext.cpython-312.pyc
   │        │  │  │  │  ├─ style.cpython-312.pyc
   │        │  │  │  │  ├─ token.cpython-312.pyc
   │        │  │  │  │  ├─ unistring.cpython-312.pyc
   │        │  │  │  │  └─ util.cpython-312.pyc
   │        │  │  │  ├─ cmdline.py
   │        │  │  │  ├─ cmdline.py:Zone.Identifier
   │        │  │  │  ├─ console.py
   │        │  │  │  ├─ console.py:Zone.Identifier
   │        │  │  │  ├─ filter.py
   │        │  │  │  ├─ filter.py:Zone.Identifier
   │        │  │  │  ├─ filters
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  └─ __pycache__
   │        │  │  │  │     └─ __init__.cpython-312.pyc
   │        │  │  │  ├─ formatter.py
   │        │  │  │  ├─ formatter.py:Zone.Identifier
   │        │  │  │  ├─ formatters
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  ├─ _mapping.cpython-312.pyc
   │        │  │  │  │  │  ├─ bbcode.cpython-312.pyc
   │        │  │  │  │  │  ├─ groff.cpython-312.pyc
   │        │  │  │  │  │  ├─ html.cpython-312.pyc
   │        │  │  │  │  │  ├─ img.cpython-312.pyc
   │        │  │  │  │  │  ├─ irc.cpython-312.pyc
   │        │  │  │  │  │  ├─ latex.cpython-312.pyc
   │        │  │  │  │  │  ├─ other.cpython-312.pyc
   │        │  │  │  │  │  ├─ pangomarkup.cpython-312.pyc
   │        │  │  │  │  │  ├─ rtf.cpython-312.pyc
   │        │  │  │  │  │  ├─ svg.cpython-312.pyc
   │        │  │  │  │  │  ├─ terminal.cpython-312.pyc
   │        │  │  │  │  │  └─ terminal256.cpython-312.pyc
   │        │  │  │  │  ├─ _mapping.py
   │        │  │  │  │  ├─ _mapping.py:Zone.Identifier
   │        │  │  │  │  ├─ bbcode.py
   │        │  │  │  │  ├─ bbcode.py:Zone.Identifier
   │        │  │  │  │  ├─ groff.py
   │        │  │  │  │  ├─ groff.py:Zone.Identifier
   │        │  │  │  │  ├─ html.py
   │        │  │  │  │  ├─ html.py:Zone.Identifier
   │        │  │  │  │  ├─ img.py
   │        │  │  │  │  ├─ img.py:Zone.Identifier
   │        │  │  │  │  ├─ irc.py
   │        │  │  │  │  ├─ irc.py:Zone.Identifier
   │        │  │  │  │  ├─ latex.py
   │        │  │  │  │  ├─ latex.py:Zone.Identifier
   │        │  │  │  │  ├─ other.py
   │        │  │  │  │  ├─ other.py:Zone.Identifier
   │        │  │  │  │  ├─ pangomarkup.py
   │        │  │  │  │  ├─ pangomarkup.py:Zone.Identifier
   │        │  │  │  │  ├─ rtf.py
   │        │  │  │  │  ├─ rtf.py:Zone.Identifier
   │        │  │  │  │  ├─ svg.py
   │        │  │  │  │  ├─ svg.py:Zone.Identifier
   │        │  │  │  │  ├─ terminal.py
   │        │  │  │  │  ├─ terminal.py:Zone.Identifier
   │        │  │  │  │  ├─ terminal256.py
   │        │  │  │  │  └─ terminal256.py:Zone.Identifier
   │        │  │  │  ├─ lexer.py
   │        │  │  │  ├─ lexer.py:Zone.Identifier
   │        │  │  │  ├─ lexers
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  ├─ _mapping.cpython-312.pyc
   │        │  │  │  │  │  └─ python.cpython-312.pyc
   │        │  │  │  │  ├─ _mapping.py
   │        │  │  │  │  ├─ _mapping.py:Zone.Identifier
   │        │  │  │  │  ├─ python.py
   │        │  │  │  │  └─ python.py:Zone.Identifier
   │        │  │  │  ├─ modeline.py
   │        │  │  │  ├─ modeline.py:Zone.Identifier
   │        │  │  │  ├─ plugin.py
   │        │  │  │  ├─ plugin.py:Zone.Identifier
   │        │  │  │  ├─ regexopt.py
   │        │  │  │  ├─ regexopt.py:Zone.Identifier
   │        │  │  │  ├─ scanner.py
   │        │  │  │  ├─ scanner.py:Zone.Identifier
   │        │  │  │  ├─ sphinxext.py
   │        │  │  │  ├─ sphinxext.py:Zone.Identifier
   │        │  │  │  ├─ style.py
   │        │  │  │  ├─ style.py:Zone.Identifier
   │        │  │  │  ├─ styles
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  └─ _mapping.cpython-312.pyc
   │        │  │  │  │  ├─ _mapping.py
   │        │  │  │  │  └─ _mapping.py:Zone.Identifier
   │        │  │  │  ├─ token.py
   │        │  │  │  ├─ token.py:Zone.Identifier
   │        │  │  │  ├─ unistring.py
   │        │  │  │  ├─ unistring.py:Zone.Identifier
   │        │  │  │  ├─ util.py
   │        │  │  │  └─ util.py:Zone.Identifier
   │        │  │  ├─ pyproject_hooks
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  └─ _impl.cpython-312.pyc
   │        │  │  │  ├─ _impl.py
   │        │  │  │  ├─ _impl.py:Zone.Identifier
   │        │  │  │  ├─ _in_process
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  └─ _in_process.cpython-312.pyc
   │        │  │  │  │  ├─ _in_process.py
   │        │  │  │  │  └─ _in_process.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  └─ py.typed:Zone.Identifier
   │        │  │  ├─ requests
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ __version__.cpython-312.pyc
   │        │  │  │  │  ├─ _internal_utils.cpython-312.pyc
   │        │  │  │  │  ├─ adapters.cpython-312.pyc
   │        │  │  │  │  ├─ api.cpython-312.pyc
   │        │  │  │  │  ├─ auth.cpython-312.pyc
   │        │  │  │  │  ├─ certs.cpython-312.pyc
   │        │  │  │  │  ├─ compat.cpython-312.pyc
   │        │  │  │  │  ├─ cookies.cpython-312.pyc
   │        │  │  │  │  ├─ exceptions.cpython-312.pyc
   │        │  │  │  │  ├─ help.cpython-312.pyc
   │        │  │  │  │  ├─ hooks.cpython-312.pyc
   │        │  │  │  │  ├─ models.cpython-312.pyc
   │        │  │  │  │  ├─ packages.cpython-312.pyc
   │        │  │  │  │  ├─ sessions.cpython-312.pyc
   │        │  │  │  │  ├─ status_codes.cpython-312.pyc
   │        │  │  │  │  ├─ structures.cpython-312.pyc
   │        │  │  │  │  └─ utils.cpython-312.pyc
   │        │  │  │  ├─ __version__.py
   │        │  │  │  ├─ __version__.py:Zone.Identifier
   │        │  │  │  ├─ _internal_utils.py
   │        │  │  │  ├─ _internal_utils.py:Zone.Identifier
   │        │  │  │  ├─ adapters.py
   │        │  │  │  ├─ adapters.py:Zone.Identifier
   │        │  │  │  ├─ api.py
   │        │  │  │  ├─ api.py:Zone.Identifier
   │        │  │  │  ├─ auth.py
   │        │  │  │  ├─ auth.py:Zone.Identifier
   │        │  │  │  ├─ certs.py
   │        │  │  │  ├─ certs.py:Zone.Identifier
   │        │  │  │  ├─ compat.py
   │        │  │  │  ├─ compat.py:Zone.Identifier
   │        │  │  │  ├─ cookies.py
   │        │  │  │  ├─ cookies.py:Zone.Identifier
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ exceptions.py:Zone.Identifier
   │        │  │  │  ├─ help.py
   │        │  │  │  ├─ help.py:Zone.Identifier
   │        │  │  │  ├─ hooks.py
   │        │  │  │  ├─ hooks.py:Zone.Identifier
   │        │  │  │  ├─ models.py
   │        │  │  │  ├─ models.py:Zone.Identifier
   │        │  │  │  ├─ packages.py
   │        │  │  │  ├─ packages.py:Zone.Identifier
   │        │  │  │  ├─ sessions.py
   │        │  │  │  ├─ sessions.py:Zone.Identifier
   │        │  │  │  ├─ status_codes.py
   │        │  │  │  ├─ status_codes.py:Zone.Identifier
   │        │  │  │  ├─ structures.py
   │        │  │  │  ├─ structures.py:Zone.Identifier
   │        │  │  │  ├─ utils.py
   │        │  │  │  └─ utils.py:Zone.Identifier
   │        │  │  ├─ resolvelib
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ providers.cpython-312.pyc
   │        │  │  │  │  ├─ reporters.cpython-312.pyc
   │        │  │  │  │  ├─ resolvers.cpython-312.pyc
   │        │  │  │  │  └─ structs.cpython-312.pyc
   │        │  │  │  ├─ compat
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  └─ collections_abc.cpython-312.pyc
   │        │  │  │  │  ├─ collections_abc.py
   │        │  │  │  │  └─ collections_abc.py:Zone.Identifier
   │        │  │  │  ├─ providers.py
   │        │  │  │  ├─ providers.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ py.typed:Zone.Identifier
   │        │  │  │  ├─ reporters.py
   │        │  │  │  ├─ reporters.py:Zone.Identifier
   │        │  │  │  ├─ resolvers.py
   │        │  │  │  ├─ resolvers.py:Zone.Identifier
   │        │  │  │  ├─ structs.py
   │        │  │  │  └─ structs.py:Zone.Identifier
   │        │  │  ├─ rich
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __main__.py
   │        │  │  │  ├─ __main__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ __main__.cpython-312.pyc
   │        │  │  │  │  ├─ _cell_widths.cpython-312.pyc
   │        │  │  │  │  ├─ _emoji_codes.cpython-312.pyc
   │        │  │  │  │  ├─ _emoji_replace.cpython-312.pyc
   │        │  │  │  │  ├─ _export_format.cpython-312.pyc
   │        │  │  │  │  ├─ _extension.cpython-312.pyc
   │        │  │  │  │  ├─ _fileno.cpython-312.pyc
   │        │  │  │  │  ├─ _inspect.cpython-312.pyc
   │        │  │  │  │  ├─ _log_render.cpython-312.pyc
   │        │  │  │  │  ├─ _loop.cpython-312.pyc
   │        │  │  │  │  ├─ _null_file.cpython-312.pyc
   │        │  │  │  │  ├─ _palettes.cpython-312.pyc
   │        │  │  │  │  ├─ _pick.cpython-312.pyc
   │        │  │  │  │  ├─ _ratio.cpython-312.pyc
   │        │  │  │  │  ├─ _spinners.cpython-312.pyc
   │        │  │  │  │  ├─ _stack.cpython-312.pyc
   │        │  │  │  │  ├─ _timer.cpython-312.pyc
   │        │  │  │  │  ├─ _win32_console.cpython-312.pyc
   │        │  │  │  │  ├─ _windows.cpython-312.pyc
   │        │  │  │  │  ├─ _windows_renderer.cpython-312.pyc
   │        │  │  │  │  ├─ _wrap.cpython-312.pyc
   │        │  │  │  │  ├─ abc.cpython-312.pyc
   │        │  │  │  │  ├─ align.cpython-312.pyc
   │        │  │  │  │  ├─ ansi.cpython-312.pyc
   │        │  │  │  │  ├─ bar.cpython-312.pyc
   │        │  │  │  │  ├─ box.cpython-312.pyc
   │        │  │  │  │  ├─ cells.cpython-312.pyc
   │        │  │  │  │  ├─ color.cpython-312.pyc
   │        │  │  │  │  ├─ color_triplet.cpython-312.pyc
   │        │  │  │  │  ├─ columns.cpython-312.pyc
   │        │  │  │  │  ├─ console.cpython-312.pyc
   │        │  │  │  │  ├─ constrain.cpython-312.pyc
   │        │  │  │  │  ├─ containers.cpython-312.pyc
   │        │  │  │  │  ├─ control.cpython-312.pyc
   │        │  │  │  │  ├─ default_styles.cpython-312.pyc
   │        │  │  │  │  ├─ diagnose.cpython-312.pyc
   │        │  │  │  │  ├─ emoji.cpython-312.pyc
   │        │  │  │  │  ├─ errors.cpython-312.pyc
   │        │  │  │  │  ├─ file_proxy.cpython-312.pyc
   │        │  │  │  │  ├─ filesize.cpython-312.pyc
   │        │  │  │  │  ├─ highlighter.cpython-312.pyc
   │        │  │  │  │  ├─ json.cpython-312.pyc
   │        │  │  │  │  ├─ jupyter.cpython-312.pyc
   │        │  │  │  │  ├─ layout.cpython-312.pyc
   │        │  │  │  │  ├─ live.cpython-312.pyc
   │        │  │  │  │  ├─ live_render.cpython-312.pyc
   │        │  │  │  │  ├─ logging.cpython-312.pyc
   │        │  │  │  │  ├─ markup.cpython-312.pyc
   │        │  │  │  │  ├─ measure.cpython-312.pyc
   │        │  │  │  │  ├─ padding.cpython-312.pyc
   │        │  │  │  │  ├─ pager.cpython-312.pyc
   │        │  │  │  │  ├─ palette.cpython-312.pyc
   │        │  │  │  │  ├─ panel.cpython-312.pyc
   │        │  │  │  │  ├─ pretty.cpython-312.pyc
   │        │  │  │  │  ├─ progress.cpython-312.pyc
   │        │  │  │  │  ├─ progress_bar.cpython-312.pyc
   │        │  │  │  │  ├─ prompt.cpython-312.pyc
   │        │  │  │  │  ├─ protocol.cpython-312.pyc
   │        │  │  │  │  ├─ region.cpython-312.pyc
   │        │  │  │  │  ├─ repr.cpython-312.pyc
   │        │  │  │  │  ├─ rule.cpython-312.pyc
   │        │  │  │  │  ├─ scope.cpython-312.pyc
   │        │  │  │  │  ├─ screen.cpython-312.pyc
   │        │  │  │  │  ├─ segment.cpython-312.pyc
   │        │  │  │  │  ├─ spinner.cpython-312.pyc
   │        │  │  │  │  ├─ status.cpython-312.pyc
   │        │  │  │  │  ├─ style.cpython-312.pyc
   │        │  │  │  │  ├─ styled.cpython-312.pyc
   │        │  │  │  │  ├─ syntax.cpython-312.pyc
   │        │  │  │  │  ├─ table.cpython-312.pyc
   │        │  │  │  │  ├─ terminal_theme.cpython-312.pyc
   │        │  │  │  │  ├─ text.cpython-312.pyc
   │        │  │  │  │  ├─ theme.cpython-312.pyc
   │        │  │  │  │  ├─ themes.cpython-312.pyc
   │        │  │  │  │  ├─ traceback.cpython-312.pyc
   │        │  │  │  │  └─ tree.cpython-312.pyc
   │        │  │  │  ├─ _cell_widths.py
   │        │  │  │  ├─ _cell_widths.py:Zone.Identifier
   │        │  │  │  ├─ _emoji_codes.py
   │        │  │  │  ├─ _emoji_codes.py:Zone.Identifier
   │        │  │  │  ├─ _emoji_replace.py
   │        │  │  │  ├─ _emoji_replace.py:Zone.Identifier
   │        │  │  │  ├─ _export_format.py
   │        │  │  │  ├─ _export_format.py:Zone.Identifier
   │        │  │  │  ├─ _extension.py
   │        │  │  │  ├─ _extension.py:Zone.Identifier
   │        │  │  │  ├─ _fileno.py
   │        │  │  │  ├─ _fileno.py:Zone.Identifier
   │        │  │  │  ├─ _inspect.py
   │        │  │  │  ├─ _inspect.py:Zone.Identifier
   │        │  │  │  ├─ _log_render.py
   │        │  │  │  ├─ _log_render.py:Zone.Identifier
   │        │  │  │  ├─ _loop.py
   │        │  │  │  ├─ _loop.py:Zone.Identifier
   │        │  │  │  ├─ _null_file.py
   │        │  │  │  ├─ _null_file.py:Zone.Identifier
   │        │  │  │  ├─ _palettes.py
   │        │  │  │  ├─ _palettes.py:Zone.Identifier
   │        │  │  │  ├─ _pick.py
   │        │  │  │  ├─ _pick.py:Zone.Identifier
   │        │  │  │  ├─ _ratio.py
   │        │  │  │  ├─ _ratio.py:Zone.Identifier
   │        │  │  │  ├─ _spinners.py
   │        │  │  │  ├─ _spinners.py:Zone.Identifier
   │        │  │  │  ├─ _stack.py
   │        │  │  │  ├─ _stack.py:Zone.Identifier
   │        │  │  │  ├─ _timer.py
   │        │  │  │  ├─ _timer.py:Zone.Identifier
   │        │  │  │  ├─ _win32_console.py
   │        │  │  │  ├─ _win32_console.py:Zone.Identifier
   │        │  │  │  ├─ _windows.py
   │        │  │  │  ├─ _windows.py:Zone.Identifier
   │        │  │  │  ├─ _windows_renderer.py
   │        │  │  │  ├─ _windows_renderer.py:Zone.Identifier
   │        │  │  │  ├─ _wrap.py
   │        │  │  │  ├─ _wrap.py:Zone.Identifier
   │        │  │  │  ├─ abc.py
   │        │  │  │  ├─ abc.py:Zone.Identifier
   │        │  │  │  ├─ align.py
   │        │  │  │  ├─ align.py:Zone.Identifier
   │        │  │  │  ├─ ansi.py
   │        │  │  │  ├─ ansi.py:Zone.Identifier
   │        │  │  │  ├─ bar.py
   │        │  │  │  ├─ bar.py:Zone.Identifier
   │        │  │  │  ├─ box.py
   │        │  │  │  ├─ box.py:Zone.Identifier
   │        │  │  │  ├─ cells.py
   │        │  │  │  ├─ cells.py:Zone.Identifier
   │        │  │  │  ├─ color.py
   │        │  │  │  ├─ color.py:Zone.Identifier
   │        │  │  │  ├─ color_triplet.py
   │        │  │  │  ├─ color_triplet.py:Zone.Identifier
   │        │  │  │  ├─ columns.py
   │        │  │  │  ├─ columns.py:Zone.Identifier
   │        │  │  │  ├─ console.py
   │        │  │  │  ├─ console.py:Zone.Identifier
   │        │  │  │  ├─ constrain.py
   │        │  │  │  ├─ constrain.py:Zone.Identifier
   │        │  │  │  ├─ containers.py
   │        │  │  │  ├─ containers.py:Zone.Identifier
   │        │  │  │  ├─ control.py
   │        │  │  │  ├─ control.py:Zone.Identifier
   │        │  │  │  ├─ default_styles.py
   │        │  │  │  ├─ default_styles.py:Zone.Identifier
   │        │  │  │  ├─ diagnose.py
   │        │  │  │  ├─ diagnose.py:Zone.Identifier
   │        │  │  │  ├─ emoji.py
   │        │  │  │  ├─ emoji.py:Zone.Identifier
   │        │  │  │  ├─ errors.py
   │        │  │  │  ├─ errors.py:Zone.Identifier
   │        │  │  │  ├─ file_proxy.py
   │        │  │  │  ├─ file_proxy.py:Zone.Identifier
   │        │  │  │  ├─ filesize.py
   │        │  │  │  ├─ filesize.py:Zone.Identifier
   │        │  │  │  ├─ highlighter.py
   │        │  │  │  ├─ highlighter.py:Zone.Identifier
   │        │  │  │  ├─ json.py
   │        │  │  │  ├─ json.py:Zone.Identifier
   │        │  │  │  ├─ jupyter.py
   │        │  │  │  ├─ jupyter.py:Zone.Identifier
   │        │  │  │  ├─ layout.py
   │        │  │  │  ├─ layout.py:Zone.Identifier
   │        │  │  │  ├─ live.py
   │        │  │  │  ├─ live.py:Zone.Identifier
   │        │  │  │  ├─ live_render.py
   │        │  │  │  ├─ live_render.py:Zone.Identifier
   │        │  │  │  ├─ logging.py
   │        │  │  │  ├─ logging.py:Zone.Identifier
   │        │  │  │  ├─ markup.py
   │        │  │  │  ├─ markup.py:Zone.Identifier
   │        │  │  │  ├─ measure.py
   │        │  │  │  ├─ measure.py:Zone.Identifier
   │        │  │  │  ├─ padding.py
   │        │  │  │  ├─ padding.py:Zone.Identifier
   │        │  │  │  ├─ pager.py
   │        │  │  │  ├─ pager.py:Zone.Identifier
   │        │  │  │  ├─ palette.py
   │        │  │  │  ├─ palette.py:Zone.Identifier
   │        │  │  │  ├─ panel.py
   │        │  │  │  ├─ panel.py:Zone.Identifier
   │        │  │  │  ├─ pretty.py
   │        │  │  │  ├─ pretty.py:Zone.Identifier
   │        │  │  │  ├─ progress.py
   │        │  │  │  ├─ progress.py:Zone.Identifier
   │        │  │  │  ├─ progress_bar.py
   │        │  │  │  ├─ progress_bar.py:Zone.Identifier
   │        │  │  │  ├─ prompt.py
   │        │  │  │  ├─ prompt.py:Zone.Identifier
   │        │  │  │  ├─ protocol.py
   │        │  │  │  ├─ protocol.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  ├─ py.typed:Zone.Identifier
   │        │  │  │  ├─ region.py
   │        │  │  │  ├─ region.py:Zone.Identifier
   │        │  │  │  ├─ repr.py
   │        │  │  │  ├─ repr.py:Zone.Identifier
   │        │  │  │  ├─ rule.py
   │        │  │  │  ├─ rule.py:Zone.Identifier
   │        │  │  │  ├─ scope.py
   │        │  │  │  ├─ scope.py:Zone.Identifier
   │        │  │  │  ├─ screen.py
   │        │  │  │  ├─ screen.py:Zone.Identifier
   │        │  │  │  ├─ segment.py
   │        │  │  │  ├─ segment.py:Zone.Identifier
   │        │  │  │  ├─ spinner.py
   │        │  │  │  ├─ spinner.py:Zone.Identifier
   │        │  │  │  ├─ status.py
   │        │  │  │  ├─ status.py:Zone.Identifier
   │        │  │  │  ├─ style.py
   │        │  │  │  ├─ style.py:Zone.Identifier
   │        │  │  │  ├─ styled.py
   │        │  │  │  ├─ styled.py:Zone.Identifier
   │        │  │  │  ├─ syntax.py
   │        │  │  │  ├─ syntax.py:Zone.Identifier
   │        │  │  │  ├─ table.py
   │        │  │  │  ├─ table.py:Zone.Identifier
   │        │  │  │  ├─ terminal_theme.py
   │        │  │  │  ├─ terminal_theme.py:Zone.Identifier
   │        │  │  │  ├─ text.py
   │        │  │  │  ├─ text.py:Zone.Identifier
   │        │  │  │  ├─ theme.py
   │        │  │  │  ├─ theme.py:Zone.Identifier
   │        │  │  │  ├─ themes.py
   │        │  │  │  ├─ themes.py:Zone.Identifier
   │        │  │  │  ├─ traceback.py
   │        │  │  │  ├─ traceback.py:Zone.Identifier
   │        │  │  │  ├─ tree.py
   │        │  │  │  └─ tree.py:Zone.Identifier
   │        │  │  ├─ tomli
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ _parser.cpython-312.pyc
   │        │  │  │  │  ├─ _re.cpython-312.pyc
   │        │  │  │  │  └─ _types.cpython-312.pyc
   │        │  │  │  ├─ _parser.py
   │        │  │  │  ├─ _parser.py:Zone.Identifier
   │        │  │  │  ├─ _re.py
   │        │  │  │  ├─ _re.py:Zone.Identifier
   │        │  │  │  ├─ _types.py
   │        │  │  │  ├─ _types.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  └─ py.typed:Zone.Identifier
   │        │  │  ├─ truststore
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ _api.cpython-312.pyc
   │        │  │  │  │  ├─ _macos.cpython-312.pyc
   │        │  │  │  │  ├─ _openssl.cpython-312.pyc
   │        │  │  │  │  ├─ _ssl_constants.cpython-312.pyc
   │        │  │  │  │  └─ _windows.cpython-312.pyc
   │        │  │  │  ├─ _api.py
   │        │  │  │  ├─ _api.py:Zone.Identifier
   │        │  │  │  ├─ _macos.py
   │        │  │  │  ├─ _macos.py:Zone.Identifier
   │        │  │  │  ├─ _openssl.py
   │        │  │  │  ├─ _openssl.py:Zone.Identifier
   │        │  │  │  ├─ _ssl_constants.py
   │        │  │  │  ├─ _ssl_constants.py:Zone.Identifier
   │        │  │  │  ├─ _windows.py
   │        │  │  │  ├─ _windows.py:Zone.Identifier
   │        │  │  │  ├─ py.typed
   │        │  │  │  └─ py.typed:Zone.Identifier
   │        │  │  ├─ typing_extensions.py
   │        │  │  ├─ typing_extensions.py:Zone.Identifier
   │        │  │  ├─ urllib3
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ _collections.cpython-312.pyc
   │        │  │  │  │  ├─ _version.cpython-312.pyc
   │        │  │  │  │  ├─ connection.cpython-312.pyc
   │        │  │  │  │  ├─ connectionpool.cpython-312.pyc
   │        │  │  │  │  ├─ exceptions.cpython-312.pyc
   │        │  │  │  │  ├─ fields.cpython-312.pyc
   │        │  │  │  │  ├─ filepost.cpython-312.pyc
   │        │  │  │  │  ├─ poolmanager.cpython-312.pyc
   │        │  │  │  │  ├─ request.cpython-312.pyc
   │        │  │  │  │  └─ response.cpython-312.pyc
   │        │  │  │  ├─ _collections.py
   │        │  │  │  ├─ _collections.py:Zone.Identifier
   │        │  │  │  ├─ _version.py
   │        │  │  │  ├─ _version.py:Zone.Identifier
   │        │  │  │  ├─ connection.py
   │        │  │  │  ├─ connection.py:Zone.Identifier
   │        │  │  │  ├─ connectionpool.py
   │        │  │  │  ├─ connectionpool.py:Zone.Identifier
   │        │  │  │  ├─ contrib
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  ├─ _appengine_environ.cpython-312.pyc
   │        │  │  │  │  │  ├─ appengine.cpython-312.pyc
   │        │  │  │  │  │  ├─ ntlmpool.cpython-312.pyc
   │        │  │  │  │  │  ├─ pyopenssl.cpython-312.pyc
   │        │  │  │  │  │  ├─ securetransport.cpython-312.pyc
   │        │  │  │  │  │  └─ socks.cpython-312.pyc
   │        │  │  │  │  ├─ _appengine_environ.py
   │        │  │  │  │  ├─ _appengine_environ.py:Zone.Identifier
   │        │  │  │  │  ├─ _securetransport
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  │  ├─ bindings.cpython-312.pyc
   │        │  │  │  │  │  │  └─ low_level.cpython-312.pyc
   │        │  │  │  │  │  ├─ bindings.py
   │        │  │  │  │  │  ├─ bindings.py:Zone.Identifier
   │        │  │  │  │  │  ├─ low_level.py
   │        │  │  │  │  │  └─ low_level.py:Zone.Identifier
   │        │  │  │  │  ├─ appengine.py
   │        │  │  │  │  ├─ appengine.py:Zone.Identifier
   │        │  │  │  │  ├─ ntlmpool.py
   │        │  │  │  │  ├─ ntlmpool.py:Zone.Identifier
   │        │  │  │  │  ├─ pyopenssl.py
   │        │  │  │  │  ├─ pyopenssl.py:Zone.Identifier
   │        │  │  │  │  ├─ securetransport.py
   │        │  │  │  │  ├─ securetransport.py:Zone.Identifier
   │        │  │  │  │  ├─ socks.py
   │        │  │  │  │  └─ socks.py:Zone.Identifier
   │        │  │  │  ├─ exceptions.py
   │        │  │  │  ├─ exceptions.py:Zone.Identifier
   │        │  │  │  ├─ fields.py
   │        │  │  │  ├─ fields.py:Zone.Identifier
   │        │  │  │  ├─ filepost.py
   │        │  │  │  ├─ filepost.py:Zone.Identifier
   │        │  │  │  ├─ packages
   │        │  │  │  │  ├─ __init__.py
   │        │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  └─ six.cpython-312.pyc
   │        │  │  │  │  ├─ backports
   │        │  │  │  │  │  ├─ __init__.py
   │        │  │  │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  │  │  ├─ __pycache__
   │        │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  │  │  ├─ makefile.cpython-312.pyc
   │        │  │  │  │  │  │  └─ weakref_finalize.cpython-312.pyc
   │        │  │  │  │  │  ├─ makefile.py
   │        │  │  │  │  │  ├─ makefile.py:Zone.Identifier
   │        │  │  │  │  │  ├─ weakref_finalize.py
   │        │  │  │  │  │  └─ weakref_finalize.py:Zone.Identifier
   │        │  │  │  │  ├─ six.py
   │        │  │  │  │  └─ six.py:Zone.Identifier
   │        │  │  │  ├─ poolmanager.py
   │        │  │  │  ├─ poolmanager.py:Zone.Identifier
   │        │  │  │  ├─ request.py
   │        │  │  │  ├─ request.py:Zone.Identifier
   │        │  │  │  ├─ response.py
   │        │  │  │  ├─ response.py:Zone.Identifier
   │        │  │  │  └─ util
   │        │  │  │     ├─ __init__.py
   │        │  │  │     ├─ __init__.py:Zone.Identifier
   │        │  │  │     ├─ __pycache__
   │        │  │  │     │  ├─ __init__.cpython-312.pyc
   │        │  │  │     │  ├─ connection.cpython-312.pyc
   │        │  │  │     │  ├─ proxy.cpython-312.pyc
   │        │  │  │     │  ├─ queue.cpython-312.pyc
   │        │  │  │     │  ├─ request.cpython-312.pyc
   │        │  │  │     │  ├─ response.cpython-312.pyc
   │        │  │  │     │  ├─ retry.cpython-312.pyc
   │        │  │  │     │  ├─ ssl_.cpython-312.pyc
   │        │  │  │     │  ├─ ssl_match_hostname.cpython-312.pyc
   │        │  │  │     │  ├─ ssltransport.cpython-312.pyc
   │        │  │  │     │  ├─ timeout.cpython-312.pyc
   │        │  │  │     │  ├─ url.cpython-312.pyc
   │        │  │  │     │  └─ wait.cpython-312.pyc
   │        │  │  │     ├─ connection.py
   │        │  │  │     ├─ connection.py:Zone.Identifier
   │        │  │  │     ├─ proxy.py
   │        │  │  │     ├─ proxy.py:Zone.Identifier
   │        │  │  │     ├─ queue.py
   │        │  │  │     ├─ queue.py:Zone.Identifier
   │        │  │  │     ├─ request.py
   │        │  │  │     ├─ request.py:Zone.Identifier
   │        │  │  │     ├─ response.py
   │        │  │  │     ├─ response.py:Zone.Identifier
   │        │  │  │     ├─ retry.py
   │        │  │  │     ├─ retry.py:Zone.Identifier
   │        │  │  │     ├─ ssl_.py
   │        │  │  │     ├─ ssl_.py:Zone.Identifier
   │        │  │  │     ├─ ssl_match_hostname.py
   │        │  │  │     ├─ ssl_match_hostname.py:Zone.Identifier
   │        │  │  │     ├─ ssltransport.py
   │        │  │  │     ├─ ssltransport.py:Zone.Identifier
   │        │  │  │     ├─ timeout.py
   │        │  │  │     ├─ timeout.py:Zone.Identifier
   │        │  │  │     ├─ url.py
   │        │  │  │     ├─ url.py:Zone.Identifier
   │        │  │  │     ├─ wait.py
   │        │  │  │     └─ wait.py:Zone.Identifier
   │        │  │  ├─ vendor.txt
   │        │  │  └─ vendor.txt:Zone.Identifier
   │        │  ├─ py.typed
   │        │  └─ py.typed:Zone.Identifier
   │        ├─ pip-25.0.1.dist-info
   │        │  ├─ AUTHORS.txt
   │        │  ├─ AUTHORS.txt:Zone.Identifier
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE.txt
   │        │  ├─ LICENSE.txt:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ REQUESTED
   │        │  ├─ REQUESTED:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ entry_points.txt
   │        │  ├─ entry_points.txt:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ pycodestyle-2.6.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE
   │        │  ├─ LICENSE:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ REQUESTED
   │        │  ├─ REQUESTED:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ entry_points.txt
   │        │  ├─ entry_points.txt:Zone.Identifier
   │        │  ├─ namespace_packages.txt
   │        │  ├─ namespace_packages.txt:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ pycodestyle.py
   │        ├─ requests
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ __version__.cpython-312.pyc
   │        │  │  ├─ _internal_utils.cpython-312.pyc
   │        │  │  ├─ adapters.cpython-312.pyc
   │        │  │  ├─ api.cpython-312.pyc
   │        │  │  ├─ auth.cpython-312.pyc
   │        │  │  ├─ certs.cpython-312.pyc
   │        │  │  ├─ compat.cpython-312.pyc
   │        │  │  ├─ cookies.cpython-312.pyc
   │        │  │  ├─ exceptions.cpython-312.pyc
   │        │  │  ├─ help.cpython-312.pyc
   │        │  │  ├─ hooks.cpython-312.pyc
   │        │  │  ├─ models.cpython-312.pyc
   │        │  │  ├─ packages.cpython-312.pyc
   │        │  │  ├─ sessions.cpython-312.pyc
   │        │  │  ├─ status_codes.cpython-312.pyc
   │        │  │  ├─ structures.cpython-312.pyc
   │        │  │  └─ utils.cpython-312.pyc
   │        │  ├─ __version__.py
   │        │  ├─ __version__.py:Zone.Identifier
   │        │  ├─ _internal_utils.py
   │        │  ├─ _internal_utils.py:Zone.Identifier
   │        │  ├─ adapters.py
   │        │  ├─ adapters.py:Zone.Identifier
   │        │  ├─ api.py
   │        │  ├─ api.py:Zone.Identifier
   │        │  ├─ auth.py
   │        │  ├─ auth.py:Zone.Identifier
   │        │  ├─ certs.py
   │        │  ├─ certs.py:Zone.Identifier
   │        │  ├─ compat.py
   │        │  ├─ compat.py:Zone.Identifier
   │        │  ├─ cookies.py
   │        │  ├─ cookies.py:Zone.Identifier
   │        │  ├─ exceptions.py
   │        │  ├─ exceptions.py:Zone.Identifier
   │        │  ├─ help.py
   │        │  ├─ help.py:Zone.Identifier
   │        │  ├─ hooks.py
   │        │  ├─ hooks.py:Zone.Identifier
   │        │  ├─ models.py
   │        │  ├─ models.py:Zone.Identifier
   │        │  ├─ packages.py
   │        │  ├─ packages.py:Zone.Identifier
   │        │  ├─ sessions.py
   │        │  ├─ sessions.py:Zone.Identifier
   │        │  ├─ status_codes.py
   │        │  ├─ status_codes.py:Zone.Identifier
   │        │  ├─ structures.py
   │        │  ├─ structures.py:Zone.Identifier
   │        │  ├─ utils.py
   │        │  └─ utils.py:Zone.Identifier
   │        ├─ requests-2.18.4.dist-info
   │        │  ├─ DESCRIPTION.rst
   │        │  ├─ DESCRIPTION.rst:Zone.Identifier
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ REQUESTED
   │        │  ├─ REQUESTED:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ metadata.json
   │        │  ├─ metadata.json:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ six-1.17.0.dist-info
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ LICENSE
   │        │  ├─ LICENSE:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        ├─ six.py
   │        ├─ urllib3
   │        │  ├─ __init__.py
   │        │  ├─ __init__.py:Zone.Identifier
   │        │  ├─ __pycache__
   │        │  │  ├─ __init__.cpython-312.pyc
   │        │  │  ├─ _collections.cpython-312.pyc
   │        │  │  ├─ connection.cpython-312.pyc
   │        │  │  ├─ connectionpool.cpython-312.pyc
   │        │  │  ├─ exceptions.cpython-312.pyc
   │        │  │  ├─ fields.cpython-312.pyc
   │        │  │  ├─ filepost.cpython-312.pyc
   │        │  │  ├─ poolmanager.cpython-312.pyc
   │        │  │  ├─ request.cpython-312.pyc
   │        │  │  └─ response.cpython-312.pyc
   │        │  ├─ _collections.py
   │        │  ├─ _collections.py:Zone.Identifier
   │        │  ├─ connection.py
   │        │  ├─ connection.py:Zone.Identifier
   │        │  ├─ connectionpool.py
   │        │  ├─ connectionpool.py:Zone.Identifier
   │        │  ├─ contrib
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  ├─ appengine.cpython-312.pyc
   │        │  │  │  ├─ ntlmpool.cpython-312.pyc
   │        │  │  │  ├─ pyopenssl.cpython-312.pyc
   │        │  │  │  ├─ securetransport.cpython-312.pyc
   │        │  │  │  └─ socks.cpython-312.pyc
   │        │  │  ├─ _securetransport
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  ├─ bindings.cpython-312.pyc
   │        │  │  │  │  └─ low_level.cpython-312.pyc
   │        │  │  │  ├─ bindings.py
   │        │  │  │  ├─ bindings.py:Zone.Identifier
   │        │  │  │  ├─ low_level.py
   │        │  │  │  └─ low_level.py:Zone.Identifier
   │        │  │  ├─ appengine.py
   │        │  │  ├─ appengine.py:Zone.Identifier
   │        │  │  ├─ ntlmpool.py
   │        │  │  ├─ ntlmpool.py:Zone.Identifier
   │        │  │  ├─ pyopenssl.py
   │        │  │  ├─ pyopenssl.py:Zone.Identifier
   │        │  │  ├─ securetransport.py
   │        │  │  ├─ securetransport.py:Zone.Identifier
   │        │  │  ├─ socks.py
   │        │  │  └─ socks.py:Zone.Identifier
   │        │  ├─ exceptions.py
   │        │  ├─ exceptions.py:Zone.Identifier
   │        │  ├─ fields.py
   │        │  ├─ fields.py:Zone.Identifier
   │        │  ├─ filepost.py
   │        │  ├─ filepost.py:Zone.Identifier
   │        │  ├─ packages
   │        │  │  ├─ __init__.py
   │        │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  ├─ __pycache__
   │        │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  ├─ ordered_dict.cpython-312.pyc
   │        │  │  │  └─ six.cpython-312.pyc
   │        │  │  ├─ backports
   │        │  │  │  ├─ __init__.py
   │        │  │  │  ├─ __init__.py:Zone.Identifier
   │        │  │  │  ├─ __pycache__
   │        │  │  │  │  ├─ __init__.cpython-312.pyc
   │        │  │  │  │  └─ makefile.cpython-312.pyc
   │        │  │  │  ├─ makefile.py
   │        │  │  │  └─ makefile.py:Zone.Identifier
   │        │  │  ├─ ordered_dict.py
   │        │  │  ├─ ordered_dict.py:Zone.Identifier
   │        │  │  ├─ six.py
   │        │  │  ├─ six.py:Zone.Identifier
   │        │  │  └─ ssl_match_hostname
   │        │  │     ├─ __init__.py
   │        │  │     ├─ __init__.py:Zone.Identifier
   │        │  │     ├─ __pycache__
   │        │  │     │  ├─ __init__.cpython-312.pyc
   │        │  │     │  └─ _implementation.cpython-312.pyc
   │        │  │     ├─ _implementation.py
   │        │  │     └─ _implementation.py:Zone.Identifier
   │        │  ├─ poolmanager.py
   │        │  ├─ poolmanager.py:Zone.Identifier
   │        │  ├─ request.py
   │        │  ├─ request.py:Zone.Identifier
   │        │  ├─ response.py
   │        │  ├─ response.py:Zone.Identifier
   │        │  └─ util
   │        │     ├─ __init__.py
   │        │     ├─ __init__.py:Zone.Identifier
   │        │     ├─ __pycache__
   │        │     │  ├─ __init__.cpython-312.pyc
   │        │     │  ├─ connection.cpython-312.pyc
   │        │     │  ├─ request.cpython-312.pyc
   │        │     │  ├─ response.cpython-312.pyc
   │        │     │  ├─ retry.cpython-312.pyc
   │        │     │  ├─ selectors.cpython-312.pyc
   │        │     │  ├─ ssl_.cpython-312.pyc
   │        │     │  ├─ timeout.cpython-312.pyc
   │        │     │  ├─ url.cpython-312.pyc
   │        │     │  └─ wait.cpython-312.pyc
   │        │     ├─ connection.py
   │        │     ├─ connection.py:Zone.Identifier
   │        │     ├─ request.py
   │        │     ├─ request.py:Zone.Identifier
   │        │     ├─ response.py
   │        │     ├─ response.py:Zone.Identifier
   │        │     ├─ retry.py
   │        │     ├─ retry.py:Zone.Identifier
   │        │     ├─ selectors.py
   │        │     ├─ selectors.py:Zone.Identifier
   │        │     ├─ ssl_.py
   │        │     ├─ ssl_.py:Zone.Identifier
   │        │     ├─ timeout.py
   │        │     ├─ timeout.py:Zone.Identifier
   │        │     ├─ url.py
   │        │     ├─ url.py:Zone.Identifier
   │        │     ├─ wait.py
   │        │     └─ wait.py:Zone.Identifier
   │        ├─ urllib3-1.22.dist-info
   │        │  ├─ DESCRIPTION.rst
   │        │  ├─ DESCRIPTION.rst:Zone.Identifier
   │        │  ├─ INSTALLER
   │        │  ├─ INSTALLER:Zone.Identifier
   │        │  ├─ METADATA
   │        │  ├─ METADATA:Zone.Identifier
   │        │  ├─ RECORD
   │        │  ├─ RECORD:Zone.Identifier
   │        │  ├─ WHEEL
   │        │  ├─ WHEEL:Zone.Identifier
   │        │  ├─ metadata.json
   │        │  ├─ metadata.json:Zone.Identifier
   │        │  ├─ top_level.txt
   │        │  └─ top_level.txt:Zone.Identifier
   │        └─ werkzeug
   │           ├─ __init__.py
   │           ├─ __init__.py:Zone.Identifier
   │           ├─ __pycache__
   │           │  ├─ __init__.cpython-312.pyc
   │           │  ├─ _internal.cpython-312.pyc
   │           │  ├─ _reloader.cpython-312.pyc
   │           │  ├─ datastructures.cpython-312.pyc
   │           │  ├─ exceptions.cpython-312.pyc
   │           │  ├─ filesystem.cpython-312.pyc
   │           │  ├─ formparser.cpython-312.pyc
   │           │  ├─ http.cpython-312.pyc
   │           │  ├─ local.cpython-312.pyc
   │           │  ├─ routing.cpython-312.pyc
   │           │  ├─ security.cpython-312.pyc
   │           │  ├─ serving.cpython-312.pyc
   │           │  ├─ test.cpython-312.pyc
   │           │  ├─ testapp.cpython-312.pyc
   │           │  ├─ urls.cpython-312.pyc
   │           │  ├─ user_agent.cpython-312.pyc
   │           │  ├─ useragents.cpython-312.pyc
   │           │  ├─ utils.cpython-312.pyc
   │           │  └─ wsgi.cpython-312.pyc
   │           ├─ _internal.py
   │           ├─ _internal.py:Zone.Identifier
   │           ├─ _reloader.py
   │           ├─ _reloader.py:Zone.Identifier
   │           ├─ datastructures.py
   │           ├─ datastructures.py:Zone.Identifier
   │           ├─ datastructures.pyi
   │           ├─ datastructures.pyi:Zone.Identifier
   │           ├─ debug
   │           │  ├─ __init__.py
   │           │  ├─ __init__.py:Zone.Identifier
   │           │  ├─ __pycache__
   │           │  │  ├─ __init__.cpython-312.pyc
   │           │  │  ├─ console.cpython-312.pyc
   │           │  │  ├─ repr.cpython-312.pyc
   │           │  │  └─ tbtools.cpython-312.pyc
   │           │  ├─ console.py
   │           │  ├─ console.py:Zone.Identifier
   │           │  ├─ repr.py
   │           │  ├─ repr.py:Zone.Identifier
   │           │  ├─ shared
   │           │  │  ├─ FONT_LICENSE
   │           │  │  ├─ FONT_LICENSE:Zone.Identifier
   │           │  │  ├─ ICON_LICENSE.md
   │           │  │  ├─ ICON_LICENSE.md:Zone.Identifier
   │           │  │  ├─ console.png
   │           │  │  ├─ console.png:Zone.Identifier
   │           │  │  ├─ debugger.js
   │           │  │  ├─ debugger.js:Zone.Identifier
   │           │  │  ├─ less.png
   │           │  │  ├─ less.png:Zone.Identifier
   │           │  │  ├─ more.png
   │           │  │  ├─ more.png:Zone.Identifier
   │           │  │  ├─ source.png
   │           │  │  ├─ source.png:Zone.Identifier
   │           │  │  ├─ style.css
   │           │  │  ├─ style.css:Zone.Identifier
   │           │  │  ├─ ubuntu.ttf
   │           │  │  └─ ubuntu.ttf:Zone.Identifier
   │           │  ├─ tbtools.py
   │           │  └─ tbtools.py:Zone.Identifier
   │           ├─ exceptions.py
   │           ├─ exceptions.py:Zone.Identifier
   │           ├─ filesystem.py
   │           ├─ filesystem.py:Zone.Identifier
   │           ├─ formparser.py
   │           ├─ formparser.py:Zone.Identifier
   │           ├─ http.py
   │           ├─ http.py:Zone.Identifier
   │           ├─ local.py
   │           ├─ local.py:Zone.Identifier
   │           ├─ middleware
   │           │  ├─ __init__.py
   │           │  ├─ __init__.py:Zone.Identifier
   │           │  ├─ __pycache__
   │           │  │  ├─ __init__.cpython-312.pyc
   │           │  │  ├─ dispatcher.cpython-312.pyc
   │           │  │  ├─ http_proxy.cpython-312.pyc
   │           │  │  ├─ lint.cpython-312.pyc
   │           │  │  ├─ profiler.cpython-312.pyc
   │           │  │  ├─ proxy_fix.cpython-312.pyc
   │           │  │  └─ shared_data.cpython-312.pyc
   │           │  ├─ dispatcher.py
   │           │  ├─ dispatcher.py:Zone.Identifier
   │           │  ├─ http_proxy.py
   │           │  ├─ http_proxy.py:Zone.Identifier
   │           │  ├─ lint.py
   │           │  ├─ lint.py:Zone.Identifier
   │           │  ├─ profiler.py
   │           │  ├─ profiler.py:Zone.Identifier
   │           │  ├─ proxy_fix.py
   │           │  ├─ proxy_fix.py:Zone.Identifier
   │           │  ├─ shared_data.py
   │           │  └─ shared_data.py:Zone.Identifier
   │           ├─ py.typed
   │           ├─ py.typed:Zone.Identifier
   │           ├─ routing.py
   │           ├─ routing.py:Zone.Identifier
   │           ├─ sansio
   │           │  ├─ __init__.py
   │           │  ├─ __init__.py:Zone.Identifier
   │           │  ├─ __pycache__
   │           │  │  ├─ __init__.cpython-312.pyc
   │           │  │  ├─ multipart.cpython-312.pyc
   │           │  │  ├─ request.cpython-312.pyc
   │           │  │  ├─ response.cpython-312.pyc
   │           │  │  └─ utils.cpython-312.pyc
   │           │  ├─ multipart.py
   │           │  ├─ multipart.py:Zone.Identifier
   │           │  ├─ request.py
   │           │  ├─ request.py:Zone.Identifier
   │           │  ├─ response.py
   │           │  ├─ response.py:Zone.Identifier
   │           │  ├─ utils.py
   │           │  └─ utils.py:Zone.Identifier
   │           ├─ security.py
   │           ├─ security.py:Zone.Identifier
   │           ├─ serving.py
   │           ├─ serving.py:Zone.Identifier
   │           ├─ test.py
   │           ├─ test.py:Zone.Identifier
   │           ├─ testapp.py
   │           ├─ testapp.py:Zone.Identifier
   │           ├─ urls.py
   │           ├─ urls.py:Zone.Identifier
   │           ├─ user_agent.py
   │           ├─ user_agent.py:Zone.Identifier
   │           ├─ useragents.py
   │           ├─ useragents.py:Zone.Identifier
   │           ├─ utils.py
   │           ├─ utils.py:Zone.Identifier
   │           ├─ wrappers
   │           │  ├─ __init__.py
   │           │  ├─ __init__.py:Zone.Identifier
   │           │  ├─ __pycache__
   │           │  │  ├─ __init__.cpython-312.pyc
   │           │  │  ├─ accept.cpython-312.pyc
   │           │  │  ├─ auth.cpython-312.pyc
   │           │  │  ├─ base_request.cpython-312.pyc
   │           │  │  ├─ base_response.cpython-312.pyc
   │           │  │  ├─ common_descriptors.cpython-312.pyc
   │           │  │  ├─ cors.cpython-312.pyc
   │           │  │  ├─ etag.cpython-312.pyc
   │           │  │  ├─ json.cpython-312.pyc
   │           │  │  ├─ request.cpython-312.pyc
   │           │  │  ├─ response.cpython-312.pyc
   │           │  │  └─ user_agent.cpython-312.pyc
   │           │  ├─ accept.py
   │           │  ├─ accept.py:Zone.Identifier
   │           │  ├─ auth.py
   │           │  ├─ auth.py:Zone.Identifier
   │           │  ├─ base_request.py
   │           │  ├─ base_request.py:Zone.Identifier
   │           │  ├─ base_response.py
   │           │  ├─ base_response.py:Zone.Identifier
   │           │  ├─ common_descriptors.py
   │           │  ├─ common_descriptors.py:Zone.Identifier
   │           │  ├─ cors.py
   │           │  ├─ cors.py:Zone.Identifier
   │           │  ├─ etag.py
   │           │  ├─ etag.py:Zone.Identifier
   │           │  ├─ json.py
   │           │  ├─ json.py:Zone.Identifier
   │           │  ├─ request.py
   │           │  ├─ request.py:Zone.Identifier
   │           │  ├─ response.py
   │           │  ├─ response.py:Zone.Identifier
   │           │  ├─ user_agent.py
   │           │  └─ user_agent.py:Zone.Identifier
   │           ├─ wsgi.py
   │           └─ wsgi.py:Zone.Identifier
   ├─ lib64
   └─ pyvenv.cfg

```