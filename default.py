import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import addon="xbmc.python" version="2.1.0"
import addon="script.module.beautifulsoup" version="3.2.1"
import addon="script.module.simple.downloader" version="0.9.4"
import addon="script.module.beautifulsoup4" 
import addon="script.module.simple.downloader" version="0.9.4"
import addon="script.module.requests" 
import addon="script.module.httplib2" 
import addon="script.module.youtube.dl" optional="true"
import addon="plugin.video.youtube" 
import addon="script.module.urlresolver" optional="true"
import addon="script.module.simplejson"    
addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
xbmc.executebuiltin('Container.SetViewMode(500)') # "Thumbnail" view

name = 'A24'
li = xbmcgui.ListItem(name, iconImage='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRW5j4AOslQjTRtcI3AziNw9Cm0loo5DHEntckhdqjSmk1H-LV3DO9UvgED')
url = 'https://youtu.be/yZGc05q7ajA'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'AmericaTV'
li = xbmcgui.ListItem(name, iconImage='http://3.bp.blogspot.com/-0r801iqHYnw/TcDykRRvTiI/AAAAAAAAACc/QM11_i0A6UQ/s1600/15882.jpg')
url = 'http://prepublish.f.qaotic.net/epa/ngrp:americatvlive-100056_all/chunklist_b1596000.m3u8|Referer=http://vmf.edge-apps.net'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'C5N'
li = xbmcgui.ListItem(name, iconImage='http://www.conexionplena.com/wp-content/uploads/2012/08/C5N-En-vivo.jpg')
url = 'http://c5n.stweb.tv/c5n/live/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'Canal 9'
li = xbmcgui.ListItem(name, iconImage='http://i.imgur.com/7d1x7.jpg')
url = 'http://158.69.127.19:8000/live/lmorales/dyd/8447.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'El Trece'
li = xbmcgui.ListItem(name, iconImage='http://2.bp.blogspot.com/__2gkr01rYEc/ShrJZSXYyCI/AAAAAAAAES8/f8_-7Eda770/s320/el_trece_logo_320.jpg')
url = 'http://prepublish.f.qaotic.net/a03/ngrp:el13_live01-100083_all/playlist.m3u8|User-Agent=Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q)'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'Telefe'
li = xbmcgui.ListItem(name, iconImage='https://lh6.googleusercontent.com/-eMQHKHFPUXY/AAAAAAAAAAI/AAAAAAAAFIQ/eH04sNi5ocY/photo.jpg')
url = 'http://live-edge01.telecentro.net.ar/live/tlfhd-360/playlist.m3u8'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'TN'
li = xbmcgui.ListItem(name, iconImage='http://laalameda.files.wordpress.com/2012/02/tn.jpg')
url = 'http://prepublish.f.qaotic.net/b05/ngrp:tn_live01-100083_all/Playlist.m3u8|User-Agent=iPhone'
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

name = 'TV Publica'
li = xbmcgui.ListItem(name, iconImage='http://www.diarioconcordia.com/wp-content/uploads/2012/12/TV-Publica-Canal-7.jpg')
url = 'http://prepublish.f.qaotic.net/a02/ngrp:c7live01-20034_all/chunklist_b1396000.m3u8|Referer=http://vmf.edge-apps.net'
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

