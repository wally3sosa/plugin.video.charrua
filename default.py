import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
xbmc.executebuiltin('Container.SetViewMode(500)') # "Thumbnail" view

name = 'A24'
li = xbmcgui.ListItem(name, iconImage='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRW5j4AOslQjTRtcI3AziNw9Cm0loo5DHEntckhdqjSmk1H-LV3DO9UvgED')
url = 'http://iphone-streaming.ustream.tv/uhls/17916700/streams/live/iphone/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'AmericaTV'
li = xbmcgui.ListItem(name, iconImage='http://3.bp.blogspot.com/-0r801iqHYnw/TcDykRRvTiI/AAAAAAAAACc/QM11_i0A6UQ/s1600/15882.jpg')
url = 'https://manifest.googlevideo.com/api/manifest/hls_playlist/id/IFcUP8xs27A.1/itag/94/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/cmbypass/yes/gir/yes/dg_shard/SUZjVVA4eHMyN0EuMQ.94/hls_chunk_host/r6---sn-5ouxa-h8qd.googlevideo.com/pmbypass/yes/gcr/uy/playlist_type/DVR/mm/32/mn/sn-5ouxa-h8qd/ms/lv/mv/m/pl/24/dover/3/upn/Ape4k4j4CPY/keepalive/yes/sver/3/fexp/9405348,9406010,9408206,9408710,9408988,9409069,9415365,9415485,9416023,9416126,9416347,9417707,9417842,9418153,9418199,9418250,9418392,9418448,9419446,9420021/mt/1441151465/ip/167.58.190.155/ipbits/0/expire/1441173122/sparams/ip,ipbits,expire,id,itag,source,requiressl,ratebypass,live,cmbypass,gir,dg_shard,hls_chunk_host,pmbypass,gcr,playlist_type,mm,mn,ms,mv,pl/signature/94CC9D9A915CAC4EDCBE179C301631C82FB31F2C.2E4CBAEA465BEC359EE6E4F3AF518727102E9050/key/dg_yt0/playlist/index.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'C5N'
li = xbmcgui.ListItem(name, iconImage='http://www.conexionplena.com/wp-content/uploads/2012/08/C5N-En-vivo.jpg')
url = 'rtmp://c5n.stweb.tv:1935/c5n/live_media'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'Canal 9'
li = xbmcgui.ListItem(name, iconImage='http://i.imgur.com/7d1x7.jpg')
url = 'http://dd65nd24m61wg.cloudfront.net/livec9/smil:C9.smil/chunklist_b796000.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'El Trece'
li = xbmcgui.ListItem(name, iconImage='http://2.bp.blogspot.com/__2gkr01rYEc/ShrJZSXYyCI/AAAAAAAAES8/f8_-7Eda770/s320/el_trece_logo_320.jpg')
url = 'http://live-edge01.telecentro.net.ar/live/13hd-360/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'Telefe'
li = xbmcgui.ListItem(name, iconImage='https://lh6.googleusercontent.com/-eMQHKHFPUXY/AAAAAAAAAAI/AAAAAAAAFIQ/eH04sNi5ocY/photo.jpg')
url = 'http://live-edge01.telecentro.net.ar/live/tlfhd-360/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'TN'
li = xbmcgui.ListItem(name, iconImage='http://laalameda.files.wordpress.com/2012/02/tn.jpg')
url = 'rtsp://stream.tn.com.ar/live/tnhd1'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'TV Publica'
li = xbmcgui.ListItem(name, iconImage='http://www.diarioconcordia.com/wp-content/uploads/2012/12/TV-Publica-Canal-7.jpg')
url = 'http://live-edge01.telecentro.net.ar/live/tvphd-360/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'magazine argentina'
li = xbmcgui.ListItem(name, iconImage='http://2.bp.blogspot.com/-9wBd52c_9xU/VXewak8_rGI/AAAAAAAAG3s/XQKDVQkkZT4/s1600/ver-magazine-tv-en-vivo-online.gif')
url = 'rtsp://stream.mgzn.tv/live/mgzntv/mgzntv'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'canal 26'
li = xbmcgui.ListItem(name, iconImage='http://foromedios.com/uploads/gallery/album_2/med_gallery_1163_2_120274.png')
url = 'http://live-edge01.telecentro.net.ar/live/26hd-180/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'telesur'
li = xbmcgui.ListItem(name, iconImage='http://www.telesurtv.net/arte/LogoBlanco648X351.jpg')
url = 'http://cdn2.telesur.ultrabase.net/livecf/telesurLive/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'discovery'
li = xbmcgui.ListItem(name, iconImage='http://i0.wp.com/cine3.com/wp-content/uploads/2014/10/Discovery-logo.jpg')
url = 'http://iphone-streaming.ustream.tv/uhls/17248101/streams/live/iphone/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'canal rural'
li = xbmcgui.ListItem(name, iconImage='http://i605.photobucket.com/albums/tt134/grupofmultimedios/cr-200x100-2011.png')
url = 'rtsp://streamrural.cmd.com.ar:554/liverural/crural/rural2'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'canal de las estrellas'
li = xbmcgui.ListItem(name, iconImage='http://www.skneo2.com/wp-content/uploads/2013-11/Canal-de-las-Estrellas-en-VIVO-1.jpg')
url = 'http://tvsawpdvr-lh.akamaihd.net/i/stch02wp_1@119660/index_518_av-p.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'mega'
li = xbmcgui.ListItem(name, iconImage='https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Mega2013oficial.png/200px-Mega2013oficial.png')
url = 'http://edge-11-mvstr.edge.mdstrm.com/live/smil:db6a38a0a2bffd96d01965c4d975b9fb/playlist.m3u8?'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'antena 3'
li = xbmcgui.ListItem(name, iconImage='http://www.piensologoexisto.com/wp-content/uploads/2011/02/logoa3.jpg')
url = 'http://antena3-aos1-apple-live.adaptive.level3.net/apple/antena3/channel01/antena_3_hd_1548K_1280x720_main.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)

