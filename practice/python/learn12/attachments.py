
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'aqie123aqie@163.com'
password =  input('Password: ')
to_addr = input('To:')
smtp_server = 'smtp.163.com'


# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('Python啊切 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('啦啦啦啦德玛西亚', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://60.205.217.197:8081/#/">啊切Music</a>...</p>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('aqie.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpeg', filename='aqie.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='aqie.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# 建立安全连接 加密SMPT
smtp_port = 465
server = smtplib.SMTP(smtp_server, 25)
server.starttls()

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()