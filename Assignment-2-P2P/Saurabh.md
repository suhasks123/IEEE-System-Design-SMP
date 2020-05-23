Essay on Bittorrent

BitTorrent is a communication protocol for peer to peer file sharing(P2P) which is used to distribute or share data and electronic files over the internet in a decentralized manner. 
P2P network is a simple network of computers, here each computer act as node or peer for sharing file within the formed network. Unlike client-server model where client always 
initiates the communication by sending a request and server can only send response, here each node act as both client and server while sharing the file. Bittorrent is based on 
both P2P architecture and client-server architecture i.e. Hybrid P2P network. This architecture consists of tracker. Bittorrent tracker is server software that centrally coordinates 
the transfer of files among users, the tracker does not contain copy of the file and only helps peers discover each other. The clients inform the tracker regarding the file they want 
to download, their IP and port and the tracker respond with a list of peers downloading the same file or already downloaded and their contact information. This list of peers that share 
the same torrent represents a swarm. these sharing is done with the help of Metainfo file also called as torrent file having extension ‘.torrent’. This file mainly contains encoded 
information regarding the url of the tracker, name of the file and hashes of the pieces of the file for verifying downloaded pieces of the file. The peers who have already downloaded 
the file i.e. original downloader is known as seeder. Seeder keeps on uploading the file until a complete copy has been distributed among downloaders. Whereas the peers without the 
complete copy of the file, who are downloading are known as leechers. They get the list of peers from the tracker which have the remaining pieces that they require and downloads them 
and at the same time it share or uploads the pieces which are completely downloaded. Once the whole file is downloaded they are called as seeders, as they know shares the complete file. 
The pieces which downloaded is validated from the hashes present in the meta info file or torrent file. Sharing of these files within the  network without any fail, is done using the piece 
selection algorithm which tries to ensure availability by replicating the pieces as quickly as possible. This is how Bittorrent works and its advantages are Distributing large files, 
software patches and updates even popular files which have high traffic and also high traffic leads to more efficient file sharing as peers will increase. But it has its disadvantages as 
It can be used for pirated/illegal contents, you cannot update file to newer versions once distributed, also IP of all peers and info of files they are downloading are publicly available on trackers.

