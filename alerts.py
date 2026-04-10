from tiny_fx import TinyFX
tiny = TinyFX(wav_root="/alerts")
rgb = tiny.rgb
from time import sleep

red_alert = (255,0,0)
#yellow_alert = (255, 191, 0) Saved for future use
#blue_alert = (0,0,255) Saved for future use, but only with USS Voyager
off = (0,0,0)
try:
    while True:
        if tiny.boot_pressed() == True:
            tiny.wav.play_wav("red_alert.wav")
            while tiny.wav.is_playing():
                tiny.rgb.set_rgb(*red_alert)
                sleep(0.5)
                tiny.rgb.set_rgb(*off)
                sleep(0.5)
finally:
    tiny.shutdown()