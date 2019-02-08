from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pyvirtualdisplay import Display

    # Load display
display = Display(visible=1, size=(800, 600))
display.start()

    # Load the driver
driver = webdriver.Firefox()
driver.get('http://127.0.0.1:3000')
# driver.save_screenshot('initial_condition.png')
        

    # Load elements to order
li_elements = driver.find_elements_by_tag_name('li')

    # Perform Ordering
# Get the order of the elements    
actual_order = [(i,int(elem.text.split(' ')[1])) 
                for i,elem in enumerate(li_elements)]
for i in range(0,len(li_elements)):
    # input('Press Enter for net move')
    actionChains = ActionChains(driver)
    # Re-order the list to get the element to switch
    actual_order = sorted(actual_order, key=lambda k:k[1])
    if actual_order[i][0] != actual_order[i][1]:
        drag = li_elements[actual_order[i][0]]
        drop = li_elements[actual_order[i][1]]
        # driver.save_screenshot(str(i)+'_move.png')
        # Drag and drop
        actionChains.drag_and_drop(li_elements[actual_order[i][0]], 
                                   li_elements[actual_order[i][1]]).perform()

        # Get the new order after switching elements
        actual_order = [(x,int(elem.text.split(' ')[1])) 
                        for x,elem in enumerate(li_elements)]

# driver.save_screenshot('final_condition.png')
input('Press Enter to leave')
driver.quit()
display.stop()
