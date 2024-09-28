from pico2d import *
from pydub import AudioSegment

g_bgmBank = { str : AudioSegment }
g_sfxBank = { str : AudioSegment }

def LoadBGM(_path: str, _name: str) -> None:
    if _path in g_bgmBank.keys():
        print(f"{_name} is already loaded.")
        return

    try:
        g_bgmBank[_name] = AudioSegment.from_wav(_path)
        print(f"{_name} loaded successfully from {_path}.")
    except Exception as e:
        print(f"Error loading {_name} from {_path}: {e}")