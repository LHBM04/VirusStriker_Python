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

from pydub import AudioSegment
import simpleaudio as SimpleAudio

# BGM 재생
DEFAULT_BGM_VOLUME:float  = 0.5                 # 기본 BGM 재생 볼륨
g_bgmVolume:float         = DEFAULT_BGM_VOLUME  # 현재 BGM 재생 볼륨

g_primarySource: SimpleAudio.WaveObject     = None  # 메인 BGM 재생 모듈
g_secondarySource: SimpleAudio.WaveObject   = None  # 서브 BGM 재생 모듈
g_jingleSource: SimpleAudio.WaveObject      = None  # 징글 BGM 재생 모듈

# 메인 BGM을 재생합니다.
def PlayPrimaryBGM(_primaryBGM: AudioSegment) -> None:
    """BGM을 재생합니다."""
    global g_primarySource
    audio = _primaryBGM - (1 - g_bgmVolume) * 100  # 볼륨 조정
    g_primarySource = audio
    # SimpleAudio를 사용하여 재생하는 코드 추가
    SimpleAudio.play_buffer(
            audio_data = audio.raw_data, 
            num_channels = audio.channels, 
            bytes_per_sample = audio.sample_width, 
            sample_rate = audio.frame_rate
        )