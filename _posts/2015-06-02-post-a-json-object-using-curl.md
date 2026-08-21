---
layout: post
class: 'post-template'
subclass: 'post'
title: "POST a JSON Object Using cURL"
date: 2015-06-02 16:50:00 +0000
slug: "post-a-json-object-using-curl"
ghost_id: 52
ghost_uuid: "9504bd0a-dbfc-40c6-b714-47959859557b"
---

<code>curl -H "Content-Type: application/json" -X POST -d '{"message":"xyz"}' http://localhost:3000/some/endpoint</code>

That JSON object will get really annoying for longer data.
