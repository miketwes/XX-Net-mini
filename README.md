#### XX-Net-mini 4.5.1
Mini version of [XX-Net](https://github.com/XX-net/XX-Net).

Mini版XX-Net特点

1. 使用最新版XX-Net

2. 去掉网页配置功能(web_control)

3. 去掉自动下载

4. 去掉X-tunnel

5. 去掉扫描和删除ip的功能, 直接持久使用707个固定ip, 解决ip骤降的问题(XX-Net/data/gae_proxy/good_ip.txt)

6. 使用PyPI最新的hypack, dnslib ,hyperframe等相关模块

7. 去掉pac

8. 统一配置文件: XX-Net/data/config.json

Usage: 

用pip安装相关模块
    
    pip install hyper PyOpenSSL dnslib PySocks

下载或克隆XX-Net-mini

    git clone https://github.com/miketwes/XX-Net-mini.git

Linux用户

    cd XX-Net-mini/code/default/launcher && python3 start.py
    
Windows用户

    cd XX-Net-mini\code\default\launcher && python start.py

如果提示 Press Enter to continue...
说明有错误出现, 可修改 XX-Net/code/default/lib/noarch/xlog.py 中的 self.min_level = FATAL 为 self.min_level = NOTSET,
以显示详细错误信息
 
如果不出现 Network is ok, you can start to surf the internet! 的提示,  说明有Ipv6网络有问题

Mini版XX-Net, 在Linux和Windows环境下正常运行(其他环境未作测试)

正常运行截图

Linux:

![l1](https://user-images.githubusercontent.com/6849681/91863827-1a667200-eca2-11ea-81cb-d899bed2394f.png)

Windows:

![w1](https://user-images.githubusercontent.com/6849681/91863873-26eaca80-eca2-11ea-82d1-b1c847d0a18f.png)

    
Chromium

        chromium --proxy-server="http://127.0.0.1:8087"
    
Firefox 
    
        about:config
        network.proxy.type 1     
        network.proxy.http 127.0.0.1
        network.proxy.http_port 8087
   
Using your app id
    
        put your appids in XX-Net-mini/data/config.json
    
        "gaeappids": [
            "yourappid1",
            "yourappid2"
        ],
