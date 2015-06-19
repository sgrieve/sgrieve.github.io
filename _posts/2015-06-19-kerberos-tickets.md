---
layout: post
title: Renewing a Kerberos Ticket
---

To get a new ticket while connected via ssh to a server, type `kinit` and then
your password at the prompt.

To check your current ticket status use `klist`, and to destroy all of your tickets
prior to logging off, use `kdestroy`.
