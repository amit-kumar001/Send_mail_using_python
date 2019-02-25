# Send_mail_using_python  
![img png](https://user-images.githubusercontent.com/47202519/53320717-78bbd300-38fc-11e9-9f0e-4d31840e9262.jpg)
  
## Key feature
<ol>

<li>smtplib module define <strong> SMTP </strong> (simple mail transfer protocol) client session object that can send mail to any internet machine. This module is used to make communication with a mail server to send mail.</li>
<li>Provide sender mail_id in one variable and recevier mail_id in another variable.  </li>
<li>SMTP used to create connection with server.<strong> smtp.gmail.com </strong> is outgoing mail server require Port for TLS/STARTTLS: 587</li>
<li><strong> s.starttls()</strong> method is used to start <strong>TLS</strong> (Transfer layer security). </li>
<li>Now provide sender mail id with password.</li>
<li>Write a message that we want to send.</li>
<li><strong>sendmail() </strong> method is used to send mail.</li>
</ol>

### Required Permission in google account 
<ol>
To send  mail using python language,  we have to give some permission in google account.  
  
open sender google account -> select security option ->click on Less secure app access ->Allow less secure apps: ON
This permission allows us to send mail.
</ol>  



### Result in mail  

![load](https://user-images.githubusercontent.com/47202519/53320976-3ba41080-38fd-11e9-99b0-7eb82fc2c662.png)



### How to run this file

Since this is a python file, hence it can be run using following command

python mail2.py

python3 mail2.py
