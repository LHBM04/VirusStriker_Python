from pico2d import *

g_sprite_bank = { str : Image } # 스프라이트 뱅크.

def AddSprite(_filePath: str):
    try:
        if _filePath in g_sprite_bank.keys():
            return
    
        g_sprite_bank[_filePath] = load_image(str)
    except FileNotFoundError:
        print(f"[Oops!] 파일을 찾지 못했습니다. 검색한 경로는 \"{_filePath}\"였습니다.")
    except Exception as exception:
        print(f"[Oops!] 파일을 불러오는 중 오류가 발생했습니다. :{exception}")

def GetSprite(_filePath: str):
    if _filePath not in g_sprite_bank.keys():
        AddSprite(_filePath)

    return g_sprite_bank[_filePath]