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
    elif type_element.upper() == 'CSS_SELECTOR':
        selector = "iron-collapse#collapse > div > ytd-search-filter-group-renderer:nth-child(" + str(group) + ") > ytd-search-filter-renderer:nth-child(" + str(item) + ") > a#endpoint > div > yt-formatted-string"
    selenium.wait_element(selector, type_element)
    selenium.search_element(selector, type_element)
    selenium.click_element(selector, type_element)


def filter_search(filter_group_name, filter_item_name, type_element='CSS_SELECTOR'):
    global group
    global item
    group = 0
    item = 0

    if filter_group_name.upper() == 'UPLOAD DATE': 
        group = 1
        if filter_item_name.upper() == 'LAST HOUR': 
            item = 1
        elif filter_item_name.upper() == 'TODAY':
            item = 2
        elif filter_item_name.upper() == 'THIS WEEK':
            item = 3
        elif filter_item_name.upper() == 'THIS MONTH':
            item = 4
        elif filter_item_name.upper() == 'THIS YEAR':
            item = 5
    elif filter_group_name.upper() == 'TYPE': 
        group = 2
        if filter_item_name.upper() == 'VIDEO': 
            item = 1
        elif filter_item_name.upper() == 'CHANNEL':
            item = 2
        elif filter_item_name.upper() == 'PLAYLIST':
            item = 3
        elif filter_item_name.upper() == 'MOVIE':
            item = 4
    elif filter_group_name.upper() == 'DURATION': 
        group = 3
        if filter_item_name.upper() == 'UNDER 4 MINUTES': 
            item = 1
        elif filter_item_name.upper() == '4 - 20 MINUTES':
            item = 2
        elif filter_item_name.upper() == 'OVER 20 MINUTES':
            item = 3
    elif filter_group_name.upper() == 'FEATURES': 
        group = 4
        if filter_item_name.upper() == 'LIVE': 
            item = 1
        elif filter_item_name.upper() == '4K':
            item = 2
        elif filter_item_name.upper() == 'HD':
            item = 3
        elif filter_item_name.upper() == 'SUBTITLES/CC':
            item = 4
        elif filter_item_name.upper() == 'CREATIVE COMMONS':
            item = 5
        elif filter_item_name.upper() == '360':
            item = 6
        elif filter_item_name.upper() == 'VR180':
            item = 7
        elif filter_item_name.upper() == '3D':
            item = 8
        elif filter_item_name.upper() == 'HDR':
            item = 9
        elif filter_item_name.upper() == 'LOCATION':
            item = 10
        elif filter_item_name.upper() == 'PURCHASED':
            item = 11
    elif filter_group_name.upper() == 'SORT BY': 
        group = 5
        if filter_item_name.upper() == 'RELEVANCE': 
            item = 1
        elif filter_item_name.upper() == 'UPLOAD DATE':
            item = 2
        elif filter_item_name.upper() == 'VIEW COUNT':
            item = 3
        elif filter_item_name.upper() == 'RATING':
            item = 4
    
    if type_element.upper() == 'CSS_SELECTOR':
        item = item * 2

    status = 'open'
    filter_menu(status)
    select_filter_element(group, item, type_element)
    status = 'close'
    filter_menu(status)


def download_video(link_video, format, path = None):
    from pytube import YouTube
    if format.upper() == 'AUDIO':
        stream_list = YouTube(link_video).streams.filter(only_audio=True, file_extension='mp4')
        stream_choosed = stream_list.order_by('abr').desc()[0]
    elif format.upper() == 'VIDEO':
        stream_list = YouTube(link_video).streams.filter(only_video=True, file_extension='mp4')
        stream_choosed = stream_list.order_by('res').desc()[0]
    else:
        TypeError('Format invalid.')
    output_download = stream_choosed.download(output_path=path)
    return output_download
        
