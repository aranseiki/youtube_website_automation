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
        download_folder = 'download'
        log_folder = 'log'
        root_path = '.\\'+'files'+'\\'
        current_day_path = (
            root_path+'\\'+current_day_folder+'\\'
        )
        download_path = (
            root_path+'\\'+current_day_folder+'\\'+download_folder+'\\'
        )
        log_path = (
            root_path+'\\'+current_day_folder+'\\'+log_folder+'\\'
        )
        csv_file_name = 'series_list_downloaded.csv'
        log_name = 'log_'+current_date+'.txt'
        log_file = log_path + log_name
        csv_file = download_path + csv_file_name

        custom.create_directory(root_path)
        custom.create_directory(current_day_path)
        custom.create_directory(download_path)
        custom.create_directory(log_path)

        basefile_path = '.\\files\\database\\20_03_2022\\base.txt'
        
        basefile = open(basefile_path, 'r', encoding='utf8')
        basefile = basefile.read().split('\n')
        index = 1
        for item in basefile:
            basefile[index - 1] = item.split(',')
            index = index + 1
        
        basefile

    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the initial process: Preparing the environment."
            )
        raise message_error

    # Preparing the datalist from base file
    try :
        datalist = []

    except:
        ...

    # Access the webpage required by user with browser
    try:
        # OPEN THE BROWSE WITH A URL
        url = "https://www.youtube.com/"
        browsername = 'chrome'
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
        texto_pesquisa = 'Sirenia'
        selenium.write_in_element(selector, texto_pesquisa)

        sleep(2)

        # CLICKS IN SEARCH ICON
        selector = "ytd-masthead > \
            div:nth-child(4) > \
            div:nth-child(2) > \
            ytd-searchbox > \
            button > \
            yt-icon"
        selenium.search_element(selector)
        selenium.click_element(selector)

        # Filtering the search
        sleep(3)
        youtube.filter_search('TYPE', 'channel', 'xpath')
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 2: searching text on website."
            )
        raise message_error

    # Localizing the video
    try:
        sleep(3)
        type_element='xpath'
        channel_name = 'Sirenia'
        selector = "//div[@id=" + \
            "'contents'" + \
            "]/ytd-channel-renderer/div[@id=" + \
            "'content-section'" + \
            "]/div[@id=" + \
            "'info-section'" + \
            "]/a/div[@id=" + \
            "'info'" + \
            "]/ytd-channel-name/div/div/\
            yt-formatted-string[text()='" + channel_name + "']"
        official_channel = True
        if official_channel == True:
            selector = selector + "/ancestor::div/ancestor::div/\
                ancestor::ytd-channel-name/ytd-badge-supported-renderer\
                /div[@aria-label=" + \
                "'Official Artist Channel'" + "]"
        selenium.search_element(selector, type_element)
        selenium.click_element(selector, type_element)
        sleep(3)

        tab_name = 'Playlists'
        youtube.menu_horizontal_in_channel(tab_name)
        sleep(1)

        playlist_name = 'Arcane Astral Aeons'
        selector = "//div[@id=" + \
            "'items'" + \
            "]/ytd-grid-playlist-renderer/h3/a[text()='" + \
            playlist_name + \
            "']/ancestor::h3/following-sibling::yt-formatted-string"
        selenium.click_element(selector, type_element)
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 4: Localizing the video"
            )
        raise message_error

    # Salving the URL of video(s) in the local list
    try:
        sleep(3)
        selector = "//div[contains(@id, " + \
            "'contents'" + \
            ")]/ytd-playlist-video-list-renderer/div[contains(@id, " + \
            "'contents'" + \
            ")]/ytd-playlist-video-renderer"
        total_videos = selenium.counter_elements(
            selector, type_element='xpath'
        )
        counter_video = 1
        id_video = 1
        video_source_list = []
        while counter_video <= total_videos:
            selector = "//div[contains(@id, " + \
                "'contents'" + \
                ")]/ytd-playlist-video-list-renderer/div[contains(@id, " + \
                "'contents'" + \
                ")]/ytd-playlist-video-renderer[" + \
                str(id_video) + \
                "]/div[@id=" + \
                "'content'" + \
                "]/div/div[@id=" + \
                "'meta'" + \
                "]/h3/a"
            attribute = 'href'
            video_source_list.append(
                selenium.get_attribute(
                    selector, attribute, type_element='xpath'
                )
            )
            id_video = id_video + 1
            counter_video = counter_video + 1
        
        sleep(3)
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 3: Colleting video link"
            )
        raise message_error

    # Downloading video
    try:
        format = 'audio'
        path = download_path + \
        '\\' + \
        texto_pesquisa.replace('\\', ' ') \
            .replace('/', ' ') \
            .replace('//',  '') \
            .replace(':', ' ') \
            .replace('*', ' ') \
            .replace('?', ' ') \
            .replace('"', ' ') \
            .replace("'", ' ') \
            .replace('<', ' ') \
            .replace('>', ' ') \
            .replace('|', ' ')
        index = 1
        
        for link_video in video_source_list:
            print('index: ' + str(index))
            output_download = youtube.download_video(link_video, format, path)
            sleep(1)
            filename_output = output_download.split('\\')[-1]
            modified_filename = filename_output.replace('.mp4', '.mp3')
            new_filename = output_download.replace(
                filename_output, modified_filename
            )
            if os.path.exists(new_filename):
                new_filename_boolean = True
                os.remove(new_filename)
                while new_filename_boolean == True:
                    if not os.path.exists(new_filename):
                        new_filename_boolean = False
                sleep(1)
            os.rename(output_download, new_filename)
            sleep(1)
            index = index + 1
        
        ...
    except:
        if message_error == '':
            message_error = TypeError(
                "Error in the process 4: Downloading"
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