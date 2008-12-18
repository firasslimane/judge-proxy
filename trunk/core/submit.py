import urllib,urllib2,sys

def UVA_Submit(problem,userid,language,code):
    url  = "http://acmicpc-live-archive.uva.es/nuevoportal/mailer.php"
    data = urllib.urlencode([('problem',problem),('userid',userid),('language',language),('code',code)])
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req,data)
    while 1:
        dt = fd.read(1024)
        if not len(dt):
            break
    return 0

