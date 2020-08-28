import bencoding
import logging
import socket
import struct
import aiohttp
import random
from urllib.parse import urlencode


class TrackerResponse:
    def __init__(self, response: dict):
        self.response = response
    @property
    def failure(self):
        if b'failure reason' in self.response:
            return self.response[b'failure reason'].decode('utf-8')
        return None
    @property
    def interval(self) -> int:
        return self.response.get(b'interval', 0)
    @property
    def complete(self) -> int:
        return self.response.get(b'complete', 0)
    @property
    def incomplete(self) -> int:
        return self.response.get(b'incomplete', 0)
    @property
    def peers(self):
        peers = self.response[b'peers']
        if type(peers)==list:
            logging.debug('Dictionary model peers are returned by tracker')
            raise NotImplementedError()
        else:
            logging.debug('Binary model peers are returned by tracker')
            peers = [peers[i:i+6] for i in range(0, len(peers), 6)]
            return [(socket.inet_ntoa(p[:4]), struct.unpack(">H", p[4:])[0]) for p in peers]
    def __str__(self):
        return f'incomplete: {self.incomplete}\n'\
               f'complete: {self.complete}\n'\
               f'interval: {self.interval}\n'\
               f'peers: {", ".join([x for (x,_) in self.peers])}\n'\


class Tracker:
    def __init__(self, torrent):
        self.torrent = torrent
        self.peer_id = '-PC0001-'+''.join([str(random.randint(0, 9)) for _ in range(12)])
        self.http_client = aiohttp.ClientSession()

    async def connect(self, first: bool=None, uploaded: int=0, downloaded: int= 0):
        params ={}
        params['info_hash'] = self.torrent.info_hash
        params['uploaded'] = 0
        params['download'] = 0
        params['peer_id'] = self.peer_id
        params['port'] = 6969
        params['left'] = self.torrent.total_size-downloaded
        params['compact'] = 1
        url = self.torrent.announce +'?'+ urlencode(params)
        print(params)
        if first:
            params['event'] = 'started'

        async with self.http_client.get(url) as response:
            if not response.status == 200:
                raise ConnectionError(f'Unable to connect to tracker: status code {response.status}')
            data = await response.read()
            return TrackerResponse(bencoding.Decoder(data).decode())
    def close(self):
        self.http_client.close()
    def raise_for_error(self, tracker_response):
        try:
            message = tracker_response.decode("utf-8")
            if "failure" in message:
                raise ConnectionError(f'Unable to connect to tracker: {format(message)}')
        except UnicodeDecodeError:
            pass

