# TODO: AudioSystem 개발 과정
# 1. 메인 BGM 재생/정지 함수 만들기
#   - 일시 정지/정지된 시점 재생 구현
#   - 페이드 효과 재생/정지 구현
# 2. 서브 BGM 재생/정지 함수 작성하기
#   - 일시 정지/정지된 시점 재생 구현
#   - 페이드 효과 재생/정지 구현
# 3. 징글 BGM 재생/정지 함수 작성하기
#   - 일시 정지/정지된 시점 재생 구현
#   - 페이드 효과 재생/정지 구현
# 4. SFX 재생 로직 작성하기 
#   - 재생 위치 다르게 하기
#   - 오브젝트 풀링 이용해서 SFX 재생 소스 할당하기
from pygame import mixer as audiosource
from pygame.mixer import Sound as bgm
from pygame.mixer import Sound as sfx

audiosource.init()

_primaryBGM: str = None
_secondaryBGM: str = None
_jingleBGM: str = None

def 