from PIL import Image
from selenium import webdriver

chrome_path = "C:\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

for i in range(300):
    web.get('https://stu255.ntust.edu.tw/ntust_stu/stu.aspx')

    web.get_screenshot_as_file("temp.png")

    verify_code = web.find_element_by_id("Image2")

    left = verify_code.location['x']
    right = verify_code.location['x'] + verify_code.size['width']
    top = verify_code.location['y']
    bottom = verify_code.location['y'] + verify_code.size['height']

    img = Image.open("temp.png")
    img = img.crop((left, top, right, bottom))
    img.save("VCode.png")

    source = Image.open("VCode.png")

    alphabet1 = source.crop((66, 0, 84, 40))
    alphabet2 = source.crop((90, 0, 101, 40))
    alphabet3 = source.crop((105, 0, 120, 40))

    alphabet1.save("alphabet1_" + str(i) + ".png")
    alphabet2.save("alphabet2_" + str(i) + ".png")
    alphabet3.save("alphabet3_" + str(i) + ".png")

