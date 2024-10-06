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

import requests

from musicast_skill.utils import validate_ip
from musicast_skill.utils import get_response


class YamahaDevice:
    """Simple Yamaha Device that can be controlled"""
    def __init__(self, ip_addr: str):
        self.ip = validate_ip(ip_addr)
        self.url = f"http://{self.ip}/YamahaExtendedControl/v1"
        self._info = self.get_device_info()
        if not self._info:
            raise requests.exceptions.ConnectionError(f"Unable to connect to {self.url}")
        self.model = self._info["model_name"]

    @property
    def system_api(self):
        """Endpoint to get system information"""
        return f"{self.url}/system"

    @property
    def control_api(self):
        """Endpoint to control the system"""
        return f"{self.url}/main"

    @property
    def tune_api(self):
        """Endpoint to control the radio"""
        return f"{self.url}/tuner"

    @property
    def net_usb_api(self):
        return f"{self.url}/netusb"

    @get_response
    def get_device_info(self):
        """Get Device info"""
        return requests.get(f"{self.system_api}/getDeviceInfo")

    @get_response
    def get_features(self):
        """Get Available Device Features"""
        return requests.get(f"{self.system_api}/getFeatures")

    @get_response
    def get_network_status(self):
        """Get Network Status"""
        return requests.get(f"{self.system_api}/getNetworkStatus")

    @get_response
    def get_func_status(self):
        """Get Function Status (e.g.: Auto Power Standby)"""
        return requests.get(f"{self.system_api}/getFuncStatus")

    @get_response
    def get_location_info(self):
        """Get Location info and zone list (device)"""
        return requests.get(f"{self.system_api}/getLocationInfo")

    @get_response
    def get_status(self):
        """Get zone info (device|zone)"""
        return requests.get(f"{self.system_api}/getStatus")

    @get_response
    def get_sound_program_list(self):
        """Get Sound Program List (device|zone)"""
        return requests.get(f"{self.system_api}/getSoundProgramList")

    @get_response
    def set_auto_power_stanby(self, enable: bool):
        """Enable/Disable Auto Power Standby"""
        return requests.get(f"{self.control_api}/setAutoPowerStan", params={"enable": enable})

    @get_response
    def power_on(self):
        """Power on"""
        return requests.get(f"{self.control_api}/setPower", params={"power": "on"})

    @get_response
    def standby(self):
        """Standby"""
        return requests.get(f"{self.control_api}/setPower", params={"power": "standby"})

    @get_response
    def power_toggle(self):
        """Power Toggle"""
        return requests.get(f"{self.control_api}/setPower", params={"power": "toggle"})

    @get_response
    def set_input(self, input: str):
        """Set an input source"""
        return requests.get(f"{self.control_api}/setInput", params={"power": input})

    def set_spotify(self):
        """Set Spotify as input source"""
        return self.set_input("spotify")

    def set_napster(self):
        """Set Napster as input source"""
        return self.set_input("napster")

    def set_net_raio(self):
        """Set Net Radio as input source"""
        return self.set_input("net_radio")

    def set_bluetooth(self):
        """Set Bluetooth as input source"""
        return self.set_input("bluetooth")

    @get_response
    def control_volume(self, action: str):
        return requests.get(f"{self.control_api}/setVolume", params={"volume": action})

    def increase_volume(self):
        """Increment volume"""
        return self.control_volume("up")

    def decrease_volume(self):
        """Decrease volume"""
        return self.control_volume("down")

    def set_volume(self, level: int):
        """Set Specific volume"""
        return self.control_volume(str(level))

    @get_response
    def mute(self):
        """Mute device"""
        return requests.get(f"{self.control_api}/setMute", params={"enable": "true"})

    @get_response
    def unmute(self):
        """Mute device"""
        return requests.get(f"{self.control_api}/setMute", params={"enable": "false"})

    @get_response
    def playback(self, cmd: str):
        """Stop"""
        return requests.get(f"{self.net_usb_api}/setPlayback", params={"playback": cmd})

    def music_stop(self):
        """Stop"""
        return self.playback("stop")

    def music_play(self):
        """Play"""
        return self.playback("play")

    def next_song(self):
        """Play"""
        return self.playback("next")

    def previous_song(self):
        """Play"""
        return self.playback("previous")

    @get_response
    def get_song_info(self):
        return requests.get(f"{self.net_usb_api}/getPlayInfo")
