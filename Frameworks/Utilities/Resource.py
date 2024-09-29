from pico2d import *
from pydub import AudioSegment

g_sprite_bank = { str : Image } # 스프라이트 뱅크.

def add_sprite(_path: str) -> None:
    global g_sprite_bank
    if _path in g_sprite_bank.keys():
        print(f"{os.path.basename(_path)} is already loaded.")
        return
    
    g_sprite_bank[_path] = load_image(_path)

g_bgm_bank = { str : AudioSegment }  # BGM 뱅크.
g_sfx_bank = { str : AudioSegment }  # SFX 뱅크.

def add_bgm(_path: str) -> None:
    global g_bgm_bank
    if _path in g_bgm_bank.keys():
        print(f"{os.path.basename(_path)} is already loaded.")
        return
    
    try:
        g_bgm_bank[_path] = AudioSegment.from_wav(_path)
    except FileNotFoundError as e:
        assert(e)
    except Exception as e:
        assert(e)

def add_sfx(_path: str) -> None:
    global g_sfx_bank
    if _path in g_sfx_bank.keys():
        print(f"{os.path.basename(_path)} is already loaded.")
        return
    
    try:
        g_bgm_bank[_path] = AudioSegment.from_wav(_path)
    except FileNotFoundError as e:
        assert(e)
    except Exception as e:
        assert(e)