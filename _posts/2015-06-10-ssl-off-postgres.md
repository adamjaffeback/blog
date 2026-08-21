---
layout: post
class: 'post-template'
subclass: 'post'
title: "So Your Server Doesn't Support SSL Connections"
date: 2015-06-10 18:18:42 +0000
slug: "ssl-off-postgres"
ghost_id: 49
ghost_uuid: "939c474c-7e2c-41b1-8caf-053adf177ea8"
---

##Problem
Oh, this was a frustrating one! After working with my database for about a month, this error randomly surfaced. Ugly. There's a lot of [low-level documentation](http://www.postgresql.org/docs/9.3/static/libpq-ssl.html) which could help...if I could read it.

{<1>}![Aint nobody got time for that](http://gifrific.com/wp-content/uploads/2012/08/Aint-Nobody-Got-Time-for-That.gif)

According to PostgreSQL:
>PostgreSQL has native support for using SSL connections to encrypt client/server communications for increased security. [...] the PostgreSQL server can be started with SSL enabled by setting the parameter ssl to on in `postgresql.conf`.

More on that file [here](http://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html).

##Fix


To find the file, open PostgreSQL in the terminal. To find the config file, enter `SHOW config_file`.

{<2>}![Path to file](/assets/images/2015/05/Screen-Shot-2015-05-28-at-11-27-32-AM.png)

Go get it. FYI, some of the files in the path are hidden.

Change `ssl = 'on'`. 
{<3>}![](/assets/images/2015/06/Screen-Shot-2015-06-02-at-9-52-47-AM.png)
Save. Restart PostgreSQL.

##That Didn't Work?
Restart your computer. Seriously. I've had this problem twice. I went back to the `postgres.conf` files to find the ssl settings the same way I left them. I tried `ssl = true`, which didn't have any effect. Only restarting the computer worked.

####More Reads
http://www.postgresql.org/docs/9.3/static/ssl-tcp.html
