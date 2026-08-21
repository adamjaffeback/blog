---
layout: post
class: 'post-template'
subclass: 'post'
title: "Uploading Intermediate SSL Certificates to AWS Elastic Beanstalk Load Balancers"
date: 2015-10-23 22:46:38 +0000
slug: "uploading-comodo-ssl-certificates-to-aws"
description: "Upload intermediate and root certificates to your AWS Elastic Beanstalk Load Balancer to fix intermittent Android https failures."
meta_title: "Intermediate SSL Certificates to AWS Elastic Beanstalk Load Balancers"
ghost_id: 57
ghost_uuid: "54f2d8f1-05b7-42bc-b17d-190562220ca7"
---

I haven't written for a while. Problems like this are why.

#Problem
We recently released an Ionic hybrid app for our company to both the Google Play and iOS App Stores. Both my CTO and I could successfully download the app and install it, but when we tried to make calls to the API, the app would fail. We thought this was because we had both been beta-testers at some point and the entire app wasn't being removed from our system.

That is, until users started posting negative reviews:

![Can't login or signup](/assets/images/2015/10/Screen-Shot-2015-10-23-at-1-56-24-PM.png)

![Cant login](/assets/images/2015/10/Screen-Shot-2015-10-23-at-1-56-17-PM.png)

Ouch.

#Diagnosis
On a hunch, I checked the server endpoint the app was calling. On my computer, the SSL certificate was fine. However, when I visited it on my phone's mobile browser, the certificate was rejected.

This was the same for my CTO, but the `https://` site worked for other Android users in the office and, cooincidentally, so did their apps.

I used [this website](https://www.ssllabs.com/ssltest/) to test the validity of my SSL certificate. It came back with an "A" rating. I wasn't satisfied.
 
Using `openssl` in the terminal, I was able to retrieve and inspect the certificate from the server:
```
openssl s_client -showcerts -connect <subdomain.domain.com>:443
// example:
openssl s_client -showcerts -connect drive.google.com:443
```

443 is the secure port. If you don't have `openssl`, you'll need to install it.

I got my certificates back, and they looked good, except for an error which looked like a silent fail (look at the third line):
![](/assets/images/2015/10/Screen-Shot-2015-10-23-at-2-07-12-PM.png)

That didn't end up mattering as much as the root certificate was missing. I had "COMODO RSA Domain Validation Secure Server CA" and "COMODO RSA Certification Authority".

Don't ask what those are...I don't know. I just know I didn't have a root certificate. 

#The Fix
We load-balance our servers using Elastic Beanstalk on AWS. You'll have to find which load balancer is attached to your server and upload a new cert.

####Find Your Certs
We've already created our certs and submitted them to a certificate authority--in our case, Comodo--using these [steps](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/ssl-server-cert.html).

You should have four or five files from Comodo. Open them in a text editor, like Sublime. Mine were labeled:

- `AddTrustExternalCARoot.crt`
- `COMODORSAAddTrustCA.crt`
- `COMODORSADomainValidationSecureServerCA.crt`
- `STAR_voltaapi_com.crt`
- `EssentialSSL Wildcard Certificate.txt`

<u>You will also need the private .pem key used to sign your request to the certificate authority.</u>

`COMODORSAAddTrustCA.crt` and `COMODORSADomainValidationSecureServerCA.crt` are generic to Comodo. You can actually get them again [here](https://support.comodo.com/index.php?/Default/Knowledgebase/Article/View/620/0/which-is-root-which-is-intermediate). Ours were the EssentialSSL SHA-2. I'll also just paste the code in the "Upload Certificate" section below.

What's strange is that `EssentialSSL Wildcard Certificate.txt` and `STAR_voltaapi_com.crt` are the same certificate, just by different names. They are the root I'm looking for, which is confusing, because I have a file named `AddTrustExternalCARoot.crt` which we're not going to end up using.

####Identify the Load Balancer
1. Log in to AWS Console and navigate to your EC2 instances.
1. From the dashboard, click "Load Balancers" on the left navigation pane.
1. Select one of the load balancers and click on the "Instances" tab: 
![](/assets/images/2015/10/crop.jpg) 
4.  Look at the name. That should match the name of the environment you're trying to upload a new SSL certificate to. If it doesn't, select a different load balancer until you find it.

####Upload Your Certificate
<ol>
<li>From the load balancer you've found, click the "Listeners" tab.</li>
<li>If there isn't an https listener yet, add one. We used the predefined security policy "ELBSecurityPolicy-2015-05" for the cipher:

![Listeners](/assets/images/2015/10/Screen-Shot-2015-10-23-at-2-45-16-PM.png)

</li>
<li>Click to change or upload the new cert. Select upload as the type. You should see this dialogue:

![](/assets/images/2015/10/Screen-Shot-2015-10-23-at-2-55-22-PM.png)

</li>
<li>Name the certificate something easy to remember. Copy and paste the text from the private key you used to submit your certificate into the field labeled "Private Key". It may begin with either:
```
-----BEGIN PRIVATE KEY-----
OR
-----BEGIN RSA PRIVATE KEY-----
```

![](/assets/images/2015/10/Screen-Shot-2015-10-23-at-3-00-45-PM.png)
</li>
<li>My public key certificate was the contents of <code>STAR_voltaapi_com.crt</code>. Just a reminder-- <code>EssentialSSL Wildcard Certificate.txt</code> is the <strong>same thing</strong>.

![](/assets/images/2015/10/Screen-Shot-2015-10-23-at-3-17-38-PM.png)

</li>
<li>The "Certificate Chain" is <strong>NOT OPTIONAL</strong> and is what got us into this mess in the first place. I combined the two generic Comodo certs (order matters):<br>
<code>cat COMODORSADomainValidationSecureServerCA.crt COMODORSAAddTrustCA.crt > certchain.txt</code><br>
Here is the combined code to paste:<br>
<code>-----BEGIN CERTIFICATE-----
MIIGCDCCA/CgAwIBAgIQKy5u6tl1NmwUim7bo3yMBzANBgkqhkiG9w0BAQwFADCB
hTELMAkGA1UEBhMCR0IxGzAZBgNVBAgTEkdyZWF0ZXIgTWFuY2hlc3RlcjEQMA4G
A1UEBxMHU2FsZm9yZDEaMBgGA1UEChMRQ09NT0RPIENBIExpbWl0ZWQxKzApBgNV
BAMTIkNPTU9ETyBSU0EgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkwHhcNMTQwMjEy
MDAwMDAwWhcNMjkwMjExMjM1OTU5WjCBkDELMAkGA1UEBhMCR0IxGzAZBgNVBAgT
EkdyZWF0ZXIgTWFuY2hlc3RlcjEQMA4GA1UEBxMHU2FsZm9yZDEaMBgGA1UEChMR
Q09NT0RPIENBIExpbWl0ZWQxNjA0BgNVBAMTLUNPTU9ETyBSU0EgRG9tYWluIFZh
bGlkYXRpb24gU2VjdXJlIFNlcnZlciBDQTCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAI7CAhnhoFmk6zg1jSz9AdDTScBkxwtiBUUWOqigwAwCfx3M28Sh
bXcDow+G+eMGnD4LgYqbSRutA776S9uMIO3Vzl5ljj4Nr0zCsLdFXlIvNN5IJGS0
Qa4Al/e+Z96e0HqnU4A7fK31llVvl0cKfIWLIpeNs4TgllfQcBhglo/uLQeTnaG6
ytHNe+nEKpooIZFNb5JPJaXyejXdJtxGpdCsWTWM/06RQ1A/WZMebFEh7lgUq/51
UHg+TLAchhP6a5i84DuUHoVS3AOTJBhuyydRReZw3iVDpA3hSqXttn7IzW3uLh0n
c13cRTCAquOyQQuvvUSH2rnlG51/ruWFgqUCAwEAAaOCAWUwggFhMB8GA1UdIwQY
MBaAFLuvfgI9+qbxPISOre44mOzZMjLUMB0GA1UdDgQWBBSQr2o6lFoL2JDqElZz
30O0Oija5zAOBgNVHQ8BAf8EBAMCAYYwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNV
HSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwGwYDVR0gBBQwEjAGBgRVHSAAMAgG
BmeBDAECATBMBgNVHR8ERTBDMEGgP6A9hjtodHRwOi8vY3JsLmNvbW9kb2NhLmNv
bS9DT01PRE9SU0FDZXJ0aWZpY2F0aW9uQXV0aG9yaXR5LmNybDBxBggrBgEFBQcB
AQRlMGMwOwYIKwYBBQUHMAKGL2h0dHA6Ly9jcnQuY29tb2RvY2EuY29tL0NPTU9E
T1JTQUFkZFRydXN0Q0EuY3J0MCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5jb21v
ZG9jYS5jb20wDQYJKoZIhvcNAQEMBQADggIBAE4rdk+SHGI2ibp3wScF9BzWRJ2p
mj6q1WZmAT7qSeaiNbz69t2Vjpk1mA42GHWx3d1Qcnyu3HeIzg/3kCDKo2cuH1Z/
e+FE6kKVxF0NAVBGFfKBiVlsit2M8RKhjTpCipj4SzR7JzsItG8kO3KdY3RYPBps
P0/HEZrIqPW1N+8QRcZs2eBelSaz662jue5/DJpmNXMyYE7l3YphLG5SEXdoltMY
dVEVABt0iN3hxzgEQyjpFv3ZBdRdRydg1vs4O2xyopT4Qhrf7W8GjEXCBgCq5Ojc
2bXhc3js9iPc0d1sjhqPpepUfJa3w/5Vjo1JXvxku88+vZbrac2/4EjxYoIQ5QxG
V/Iz2tDIY+3GH5QFlkoakdH368+PUq4NCNk+qKBR6cGHdNXJ93SrLlP7u3r7l+L4
HyaPs9Kg4DdbKDsx5Q5XLVq4rXmsXiBmGqW5prU5wfWYQ//u+aen/e7KJD2AFsQX
j4rBYKEMrltDR5FL1ZoXX/nUh8HCjLfn4g8wGTeGrODcQgPmlKidrv0PJFGUzpII
0fxQ8ANAe4hZ7Q7drNJ3gjTcBpUC2JD5Leo31Rpg0Gcg19hCC0Wvgmje3WYkN5Ap
lBlGGSW4gNfL1IYoakRwJiNiqZ+Gb7+6kHDSVneFeO/qJakXzlByjAA6quPbYzSf
+AZxAeKCINT+b72x
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFdDCCBFygAwIBAgIQJ2buVutJ846r13Ci/ITeIjANBgkqhkiG9w0BAQwFADBv
MQswCQYDVQQGEwJTRTEUMBIGA1UEChMLQWRkVHJ1c3QgQUIxJjAkBgNVBAsTHUFk
ZFRydXN0IEV4dGVybmFsIFRUUCBOZXR3b3JrMSIwIAYDVQQDExlBZGRUcnVzdCBF
eHRlcm5hbCBDQSBSb290MB4XDTAwMDUzMDEwNDgzOFoXDTIwMDUzMDEwNDgzOFow
gYUxCzAJBgNVBAYTAkdCMRswGQYDVQQIExJHcmVhdGVyIE1hbmNoZXN0ZXIxEDAO
BgNVBAcTB1NhbGZvcmQxGjAYBgNVBAoTEUNPTU9ETyBDQSBMaW1pdGVkMSswKQYD
VQQDEyJDT01PRE8gUlNBIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MIICIjANBgkq
hkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAkehUktIKVrGsDSTdxc9EZ3SZKzejfSNw
AHG8U9/E+ioSj0t/EFa9n3Byt2F/yUsPF6c947AEYe7/EZfH9IY+Cvo+XPmT5jR6
2RRr55yzhaCCenavcZDX7P0N+pxs+t+wgvQUfvm+xKYvT3+Zf7X8Z0NyvQwA1onr
ayzT7Y+YHBSrfuXjbvzYqOSSJNpDa2K4Vf3qwbxstovzDo2a5JtsaZn4eEgwRdWt
4Q08RWD8MpZRJ7xnw8outmvqRsfHIKCxH2XeSAi6pE6p8oNGN4Tr6MyBSENnTnIq
m1y9TBsoilwie7SrmNnu4FGDwwlGTm0+mfqVF9p8M1dBPI1R7Qu2XK8sYxrfV8g/
vOldxJuvRZnio1oktLqpVj3Pb6r/SVi+8Kj/9Lit6Tf7urj0Czr56ENCHonYhMsT
8dm74YlguIwoVqwUHZwK53Hrzw7dPamWoUi9PPevtQ0iTMARgexWO/bTouJbt7IE
IlKVgJNp6I5MZfGRAy1wdALqi2cVKWlSArvX31BqVUa/oKMoYX9w0MOiqiwhqkfO
KJwGRXa/ghgntNWutMtQ5mv0TIZxMOmm3xaG4Nj/QN370EKIf6MzOi5cHkERgWPO
GHFrK+ymircxXDpqR+DDeVnWIBqv8mqYqnK8V0rSS527EPywTEHl7R09XiidnMy/
s1Hap0flhFMCAwEAAaOB9DCB8TAfBgNVHSMEGDAWgBStvZh6NLQm9/rEJlTvA73g
JMtUGjAdBgNVHQ4EFgQUu69+Aj36pvE8hI6t7jiY7NkyMtQwDgYDVR0PAQH/BAQD
AgGGMA8GA1UdEwEB/wQFMAMBAf8wEQYDVR0gBAowCDAGBgRVHSAAMEQGA1UdHwQ9
MDswOaA3oDWGM2h0dHA6Ly9jcmwudXNlcnRydXN0LmNvbS9BZGRUcnVzdEV4dGVy
bmFsQ0FSb290LmNybDA1BggrBgEFBQcBAQQpMCcwJQYIKwYBBQUHMAGGGWh0dHA6
Ly9vY3NwLnVzZXJ0cnVzdC5jb20wDQYJKoZIhvcNAQEMBQADggEBAGS/g/FfmoXQ
zbihKVcN6Fr30ek+8nYEbvFScLsePP9NDXRqzIGCJdPDoCpdTPW6i6FtxFQJdcfj
Jw5dhHk3QBN39bSsHNA7qxcS1u80GH4r6XnTq1dFDK8o+tDb5VCViLvfhVdpfZLY
Uspzgb8c8+a4bmYRBbMelC1/kZWSWfFMzqORcUx8Rww7Cxn2obFshj5cqsQugsv5
B5a6SE2Q8pTIqXOi6wZ7I53eovNNVZ96YUWYGGjHXkBrI/V5eu+MtWuLt29G9Hvx
PUsE2JOAWVrgQSQdso8VYFhH2+9uRv0V9dlfmrPb2LjkQLPNlzmuhbsdjrzch5vR
pu/xO28QOG8=
-----END CERTIFICATE-----
</code>
</li>
<li>Save and enjoy!</li>
</ol>

#Summary
I still don't know why my desktop web browser accepted the certificates, as did many other mobile devices, but a select-few Android mobiles failed. Three of the four documented devices with issues were Samsung Galaxy Note 4's running Android 5 (Lollipop).

Upload intermediate and root certificates to your AWS Elastic Beanstalk Load Balancer.

You're SOL if you don't have the private key you used to sign the cert in the first place. Pony up for new cert and keep that key safe!

Major thanks to this [question and answer](http://serverfault.com/questions/393822/how-do-i-install-intermediate-certificates-in-aws), which got me on the way to a solution.
