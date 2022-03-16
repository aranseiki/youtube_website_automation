from time import sleep
from selenium.webdriver import Firefox, Chrome, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


browser = ''


def start_browser(url, browsername):
    """
    Definition
    ----------
    Starts the Firefox browser and open it with an URL.
    Require to inform URL parameter.
    ----------

    Parameters
    ----------
        url : str
            Link URL of a valid webpage
    ----------

    Output
    ----------
    None

    """
    global browser
    if browsername.upper().__contains__('CHROME'):
        browser = Chrome()
    elif browsername.upper().__contains__('EDGE'):
        browser = Edge()
    elif browsername.upper().__contains__('FIREFOX'):
        browser = Firefox()
    else:
        print (f' {browsername} not avaliable. Chose one these following options: Chrome, Edge, Firefox.')
        print ('By default, it works on Edge. ')
        browser = Firefox()
    browser.maximize_window()
    open_link(url)


def open_link(url):
    browser.get(url)
    wait_page_loaded()


def open_window():
    """
    Definition
    ----------
    Stops the Firefox browser controlled by automation.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    browser.execute_script('window.open()')


def get_window_id():
    """
    Definition
    ----------
    Stops the Firefox browser controlled by automation.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    
    window_id = browser.current_window_handle
    return window_id


def get_all_window_ids():
    """
    Definition
    ----------
    Stops the Firefox browser controlled by automation.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    
    window_id = browser.window_handles
    return window_id


def wait_page_loaded():
    """
    Definition
    ----------
    Waits the current webpage in context be totally fulled.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    done_state = False
    while done_state == False:
        state = browser.execute_script(
            'return window.document.readyState'
        )
        if state != 'complete':
            sleep(1)
        else:
            done_state = True


def back_page():
    """
    Definition
    ----------
    Back the navigation for earlierly webpage accessed.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    browser.back()
    wait_page_loaded()


def center_element(selector, type_element='CSS_SELECTOR'):
    """
    Definition
    ----------
    centralizes a webelement to center of screen.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    
    # type_element = choose_type_element(type_element)

    if type_element.upper() == 'CSS_SELECTOR':
        browser.execute_script(
            'document.querySelector("' + selector
            + '").scrollIntoView({block: "center"})'
        )
    elif type_element.upper() == 'XPATH':
        browser.execute_script(
            '''element = document.evaluate("'''+selector+'''", 
            document, null, XPathResult.FIRST_ORDERED_NODE_TYPE,
            null).singleNodeValue;
            element.scrollIntoView({block: "center"});'''
        )


def wait_element(selector, type_element='CSS_SELECTOR', time=30):
    """
    Definition
    ----------
    Waits a element in the current webpage in context be \
        totally visible.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]
    time : int
        Time, in seconds, that will be wait for the \
            visibility of element. The default value is 30 seconds. \n
        Example: \n\t\t time=30

    ----------

    Output
    ----------
    None

    """
    try:
        wait = WebDriverWait(browser, time)
        sleep(0.5)
        type_element_by = choose_type_element(type_element)
        wait.until(EC.visibility_of_element_located((
                type_element_by, selector)
            ))
        center_element(selector, type_element)
        wait_page_loaded()
    except:
        ...


def choose_type_element(type_element):
    if type_element.upper() == 'CLASS_NAME':
        type_element = By.CLASS_NAME
    elif type_element.upper() == 'CSS_SELECTOR':
        type_element = By.CSS_SELECTOR
    elif type_element.upper() == 'ID':
        type_element = By.ID
    elif type_element.upper() == 'LINK_TEXT':
        type_element = By.LINK_TEXT
    elif type_element.upper() == 'NAME':
        type_element = By.NAME
    elif type_element.upper() == 'PARTIAL_LINK_TEXT':
        type_element = By.PARTIAL_LINK_TEXT
    elif type_element.upper() == 'TAG_NAME':
        type_element = By.TAG_NAME
    elif type_element.upper() == 'XPATH':
        type_element = By.XPATH
    return type_element


def search_very_elements(selector, type_element='CSS_SELECTOR'):
    """
    Definition
    ----------
    Finds all elements with location similar of the \
        selector parameter
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t a[id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    type_element = choose_type_element(type_element)
    browser.find_elements(type_element, selector)
    center_element(selector, type_element)


def search_element(selector, type_element='CSS_SELECTOR'):
    """
    Definition
    ----------
    Finds one element with the exact match location of \
        the selector parameter
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    type_element = choose_type_element(type_element)
    browser.find_element(type_element, selector)
    center_element(selector, type_element)


def counter_elements(selector, type_element='CSS_SELECTOR'):
    """
    Definition
    ----------
    Counts all elements with location similar of the \
        selector parameter
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    type_element = choose_type_element(type_element)
    center_element(selector, type_element)
    elements = browser.find_elements(type_element, selector)
    return elements.__len__()


def extract_text(selector, type_element='CSS_SELECTOR'):
    """
    Definition
    ----------
    Extracts the text anchored in the element.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    type_element = choose_type_element(type_element)
    element = browser.find_element(type_element, selector)
    text_element = element.text
    center_element(selector, type_element)
    return text_element


def get_attribute(selector, attribute, type_element='CSS_SELECTOR'):
    type_element = choose_type_element(type_element)
    element = browser.find_element(type_element, selector)
    center_element(selector, type_element)
    attribute_value = element.get_attribute(attribute)
    return attribute_value


def click_element(selector, type_element='CSS_SELECTOR'):
    """
    Definition
    ----------
    Click in the element informed with the exact match location of \
        the selector parameter.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    try:
        type_element = choose_type_element(type_element)
        center_element(selector, type_element)
        element = browser.find_element(type_element, selector)
        element.click()
        wait_page_loaded()
    except:
        ...


def write_in_element(selector, text, type_element='CSS_SELECTOR'):
    """
    Definition
    ----------
    Writes in the element informed with the exact match location of \
        the selector parameter.
    Require to inform selector parameter.

    ----------

    Parameters
    ----------
    selector : str
        Location of a DOM element, also called xpath. \n
        Example: \n\t\t [id="sdgBod"] > span:nth-child[2]

    ----------

    Output
    ----------
    None

    """
    type_element = choose_type_element(type_element)
    center_element(selector, type_element)
    element = browser.find_element(type_element, selector)
    element.send_keys(text)
    wait_page_loaded()


def mouse_click(webelement):
    """
    Definition
    ----------
    Performs double left click of mouse in the webelement.
    Require to inform webelement parameter.

    ----------

    Parameters
    ----------
    webelement : WebDriver
        A webelement of the type WebDriver of Selenium library. \n
        Example: \n\t\t browser.search_element(\
            By.XPATH("//input[@value='submit']"))


    ----------

    Output
    ----------
    None

    """
    action = ActionChains(browser)
    action.double_click(webelement).perform()


def close_window(window):
    """
    Definition
    ----------
    Stops the Firefox browser controlled by automation.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    browser.switch_to.window(window)
    browser.close()


def close_all_windows_but_this(window_id):
    """
    Definition
    ----------
    Stops the Firefox browser controlled by automation.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    windows_list = browser.window_handles
    for window in windows_list:
        if window != window_id:
            browser.switch_to.window(window)
            browser.close()


def stop_browser():
    """
    Definition
    ----------
    Stops the Firefox browser controlled by automation.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    windows_list = len(browser.window_handles)

    while windows_list > 0:
        window = browser.window_handles[0]
        close_window(window)
        windows_list = windows_list - 1
