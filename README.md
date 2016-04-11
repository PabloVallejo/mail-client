## Mail client

This is a simple Mail client excercise from the programming assignments of chapter two of [Computer Networking](http://www.amazon.com/Computer-Networking-Top-Down-Approach-Edition/dp/0132856204) book.

### Setup

Get a [Gmail app password](https://security.google.com/settings/security/apppasswords), and base64 encode it, also base64 encode yout email. In python it would be:

```python
import base64

# Encode email.
base64.b64encode('me@gmail.com')
>>> bWVAZ21haWwuY29t

# Encode App password.
base64.64encode('myapppassword')
>>> bXlhcHBwYXNzd29yZA==
```

Then clone the repository and use those username and password to replace the following lines:

```bash
# Clone the repo.
$ git clone https://github.com/PabloVallejo/mail-client.git
```

```python

# Line 43.
client_socket.send('AUTH LOGIN base64-email\r\n')

# Line 46.
client_socket.send('base64-app-password\r\n')
```

### Running the script.

```bash
# Cd in to repo.
$ cd mail-client

# Run the client.
$ python client.py
```

**Sample output**
```bash
python client.py
220 smtp.gmail.com ESMTP 4fmh8jtyhg5d.37 - gsmtp
250-smtp.gmail.com at your service, [181.54.230.252]
250-SIZE 35882577
250-8BITMIME
250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH
250-ENHANCEDSTATUSCODES
250-PIPELINING
250-CHUNKING
250 SMTPUTF8
334 UGFzc3dvcmQ6
235 2.7.0 Accepted
250 2.1.0 OK 4fmh8jtyhg5d.37 - gsmtp
250 2.1.5 OK 4fmh8jtyhg5d.37 - gsmtp
354  Go ahead 4fmh8jtyhg5d.37 - gsmtp
250 2.0.0 OK 1460351311 4fmh8jtyhg5d.37 - gsmtp
```

### References

* [StackOverflow](http://stackoverflow.com/questions/8974283/gmail-auth-login-smtp-authentication)
* [Lee Jef](https://leejef.wordpress.com/2013/11/02/net-cent-assignment-3-mail-client/)


