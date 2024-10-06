#  Copyright 2024 Hkxs
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the “Software”), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import configparser
import time

from musicast_skill.device import YamahaDevice


if __name__ == "__main__":
    env = configparser.ConfigParser()
    env.read(".env")
    device_info = env["DEVICE_INFO"]
    device = YamahaDevice(device_info["IP"])
    print(f"System Info: {device.model}")
    print("Pausing...")
    device.music_stop()
    time.sleep(3)
    print("Resume...")
    device.music_play()
    time.sleep(2)
    print("Next song")
    device.next_song()
    song_info = device.get_song_info()
    print(f"Track: {song_info.get('track')}")
    print(f"Album: {song_info.get('album')}")
    time.sleep(3)
    print("Never mind, getting back")
    device.previous_song()
    time.sleep(1)
    song_info = device.get_song_info()
    print(f"Track: {song_info.get('track')}")
    print(f"Album: {song_info.get('album')}")
