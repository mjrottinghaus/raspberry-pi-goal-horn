# NHL Goal Horn - Raspberry Pi

## Setup

Create the virtual enviorment via the following commands:

```bash
mkdir opt
python3 -m venv ./opt
```

```bash
source opt/env/bin/activate
```

### Dependencies

To run this code base, it is expected that you will be in a linux enviorment. Future development may lead to the addition of windows, but this is being built to be hosed on a Raspberry Pi running a linux distribution.

All python dependencies exist inside the requirements.txt file

You will need to have the mpg123 audio player for linux installed:

```bash
sudo apt install mpg123
```

Once you have created the virtual enviorment and activated it, you can download the requirements.

```bash 
pip install -r requirements.txt
```
