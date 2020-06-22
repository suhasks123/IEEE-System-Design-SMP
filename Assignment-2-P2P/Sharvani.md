<h1>BitTorrent</h1>
Sometimes downloading large files from websites can be really painful and slow especially when many people try to download at the same time. The website could crash too :/

Unlike typical downloads, files using BitTorrent (similar to a peer to peer protocol) actually download faster when more people are involved and it works with any kind of file.

Usually, when someone downloads a file from a normal website it comes to their computer in a stream from a single source and when multiple people want the file that single source can get overworked and can even shut down.

<b>BitTorrent</b> solves this problem by making each downloader a source. In this way they get pieces of the file but also provide pieces to each other together the downloaders become a network of multiple sources all working to provide pieces to one another which makes downloads fast. 
To connect to other users who have the pieces of our file, BitTorrent uses a computer called a <b>tracker</b> that helps our computer find other computers called <b>peers</b>. 
The tracker keeps track of computers that are downloading or already have the whole file and introduces our computer to them with the connections in place.
Because of the presence of this central entity(tracker), BitTorrent is a <b>hybrid P2P protocol</b>.(There are 2 kinds of P2P protocol: pure P2P[any single, arbitrary chosen peer can be removed from the network without having the network suffering any loss of network service] and hybrid P2P[a central entity is necessary to provide parts of the offered network services])

Users downloading from a BitTorrent swarm are commonly referred to as <b>leechers</b> or <b>peers</b>. Users that remain connected to a BitTorrent swarm even after they’ve downloaded the complete file, contributing more of their upload bandwidth so other people can continue to download the file, are referred to as <b>seeders</b>. For a torrent to be downloadable, one seeder who has a complete copy of all the files in the torrent must initially join the swarm so other users can download the data. If a torrent has no seeders, it won’t be possible to download as no connected user has the complete file.

BitTorrent clients reward other clients who upload, preferring to send data to clients who contribute more upload bandwidth rather than sending data to clients who upload at a very slow speed. This speeds up download times for the swarm as a whole and rewards users who contribute more upload bandwidth.

There is a <b>.torrent file</b> or <b>metainfo file</b> that regulates how many pieces there are for a given file, how these should be exchanged between peers, as well as how the data integrity of these pieces can be confirmed by clients. These torrent files are generally created using client software. A list of trackers and the original file are required to create this torrent file. Once the file is created it can be shared using the regular methods such as email, file sharing websites etc.

BitTorrent uses <b>piece selection algorithm</b> to decide which piece to download with the goal of achieving maximum piece replication and ensuring piece availability.
Firstly a <b>random piece</b> is selected so that a peer can quickly select a piece and start uploading.  Nextly, <b>rarest pieces</b> are given priority and downloaded. When peers always choose the rarest available piece, all the pieces of the file will be quickly replicated and can avoid losing a piece. Also,since a file is partitioned into pieces before downloading, these pieces are again subdivided into sub-pieces. When a sub-piece is requested, the remaining sub-pieces of the same piece are requested before any other piece. With this pieces can be assembled quickly, and will be available for other peers. Instead of waiting for a single peer, a request is sent to all peers for the last few pieces. This will improve the efficiency.

Although BitTorrent is popularly used to download pirated material, it is still used in a number of different, legal, solutions where distribution of larger files is important such as:
Facebook use it to distribute updates within their huge data centers, larger files such as Linux distributions

It does have many <b>disadvantages</b> along with the cool advantages we know:
We Cannot modify/update the file to newer versions once the torrent has been distributed. There are security issues and the IP of all peers and info of files they are downloading are publicly available on trackers. Also, The tracker is a critical component and if it fails it can disrupt the distribution of all the files it has tracking.


<b>-Sharvani</b>

