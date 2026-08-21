---
layout: post
class: 'post-template'
subclass: 'post'
title: "Forwarding Your Gmail for Business Account"
date: 2015-04-01 23:27:12 +0000
slug: "forwarding-your-gmail-for-business-account"
ghost_id: 43
ghost_uuid: "8e3695fc-0218-4457-9857-bf2ffd9eaccf"
---

#Gmail Begets Gmail
I have two gmail accounts which feed into my main gmail address. It's gmail inception.

The problem is, each of these addresses have non-standard domains. So, instead of `dork@gmail.com`, it's `dork@email.arizona.edu` and `dork@voltacharging.com`.

Google doesn't recognize these accounts immediately, so the magic pre-filling doesn't happen.

#Step-by-Step
####Go to the email address you want to forward.
<ol>
<li>Open the email settings by clicking the gear icon, then <code>Settings</code>.</li>
<li>Click <code>Forwarding and POP/IMAP</code>.</li>
<li>Enable POP for all mail. When a message is accessed for POP, archive a copy. (These are my settings)

![](/assets/images/2015/04/Screen-Shot-2015-04-01-at-4-01-19-PM.png)
</li>
<li>Save changes at the bottom of the page.</li>
</ol>
####Go to the email address you want to get mail delivered to.
<i>Set up receiving:</i>
<ol>
<li>Open the email settings by clicking the gear icon, then <code>Settings</code>.</li>
<li>Click <code>Accounts and Import</code>.</li>
<li>Click <code>Add a POP3 mail account you own</code>. A popup will occur. Enter your full gmail business address.

![](/assets/images/2015/04/Screen-Shot-2015-04-01-at-4-12-04-PM.png)
</li>
<li>Enter your entire email address as the username. Replace the POP Server with <code>pop.gmail.com</code> and a port of 995. Use SSL. Add the account.

![](/assets/images/2015/04/Screen-Shot-2015-04-01-at-4-16-53-PM.png)
</li>
</ol>

<i>Set up sending:</i>
Most of the time, the previous process will ask you if you want to send email via this account as well. 

![](/assets/images/2015/04/Screen-Shot-2015-04-01-at-4-22-12-PM.png)

<ol>
<li>Enter your name and UNCHECK alias.</li>
<li>Enter your entire email address as the username. Replace the SMTP Server with <code>smtp.gmail.com</code> and a port of 587. Use TLS. Add the account.
</ol>
