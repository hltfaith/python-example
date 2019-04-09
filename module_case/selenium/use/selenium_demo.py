
'''


一、什么是Selenium

selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,
编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。
Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，
因此可以用于任何支持JavaScript的浏览器上。

selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。

这里要说一下比较重要的PhantomJS,PhantomJS是一个而基于WebKit的服务端JavaScript API,支持Web而不需要浏览器支持，其快速、
原生支持各种Web标准：Dom处理，CSS选择器，JSON等等。PhantomJS可以用用于页面自动化、网络监测、网页截屏，以及无界面测试


'''

from selenium import webdriver

# print(help(webdriver))


# 声明浏览器对象
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()

# 访问页面
# browser.get("http://www.baidu.com")
# print(browser.page_source)
# browser.close()
# 上述代码运行后，会自动打开Chrome浏览器，并登陆百度打印百度首页的源代码，然后关闭浏览器



'''

查找元素
单个元素查找

'''

# browser = webdriver.Chrome()
#
# browser.get("http://www.taobao.com")
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
#
# print(input_first)
# print(input_second)
# print(input_third)

# browser.close()

'''
这里我们通过三种不同的方式去获取响应的元素，第一种是通过id的方式，第二个中是CSS选择器，
第三种是xpath选择器，结果都是相同的。

结果如下：
<selenium.webdriver.remote.webelement.WebElement (session="e0e15ca1280c17981945542d608f5cb2", element="0.893452788352116-1")>
<selenium.webdriver.remote.webelement.WebElement (session="e0e15ca1280c17981945542d608f5cb2", element="0.893452788352116-1")>
<selenium.webdriver.remote.webelement.WebElement (session="e0e15ca1280c17981945542d608f5cb2", element="0.893452788352116-1")>

'''


'''

这里列举一下常用的查找元素方法：

find_element_by_name
find_element_by_id
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

下面这种方式是比较通用的一种方式：这里需要记住By模块所以需要导入
from selenium.webdriver.common.by import By

当然这种方法和上述的方式是通用的，browser.find_element(By.ID,"q")这里By.ID中的ID可以替换为其他几个


'''

# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# input_first = browser.find_element(By.ID, 'q')
# print(input_first)
# browser.close()



'''

多个元素查找

其实多个元素和单个元素的区别，举个例子：find_elements,单个元素是find_element,
其他使用上没什么区别，通过其中的一个例子演示：



当然下面的方式也是可以通过导入from selenium.webdriver.common.by import By 这种方式实现

lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')

同样的在单个元素中查找的方法在多个元素查找中同样存在：
find_elements_by_name
find_elements_by_id
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector

'''

# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()



'''

元素交互操作
对于获取的元素调用交互方法

'''

# import time
#
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys('ipad')
# time.sleep(1)
#
# input_str.clear()
# input_str.send_keys('MakBook pro')
# button = browser.find_element_by_class_name('btn-search')
# button.click()


'''

交互动作
将动作附加到动作链中串行执行

'''

# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
#
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()


'''

执行JavaScript
这是一个非常有用的方法，这里就可以直接调用js方法来实现一些操作，
下面的例子是通过登录知乎然后通过js翻到页面底部，并弹框提示

'''

# browser = webdriver.Chrome()
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')




'''

获取元素属性
get_attribute('class')

'''


# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))



'''

获取文本值
text

'''

# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)


'''

获取ID，位置，标签名
id
location
tag_name
size

'''

# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)


'''

Frame
在很多网页中都是有Frame标签，所以我们爬取数据的时候就涉及到切入到frame中以及切出来的问题，通过下面的例子演示
这里常用的是switch_to.from()和switch_to.parent_frame()

'''


# import time
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)




'''

等待
当使用了隐式等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，
超出设定时间后则抛出找不到元素的异常, 换句话说，当查找元素或元素并没有立即出现的时候，
隐式等待将等待一段时间再查找 DOM，默认的时间是0

隐式等待
到了一定的时间发现元素还没有加载，则继续等待我们指定的时间，如果超过了我们指定的时间还没有加载就会抛出异常，
如果没有需要等待的时候就已经加载完毕就会立即执行


'''

# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)
#


'''

显示等待

指定一个等待条件，并且指定一个最长等待时间，会在这个时间内进行判断是否满足等待条件，如果成立就会立即返回，
如果不成立，就会一直等待，直到等待你指定的最长等待时间，如果还是不满足，就会抛出异常，如果满足了就会正常返回


'''


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)


