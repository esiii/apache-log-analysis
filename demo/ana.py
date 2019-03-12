import csv
import time
import re



def process(ana_path,res_path1,res_path2):

    ps = open("../result/yic.txt","w")
    f = open(ana_path, 'r')
    j = 0

    log = []
    lineid = 0
    for i in f:
        j = i.split(" ")
        lineid += 1
        j.insert(0, lineid)
        del j[3], j[2]
        # j[2] = j[2]+' '+j[3]
        j[2] = time.mktime(time.strptime((j[2] + ' ' + j[3]), "[%d/%b/%Y:%H:%M:%S %z]"))
        del j[3]

        j[3] = j[3].replace('"', '')
        j[5] = j[5].replace('"', '')
        j.insert(9, ' ')
        for n in range(10, len(j)):
            j[9] = j[9] + ' ' + j[n]
        del j[10:]

        log.append(j)
    #print(log)

    res_log = []
    tn = 0
    for re_i in log:
        #print(len(re_i))
        if(len(re_i)<=9):
            res_log.append(re_i)
        else:
            re_i.insert(9, len(re_i[8]))
            s = re.compile("Mozilla.*\(Windows.*?\).*Chrome.*")
            if (len(s.findall(re_i[10])) or len(re.compile("Mozilla.*\(Windows.*\).*Firefox.*").findall(re_i[10])) or len(re.compile("Mozilla.*\(Windows.*\).*AppleWebKit.*").findall(re_i[10]))):
                browserid = 'T1'
            elif len(re.compile("Mozilla.*\(Windows.*rv:.*\).*").findall(re_i[10])) and (len(re_i[10]) <= 100):
                browserid = 'T2'
            elif (len(re.compile("Mozilla.*\(compatible.*MSIE.*").findall(re_i[10]))or len(re.compile("Mozilla.*\(compatible.*msie.*").findall(re_i[10]))) and len(re_i[10]) <= 200:
                browserid = 'T3'
            elif len(re.compile("Mozilla.*\(compatible.*Windows.*NET.*\)").findall(re_i[10])):
                browserid = 'T4'
            elif len(re.compile("Mozilla.*\(Windows.*\)AppleWebKit.*").findall(re_i[10])):
                browserid = 'T5'
            elif len(re.compile("Mozilla.*\(compatible;.*http://.*\)").findall(re_i[10])) and (len(re_i[10]) <= 150):
                browserid = 'T6'
            elif len(re.compile("Mozilla.*\(compatible;.*@.*.com.*\)").findall(re_i[10])) and (len(re_i[10]) <= 100):
                browserid = 'T7'
            elif len(re.compile("Mozilla.*\(compatible;.*Indy.*\)").findall(re_i[10])) and (len(re_i[10]) <= 80):
                browserid = 'T8'
            elif (len(re.compile("Sogou.*http://www.sogou.*").findall(re_i[10])) or len(re.compile("Youdao .*http://.*youdao.*").findall(re_i[10])) or len(re.compile("psbot.*http://.*picsearch.*").findall(re_i[10])) or len(re.compile("Baiduspider.*http://.*baidu.*").findall(re_i[10])) or len(re.compile("findlinks.*http://.*findlinks.*").findall(re_i[10])) or len(re.compile("Wotbox.*wotbox").findall(re_i[10]))) and (len(re_i[10]) <= 100):
                browserid = 'T9'
            elif (len(re.compile("Java/.*").findall(re_i[10])) or len(re.compile(".*Nutch/.*").findall(re_i[10]))) and (len(re_i[10]) <= 30):
                browserid = 'T10'
            elif len(re.compile("Jakarta.*Commons.*HttpClient.*").findall(re_i[10])) and (len(re_i[10]) <= 50):
                browserid = 'T11'
            elif len(re.compile("Mozilla.*").findall(re_i[10])) and (len(re_i[10]) <= 30):
                browserid = 'T12'
            elif len(re.compile(".*Android.*").findall(re_i[10])):
                browserid = 'T13'
            elif len(re.compile("Mozilla.*\(.*iPhone.*\).*").findall(re_i[10])) and (len(re_i[10]) <= 150):
                browserid = 'T14'
            elif len(re.compile("Mozilla.*\(.*iPad.*\).*AppleWebKit.*Mobile.*").findall(re_i[10])):
                browserid = 'T15'
            elif (len(re.compile("Mozilla.*\(.*Linux.*\).*Gecko.*").findall(re_i[10])) or len(re.compile("UCWEB.*\(.*\).*UCBrowser.*").findall(re_i[10]))):
                browserid = 'T16'
            elif len(re.compile("Mozilla.*\(.*Mac OS.*\).*Gecko.*").findall(re_i[10])):
                browserid = 'T17'
            # T18-T23为自动化机器人
            elif len(re.compile("msnbot.*\(.*http://.*msnbot.*\)").findall(re_i[10])) and len(re_i[10]) <= 100:
                browserid = 'T18'
            elif (len(re.compile("Googlebot.*").findall(re_i[10])) or len(re.compile(".*Bot.*").findall(re_i[10]))):
                browserid = 'T19'
            elif (len(re.compile("hqthCrawler.*").findall(re_i[10])) or len(
                    re.compile("hqthcrawler.*").findall(re_i[10]))) and (len(re_i[10]) <= 30):
                browserid = 'T20'
            elif (len(re.compile("YisouSpider.*").findall(re_i[10]))  or len(re.compile("nutch spider.*").findall(re_i[10])) or len(re.compile("spider.*Nutch").findall(re_i[10])) or len(re.compile(".*Baiduspider.*").findall(re_i[10])) ) and (len(re_i[10]) <= 50):
                browserid = 'T21'
            elif (len(re.compile("Sosospider.*http://.*").findall(re_i[10])) or len(re.compile("Sogou.*Spider.*").findall(re_i[10])) or len(re.compile("Sogou.*spider.*").findall(re_i[10]))  or len(re.compile("SogouFramework").findall(re_i[10]))):
                browserid = 'T22'
            elif (len(re.compile("Tianwang.*").findall(re_i[10])) or len(re.compile("TSINGHUA.*").findall(re_i[10])) )and (len(re_i[10]) <= 30):
                browserid = 'T23'
            elif (len(re.compile("Wget.*").findall(re_i[10])) or len(re.compile("curl.*").findall(re_i[10]))):
                browserid = 'T24'
            elif len(re.compile("godtroop.*").findall(re_i[10])) and (len(re_i[10]) <= 50):
                browserid = 'T25'
            elif len(re.compile("DoCoMo.*\(compatible.*http://.*\).*").findall(re_i[10])) and (len(re_i[10]) <= 150):
                browserid = 'T26'
            elif (len(re.compile("-").findall(re_i[10])) or len(re.compile("").findall(re_i[10]))) and (len(re_i[10]) <= 10):
                browserid = 'T27'
            elif len(re.compile("Yeti.*Corp.*http://.*").findall(re_i[10])):
                browserid = 'T28'
            elif len(re.compile("SAMSUNG-SGH.*Configuration.*Browser.*http.*").findall(re_i[10])):
                browserid = 'T29'
            elif len(re.compile("Python.*").findall(re_i[10])) and (len(re_i[10]) <= 30):
                browserid = 'T30'
            elif len(re.compile("Opera.*Windows.*").findall(re_i[10])) and (len(re_i[10]) <= 100):
                browserid = 'T31'
            elif len(re.compile("crawler.*http.*crawler.*").findall(re_i[10])) and (len(re_i[10]) <= 100):
                browserid = 'T32'
            elif len(re.compile("ExB.*http.*exb.*").findall(re_i[10])) and (len(re_i[10]) <= 100):
                browserid = 'T33'
            elif (len(re.compile("360.*").findall(re_i[10])) or len(re.compile("Ucweb.*").findall(re_i[10])) or len(re.compile("UCWEB.*").findall(re_i[10])) or len(re.compile("Opera.*").findall(re_i[10])) or len(re.compile("Yahoo.*").findall(re_i[10])) or len(re.compile("Internet Explorer.*").findall(re_i[10])) or len(re.compile("IE.*").findall(re_i[10]))) and (len(re_i[10]) <= 100):
                browserid = 'T34'
            elif (len(re.compile("useragent.*").findall(re_i[10])) ):
                browserid = 'T35'
            elif (len(re.compile("Microsoft.*MiniRedir.*").findall(re_i[10])) ):
                browserid = 'T36'
            else:
                browserid = 'Tn'
                tn += 1
            re_i.insert(11, browserid)
            res_log.append(re_i)
    if(tn>10):
        ps.write(ana_path + ',' + res_path2 + ',' + str(tn) + '\n')
        print(ana_path,res_path1,res_path2,tn)
    #print(tn)

    with open(res_path1, 'w') as csvfile:
        write = csv.writer(csvfile)

        write.writerow(
            ['lineID', 'IP', 'time', 'method', 'request_url', 'protocol', 'return-sta', 'byte-num', 'from_url',
             'browser'])

        write.writerows(log)
    with open(res_path2, 'w') as csvfile:
        write = csv.writer(csvfile)

        write.writerow(
            ['lineID', 'IP', 'time', 'method', 'request_url', 'protocol', 'return-sta', 'byte-num', 'from_url',
             'from_url_len', 'browser', 'browserid'])

        write.writerows(log)


    f.close()
