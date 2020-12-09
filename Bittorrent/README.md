**Overview**

BitTorrent is a communication protocol for peer-to-peer file sharing (P2P), that enables users  
to distribute data and electronic files over the Internet in a decentralized manner.  
A peer-to-peer network allows computer hardware and software to communicate without the need for  
a server. Unlike client-server architecture, there is no central server for processing requests  
in a P2P architecture. The peers directly interact with one another without the requirement of a  
central server. Users/Peers are mainly classified as seeds, leeches in torrent system.  
***Seeds***  
*Seed is the user that have the complete file downloaded already and are now sharing the file with  
peers but not downloading any parts of the file from others.*  
***Leeches***  
*Leechers are those who are downloading and uploading at the same time.*  

Any file which has to be downloaded is distributed or already downloaded by the peers all over the  
network and the list of all these peers is maintained and updated by one called Tracker. For downloading  
any files we need to download the locations of all the peers and Tracker ID in order to contact them to  
download and this information is stored in the .torrent file. which we download directly or through magnet  
links provided on sites. This torrent file is has all information about the file holders and Tracker info.

**Code Structure**  
The **cli.py** file takes .torrent file as argument and extracts the information of Tracker and peers containing  
the file to be downloaded by decoding the .torrent file using the **torrent.py** file and **bencoding.py**.  
which returns the data and sends to **client.py** which makes calls **tracker.py** to confirm the tracker  
and the peers available which involves setting up connection between the peer and tracker by using 3-way  
handshake. Once the seeders/leechers are confirmed, client.py sets connection to other peers i.e.  
seeders/leechers, which after connection setup sends the files request which send in pieces which is further  
divided in blocks and the other peer acknowledges it as is there and onces confirmed we setted up connection  
and files are started downloading in blocks which combine and make pieces which further makes the whole file.  
The maxpeer limit is set to 40 i.e. at same time it can connect to 40 peers for download. unlike simultaneous  
downloades(implemented by multithreading) asyncio execute it more as multitasking.
