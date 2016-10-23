import mice
import os

s1 = mice.m.getServer(1)
#script assumes you only run one Mumble vserver.

rootcert = '/etc/letsencrypt/live/your.mumbledomain.com/cert.pem'
certF = open(rootcert)
certS = certF.read()
certF.close()
#print(certS)

rootkey = '/etc/letsencrypt/live/your.mumbledomain.com/privkey.pem'
keyF = open(rootkey)
keyS = keyF.read()
keyF.close()
#print(certH)

#Leave the passhprase field empty (no space) if you don't use one.
passphrase = 'YOUR PASSPHRASE'

s1.updateCertificate(certS, keyS, passphrase)
