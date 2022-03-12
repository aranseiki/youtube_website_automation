import lib.selenium_utils as selenium


def filter_menu(status):
    if status.upper() == 'OPEN':
        selector = "tp-yt-paper-button#button.ytd-toggle-button-renderer"
        attribute = 'aria-pressed'
        checking_menu_state = selenium.get_attribute(selector, attribute)
        if checking_menu_state.upper() == 'FALSE':
            selector = 'ytd-search-sub-menu-renderer > div:nth-child(1) > div > ytd-toggle-button-renderer > a > tp-yt-paper-button > yt-icon'
            selenium.search_element(selector)
            selenium.click_element(selector)
    elif status.upper() == 'CLOSE':
        selector = "tp-yt-paper-button#button.ytd-toggle-button-renderer"
        attribute = 'aria-pressed'
        checking_menu_state = selenium.get_attribute(selector, attribute)
        if checking_menu_state.upper() == 'TRUE':
            selector = 'ytd-search-sub-menu-renderer > div:nth-child(1) > div > ytd-toggle-button-renderer > a > tp-yt-paper-button > yt-icon'
            selenium.search_element(selector)
            selenium.click_element(selector)


def select_filter_element(group, item, type_element = 'CSS_SELECTOR'):
    if type_element.upper() == 'XPATH':
        selector = "//ytd-search-filter-group-renderer[" + str(group) + "]/ytd-search-filter-renderer[" + str(item) + "]//a[contains(@id, 'endpoint')]/div/yt-formatted-string"
        selenium.wait_element(selector, type_element)
        selenium.search_element(selector, type_element)
        selenium.click_element(selector, type_element)
    elif type_element.upper() == 'CSS_SELECTOR':
        ...


def filter_search(filter_group_name, filter_item_name, type_element='CSS_SELECTOR'):
    global group
    global item
    group = 0
    item = 0
    if filter_group_name.upper() == 'UPLOAD DATE': 
        group = 1
        if filter_item_name.upper() == 'LAST HOUR': 
            item = 1
            ...
        elif filter_item_name.upper() == 'TODAY':
            item = 2
            ...
        elif filter_item_name.upper() == 'THIS WEEK':
            item = 3
            ...
        elif filter_item_name.upper() == 'THIS MONTH':
            item = 4
            ...
        elif filter_item_name.upper() == 'THIS YEAR':
            item = 5
            ...
    status = 'open'
    filter_menu(status)
    select_filter_element(group, item, type_element)
    status = 'close'
    filter_menu(status)
