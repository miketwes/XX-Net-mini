![g](https://user-images.githubusercontent.com/6849681/111906137-19543100-8a8a-11eb-9220-89bcca785dc2.gif)


XX-Net-mini 4.5.2 Mini version of [XX-Net](https://github.com/XX-net/XX-Net), Linux (Ubuntu, Debian)和Win10 x64下正常运行.


使用说明:

   Win10_x64用户运行: start.bat, 运行演示观看: mini.mp4
 
   Linux用户终端运行:
   
    sudo aptitude install python3.9 openssl libnss3-tools
    python3 XX-Net-mini/code/default/launcher/start.py
        

运行时如果提示 

    Press Enter to continue..., 
说明有错误出现, 可修改 XX-Net-mini/code/default/lib/noarch/xlog.py中的

    self.min_level = FATAL
为

    self.min_level = NOTSET
以显示详细错误信息, 欢迎提交错误报告, 提交报告时请尽可能附上详细错误信息

如果不出现 

    Network is ok, you can start to surf the internet!
的提示, 说明Ipv6网络有问题或宽带/DHCP未连接, Ipv6网络问题可参考: [network IPv6 fail 怎么设置](https://github.com/miketwes/XX-Net-mini/issues/16)

Linux chromium浏览器代理设置: 

    chromium --proxy-server="http://127.0.0.1:8087" 
   
使用自己的appid, 编辑XX-Net-mini/data/config.json:  
    
        "gaeappids": [
            "yourappid1",
            "yourappid2"
        ],
