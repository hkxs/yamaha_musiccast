# Yamaha MusicCast API
Let's try to control my CRX-N470 using the API for MusicCast: 

https://forum.smartapfel.de/attachment/4358-yamaha-musiccast-http-simplified-api-for-controlsystems-pdf/

## Usage
The module is just a wrapper around the API using requests, in order to use it 
just import *YamahaDevice* and create an instance using the IP address of the
device (as a string)

```
>>> from yamaha_device import YamahaDevice
>>> 
>>> device = YamahaDevice(ip_address_str)
```

If the module is able to connect to the device it will be able to control it and
get information about it:
``` 
>>> Get the model of the device
>>> device.model
'CRX-N470'
>>> 
>>> # Stop the music
>>> device.music_stop()
{'response_code': 0}
>>> 
>>> # Start the music
>>> device.music_play()
{'response_code': 0}
>>> 
>>> # Get information about the song that is being played
>>> song_info = device.get_song_info()
>>> song_info.get('track')
'We Share the Same Skies'
>>> song_info.get('album')
'Ignore The Ignorant'
```
