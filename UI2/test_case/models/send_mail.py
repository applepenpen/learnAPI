#封装邮件自动发送方法

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
import time
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email import encoders
from email.mime.base import MIMEBase
from UI2.test_case.models.readConfig import ReadConfig
from UI2.data import globalparam
#格式化邮件地址
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#根据报告路径获取报告文件名
def get_report_name(report_path):
    return os.path.split(report_path)[-1]

def send_mail(report_path):
    localReadConfig = ReadConfig()
    print(localReadConfig.get_mail('mail_host'))
    host=localReadConfig.get_mail('mail_host')
    user = localReadConfig.get_mail("mail_user")
    password = localReadConfig.get_mail("mail_pass")
    sender = _format_addr(localReadConfig.get_mail("sender"))
    title = localReadConfig.get_mail("subject")
    content=localReadConfig.get_mail("content")
    # receiver = _format_addr(localReadConfig.get_mail("receiver"))
    # receiver=_format_addr('793188762@qq.com')
    receiver=localReadConfig.get_mail('receiver')
    # 获取收件人列表
    receivers=[]
    if ',' in str(receiver):
        for n in str(receiver).split(','):
            receivers.append(n)
    else:
        receivers.append(receiver)
    date=str(time.strftime("%Y-%m-%d %H:%M:%S"))
    title=date+'_'+title

    # 构造邮件
    with open(report_path,'rb') as f:
        datas=f.read()
        # html_file = MIMEBase('html', 'html', file_name=get_report_name(report_path))
        html_file = MIMEBase('zip', 'zip', file_name=get_report_name(report_path))
        html_file.add_header('Content-Disposition', 'attachment', filename=get_report_name(report_path))
        html_file.set_payload(datas)
        encoders.encode_base64(html_file)
    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=receiver
    msg['Subject']=Header(title,'utf-8')
    msg.attach(MIMEText(content,'plain','utf-8'))
    msg.attach(html_file)

    #发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(host)
        smtp.login(user, password)
        smtp.sendmail(sender, receivers, msg.as_string())
        # log.info('mail send successful....')
        smtp.quit()
        # self.logger.info("The test report has send to developer by email.")
    except Exception as e:
        print(e)
        # log.info(e)


if __name__=='__main__':
    send_mail('/Users/fumengjiao/work/python3_10/UI2/report/testReport/2022-07-18 16_32_26report.html')
