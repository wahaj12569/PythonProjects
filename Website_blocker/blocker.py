import datetime
import time

end_time =datetime.datetime(2024,8,30)
site_block =['www.wscubetech.com','www.facebook.com']
host_path ='/private/etc/hosts'
redir ='127.0.0.1'


while True:
    if datetime.datetime.now()<end_time:
        print('Start Blocking')
        with open(host_path,'r+') as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redir+' '+website+'\n')
                else:
                    pass
    else:
        with open(host_path,'r+') as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for webite in site_block):
                    host_file.write(lines)
        time.sleep(5)