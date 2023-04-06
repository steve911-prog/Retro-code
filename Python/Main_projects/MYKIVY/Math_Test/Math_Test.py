from kivy.core.audio import SoundLoader

sound = SoundLoader.load('sergey-briksa-mir-ne-prost-2014.mp3')
if sound:
    sound.play()
