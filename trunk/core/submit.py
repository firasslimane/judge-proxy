import urllib,urllib2,sys,string

def UVA_GetFirstLine(url):
    f=urllib.urlopen(url)
    lines=f.readlines()
    f.close()
    
    i=0 
    for  i in range(len(lines)):
        lines[i]=lines[i].strip('\t\n ')
    aline=string.join(lines,'')
    start=aline.find('<tr')
    start=aline.find('<tr',start+1)
    end=aline.find('<tr',start+1)
    print aline[start:end]

def UVA_Submit(problem,userid,language,code):
    url  = "http://acmicpc-live-archive.uva.es/nuevoportal/mailer.php"
    sturl = "http://acmicpc-live-archive.uva.es/nuevoportal/status.php"
    UVA_GetFirstLine(sturl)
    data = urllib.urlencode([('problem',problem),('userid',userid),('language',language),('code',code)])
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req,data)
    return 0

