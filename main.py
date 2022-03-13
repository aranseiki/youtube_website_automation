import lib.selenium_utils as selenium
import lib.python_functions_utils as custom
import lib.youtube_functions as youtube
import os
import datetime as dt
from time import sleep

try:

    # Preparing the environment
    try:
        message_error = ''
        current_date = dt.datetime.now().strftime('%d/%m/%Y').replace('/', '_')
        execution_initial = dt.datetime.now().strftime('%H:%M:%S')
        current_day_folder = current_date
        export_folder = 'export'
        log_folder = 'log'
        root_path = '.\\'+'files'+'\\'
        current_day_path = (
            root_path+'\\'+current_day_folder+'\\'
        )
        export_path = (
            root_path+'\\'+current_day_folder+'\\'+export_folder+'\\'
        )
        log_path = (
            root_path+'\\'+current_day_folder+'\\'+log_folder+'\\'
        )
        csv_file_name = 'series_list_exported.csv'
        log_name = 'log_'+current_date+'.txt'
        log_file = log_path + log_name
        csv_file = export_path + csv_file_name

        custom.create_directory(root_path)
        custom.create_directory(current_day_path)
        custom.create_directory(export_path)
        custom.create_directory(log_path)
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the initial process: Preparing the environment."
            )
        raise message_error

    # Access the webpage required by user with browser
    try:
        # OPEN THE BROWSE WITH A URL
        url = "https://www.youtube.com/"
        browsername = 'Firefox'
        selenium.start_browser(url, browsername)
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 1: Starting browser."
            )
        raise message_error
    
    # Search text on site
    try:
        # SELECT SEARCH BAR
        selector = "input[id="+"'search'"+"]"
        selenium.search_element(selector)
        selenium.click_element(selector)
        # WRITE TEXT IN SEARCH BAR SELECTED
        texto_pesquisa = 'chinês mandarim básico completo aula de chinês'
        selenium.write_in_element(selector, texto_pesquisa)

        sleep(2)

        # CLICKS IN SEARCH ICON
        selector = "ytd-masthead > div:nth-child(4) > div:nth-child(2) > ytd-searchbox > button > yt-icon"
        selenium.search_element(selector)
        selenium.click_element(selector)
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 2: searching text on website."
            )
        raise message_error

    # Filtering the search
    try:
        sleep(3)
        youtube.filter_search('TYPE', 'PLAYLIST', 'xpath')
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 3: filtering series list on webpage."
            )
        raise message_error

    # Entering in the correct item 
    try:
        sleep(3)
        type_element='xpath'
        selector = "//span[contains(text(), " + \
            "'Curso de Chinês Mandarim Básico Completo'" + \
            ")]/ancestor::a/following-sibling::yt-formatted-string/a[contains(text(), " + \
            "'View full playlist'" + ")]"
        selenium.click_element(selector, type_element)
        selector = "//div[contains(@id, " + \
            "'contents'" + \
            ")]/ytd-playlist-video-list-renderer/div[contains(@id, " + \
            "'contents'" + \
            ")]/ytd-playlist-video-renderer"
        sleep(3)
        total_videos = selenium.counter_elements(selector, type_element='xpath')
        counter_video = 1
        id_video = 1
        video_source_list = []
        while counter_video <= total_videos:
            selector = "//div[contains(@id, " + "'contents'" + ")]/ytd-playlist-video-list-renderer/div[contains(@id, " + "'contents'" + ")]/ytd-playlist-video-renderer[" + str(id_video) + "]/div[@id=" + "'content'" + "]/div/div[@id=" + "'meta'" + "]/h3/a"
            attribute = 'href'
            video_source_list.append(selenium.get_attribute(selector, attribute, type_element='xpath'))
            id_video = id_video + 1
            counter_video = counter_video + 1
        
        sleep(3)

    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 3: filtering series list on webpage."
            )
        raise message_error

except:
    if not str(message_error).__contains__('[Internal Business Error]'):
        message_error = '[Internal System Error]: ' + str(message_error)
    status = 'NOK'
    message = message_error

finally:
    try:
        # CLOSE THE BROWSER
        # selenium.stop_browser()
        ...
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the final process: Stopping the browser."
            )

    if message_error == '':
        status = 'OK'
        message = 'Process have been done with success.'

    current_time_log = dt.datetime.now().strftime('%H:%M:%S')
    file_exists = os.path.exists(log_file)
    if not file_exists:
        custom.save_csv(log_file, 'w', [
            'Status ',
            'Message Execution ',
            'DateTime Initial Execution ',
            'Time Final Execution '
        ])
    log = open(log_file, 'a', encoding='utf8')
    log_content = (
        status,
        message,
        current_date.replace('_', '/') + ': ' + execution_initial,
        current_time_log
    )
    log_content = str(
        log_content
    ).replace('(', '').replace(')', '').replace('TypeError', '')
    log.write(log_content + '\r\n')
    log.close()
