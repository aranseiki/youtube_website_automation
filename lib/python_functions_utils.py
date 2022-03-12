import os
import csv
import smtplib
import ssl


navegador = ''


def cls():
    """
    Definition
    ----------
    Clear the terminal history.

    ----------

    Parameters
    ----------
    No parameters

    ----------

    Output
    ----------
    None

    """
    os.system('cls')


def create_directory(path):
    """
    Definition
    ----------
    Creates a folder in the location informed by path parameter.
    Requires to inform path parameter.

    ----------

    Parameters
    ----------
    path: str
        Path where the folder will be created, including the \
            name of the folder to be created. \n
        Example: \n\t\t 'C:\\Projects\\AutomationTests' \n\t
        In this example, the path to create the folder is \
            'C:\\Projects\\', \
                where the folder to be created is AutomationTests.

    ----------

    Output
    ----------
    None

    """
    if not os.path.exists(path):
        os.mkdir(path)


def save_csv(file, mode, content):
    """
    Definition
    ----------
    Saves the content of a list object in a file.
    Requires to inform file, mode, and content parameters.

    ----------

    Parameters
    ----------
    * file: str \n
        Path where the file will be created, including the \
            name of the file to be handled. \n
        Example: \n\t\t 'C:\\Projects\\AutomationTests\\export.csv' \n\t
        In this example, the path to create the file is \
            'C:\\Projects\\AutomationTests', \
                where the file to be created is export.csv.

    * mode: str \n
        Indicates how to the file will be handled. \n
            ‘r’     Read        Open a file for read only \n\t\t
            ‘w’     Write       Open a file for write only (overwrite) \n\t\t
            ‘a’     Append      Open a file for write only (append) \n\t\t
            ‘r+’    Read+Write  open a file for both reading and writing \n\t\t
            ‘x’     Create      Create a new file \n\t\t
        Example: \n\t\t 'w' \n\t
        In this example, the mode to create the file is \
            write, overwriting the content before. \

    * content: list \n
        List of string for to extract to .csv file.
        Example: \n\t\t ['apple', 'orange', 'Strawberry']

    ----------

    Output
    ----------
    None

    """
    handled_file = open(file, mode, encoding='utf8')
    writer = csv.writer(handled_file)
    writer.writerow(content)
    handled_file.close()


def handling_attachment(content_attachment):
    """
    Definition
    ----------
    handles the content of the attachment removing special \
        characters as comma or quotation marks
    Requires to inform content_attachment parameter.

    ----------

    Parameters
    ----------
    * content_attachment: list \n
        List of string. \n
        Example: \n\t\t ['apple', 'orange', 'Strawberry']

    ----------

    Output
    ----------
    Returns a string with the content of list concatenated \
        without special characters.

    """
    content_attachment = str(
        content_attachment
    ).replace('[', '').replace('\\n', ' ')\
        .replace('"', '').replace(';', '')\
        .replace("', '", "'; '").replace(',', '')\
        .replace(';', ',').replace(']', '\r\n')
    return content_attachment


def send_email_outlook(address_from, password, address_to, message):
    """
    Definition
    ----------
    Sends e-mail from Microsoft Outlook server. \n
    Requires to inform address_from, password, \
        address_to, and message parameters.

    ----------

    Parameters
    ----------
    * address_from: str \n
        String to indicate the e-mail address that will be send from. \
            Also indicates the address that will be \
                make logon in the e-mail server. \n
            Example: \n\t\t 'First name and last name <alias_from@domain.com>'

    * password: str \n
        String that inform the password. \
        The password not will be saved internally not at all, you're secure. \n
            Example: \n\t\t ['apple', 'orange', 'Strawberry']

    * address_to: str \n
        String to indicate the e-mail address which  it will be sent. \n
            Example: \n\t\t 'alias_to@domain.com'

    * message: str \n
        String to indicate the content of e-mail that will be sent. \n
            Example: \n\t\t
                '''From: {}
                    To: {}
                    Subject: {}
                    Content-Type: multipart/mixed;
                    Content-Disposition: attachment; filename="{}"

                    {}

                '''
        In this example, a structure formated for to concatenate string and \
            variable, defining the variable spaces by "{}". \
                This also accepts attachment.
    ----------

    Output
    ----------
    None

    """
    login = address_from.split('<')[1].replace('>', '')
    server = smtplib.SMTP('smtp.office365.com')
    server.connect("smtp.office365.com", 587)
    server.ehlo('hello')
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login(str(login), password)
    cls()
    server.sendmail(address_from, address_to, message)
    server.quit()


def serie_list_handling(list_param):
    """
    Definition
    ----------
    handles the content of the list of string removing special \
        characters as semicolon or quotation marks

    ----------

    Parameters
    ----------
    * list_param: list \n
        List of string. \n
        Example: \n\t\t ['apple', 'orange', 'Strawberry']

    ----------

    Output
    ----------
    Returns a string with the content of list concatenated \
        without special characters.

    """
    return str(list_param)\
        .replace("', \'", ', ')\
        .replace('\\r\\n,', '\r\n')\
        .replace('\r', "', '")\
        .replace('\\r', "', '")\
        .replace('\n', "', '")\
        .replace('\\n', "', '")\
        .replace("']", '')\
        .replace('"]', "")\
        .replace("['", '')\
        .replace('["', "")\
        .replace('"', "'")\
        .replace('"', "")\
        .replace('""', "")\
        .replace("''", "")\
        .replace("', , '", "', '")\
        .replace("' ", "'")\
        .replace(", ,", "")\
        .replace("' ,", "',")\
        .replace("', '", ";")\
        .split('\r\n')
