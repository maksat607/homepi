#!/bin/bash
curl -u maksat607 --silent "https://mail.google.com/mail/feed/atom" |
perl -ne 'print "\t" if //;
print "$2\n" if /<(title|name)>(.*)<\/\1>/;'
