一：高级模块 (code7)
	1. secure_link_module 安全链接模块
		a.制定并允许检查请求的链接的真实性及保护资源免收未授权访问
		b.限制链接生效周期
		c.语法：
			secure_link ;
			secure_link_md5 ;
		d.下载
			1. 客户端->下载->生成下载地址->服务端校验
	2.geoip_module 基于IP地址匹配MaxMind GeoIP 二进制文件,读取所在地域信息
		(不同地域人访问不同服务器ip)
		a.安装nginx模块 yum install nginx-module-geoip
			/etc/nginx/modules/  查看对应模块
		b. 用途
			1. 区分 国内外作HTTP访问规则
			2. 区分国内城市地域作HTTP访问规则
			3. download_geoip.sh 新建tmp文件
			4. gunzip 解压
			5.  nginx.conf 配置文件
				load_module modules/ngx_http_geoip_module.so; 
	3. HTTPS服务
		1. https协议原理,优势劣势
			a.传输数据，数据内容被劫持
			b. 对传输内容加密,身份认证
			c. 对称加密
			d. 非对称加密 (公钥私钥)
		2. 中间人伪造客户端和服务端
		3. 生成密钥和CA证书
			a. 生成key 密钥
				1. rpm -qa|grep open
				2. openssl genrsa -idea -out jesonc.key 1024
					密码：123456
			b. 生成证书签名请求文件 csr文件
				openssl req -new -key jesonc.key -out jesonc.csr
			c. 生成证书签名文件CA文件
				openssl x509 -req -days 3650 -in jesonc.csr -signkey jesonc.key -out jesonc.crt
			d. 通过key 直接生成crt证书
				openssl req -days 36500 -x509 -sha256 -nodes -newkey rsa:2048 -keyout jesonc.key -out jesonc_apple.crt
			e.  openssl rsa -in ./jesonc.key -out ./jesoncou_nopas.key
		4. https服务优化
			1. 激活keepalive 长连接
			2. 设置ssl session 缓存
	4. Nginx +LUA
		1.Nginx 并发处理epoll优势(非阻塞IO),lua轻量
			用户ip,访问次数，安全
		2. yum install lua
			chmod a+rx ./test.lua
		3. 搭建环境 (http://www.imooc.com/article/19597)
			1.LuaJIT
			2. ngx_devel_kit lua-nginx-module
			3.重新编译nginx