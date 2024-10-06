# VirusStriker_Python
![Virus Striker](./Resources/Sprites/GUI/Sprite_Logo.png)


기존의 "Virus Striker"를 Python으로 포팅한 버전. (2D 게임 프로그래밍 텀 프로젝트)

## Requirements
### Python Version
`>= 3.12`
### Modules
* multipledispatch
* numpy
* pathlib
* pico2d
* sdl2
## TODO: Frameworks(Hierarchy) ※ 추후 변경 가능
### Core
#### Components
- **Component**
  - **Animation**
    - GameObject 
  - **Animation**
    - Animator
    - Animation
  - **Collider2D**
    - BoxCollider2D
    - CircleCollider2D
  - **Renderer**
     - SpriteRenderer
     - CanvasRenderer 
  - **Transform**
    - Transform
    - RectTransform
#### Utilities
- **AudioManagement**
  - AudioManager
  - AudioSource
    - LoopAudioSource 
  - SFX
  - BGM
  - BGMLoopData
- **InputManagement**
  - EInputState 
  - InputManager
- **Mathematics**
  - Vector2
  - Vector3
  - MathF
  - MathV
  - Rotation   
- **FileManagement**
  - FileManager
  - JsonManager 
- **Singleton** 
  - Singleton
  - LazySingleton
#### GUI
- **Canvas**
- **CanvasGroup**
- **UIObject**
  - Text
  - Image
  - Button
  - InputField
  - ect...   
#### System
- **SystemManager**
