from selenium import webdriver
import urllib3
import urllib
import urllib.parse
import time
import multiprocessing
import api.baidu
import api.youdaoapi
service_args=[]

service_args.append('--load-images=false')  ##关闭图片加载  
service_args.append('--disk-cache=true')  ##开启缓存
#driver = webdriver.Chrome(executable_path="D:\ProGramFiles\chromedriver_win32\chromedriver.exe",service_args=service_args)
#driver = webdriver.PhantomJS(executable_path="D:\ProGramFiles\phantomjs-2.1.1-windows\phantomjs.exe",service_args=service_args)
driver = webdriver.PhantomJS(service_args=service_args)
def youdao(input):
    try:
        a = ''
        driver.get("http://fanyi.youdao.com/")
        driver.find_element_by_id('inputOriginal').send_keys(input) 
        time.sleep(1)
        answers = driver.find_elements_by_css_selector("span[data-section][data-sentence]")#transTarget > p > spandata-section
        for ans in answers :
            a += '\n'+ans.text
        #print(a)
        return a
    except:
        return 'erro'

def baidu(input):
    try:
        a = ''
        input=urllib.parse.quote(input)
        driver.get("https://fanyi.baidu.com/#zh/en/{input}".format(input=input))
        driver.refresh() 
        time.sleep(3)
        answers = driver.find_elements_by_xpath('//p[@class="ordinary-output target-output clearfix"]/span')
        for ans in answers :
            a += '\n'+ans.text
        #print(a)    
        return a
    except:
        return 'erro'

def google(input):
    try:
        a = ''
        input=urllib.parse.quote(input)
        driver.get("https://translate.google.cn/#view=home&op=translate&sl=auto&tl=en&text={input}".format(input=input))
        time.sleep(1)
        answers = driver.find_elements_by_xpath('//span[@class="tlid-translation translation"]/span')
        for ans in answers :
            a += '\n'+ans.text  
        return a
    except:
        return 'erro'
def cnki(input):
    try:
        a = '单词意思:'
        input=urllib.parse.quote(input)
        driver.get("http://dict.cnki.net/dict_result.aspx?searchword={input}".format(input=input))
        time.sleep(1)
        answers = driver.find_elements_by_xpath('//li/font/a[1]')
        for ans in answers :
            if ans.text == '':
                continue
            a += '    '+ans.text  
        a += '\n\n句子示例:'
        answers = driver.find_elements_by_xpath("//table[starts-with(@id,'show')]/tbody/tr/td")
        for ans in answers :
            if ans.text == '' or '短句来源' in ans.text :
                continue
            if  ans.text == '更多       ':
                break
            a += '\n\n'+ans.text  
        return a
    except :
        pass
def translate(input):
    try:
        ans = []
        ans.append(google(input))
        ans.append(baidu(input))                                 #抓包方式获得百度翻译结果
        ans.append(youdao(input))                                #抓包方式获得有道翻译结果
        #ans.append(api.baidu.baidu(input))                        #百度api 方式
        #ans.append(api.youdaoapi.connect(input))                  #有道api 方式
        return ans
    except Exception as e:
        print(e)
        return  [0,0,0]


