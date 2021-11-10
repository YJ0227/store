import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

mail_host = "smtp.qq.com"  # 设置服务器

sender = '1574858294@qq.com'
mail_pass = "csmcuyujsydtfehe"  # 口令
receivers = '1574858294@qq.com'

# 设置邮件内容
msg = MIMEMultipart()
msg['From'] = Header(sender)      # 发件人信息
msg['To'] = Header(receivers)     # 收件人信息
subject = 'ICBC测试报告'   # 邮件标题
msg['Subject'] = subject
# 发送的文本内容，plain表示纯文本
message = MIMEText('ICBC的测试结果，详细报告请见附件！', 'plain', 'utf-8')
msg.attach(message)
# 构造附件，传送当前目录下的文件：计算器测试报告.html
att = MIMEText(open('测试结果.xlsx', 'rb').read(), 'base', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att.add_header('Content-Disposition', 'attachment', filename="测试结果.xlsx")
msg.attach(att)

# 连接服务器
service = smtplib.SMTP_SSL(mail_host)
service.connect(mail_host, 465)
# 登录SMTP服务器
service.login(sender, mail_pass)
# 发送邮件，邮件正文是一个str,所有使用as_string()把MIMEText对象变成str
service.sendmail(sender, receivers, msg.as_string())
print("发送成功！")
# 退出登录
service.quit()
