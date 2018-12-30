from PIL import Image
from selenium import webdriver

chrome_path = "C:\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

for i in range(10):
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

    number_width = 14

    number1 = source.crop((13, 0, number_width + 13, 40))
    number2 = source.crop((31, 0, number_width + 31, 40))
    number3 = source.crop((49, 0, number_width + 49, 40))

    number1.save("number1_" + str(i) + ".png")
    number2.save("number2_" + str(i) + ".png")
    number3.save("number3_" + str(i) + ".png")

