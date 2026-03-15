# -*- coding: utf-8 -*- 
import tempfile
import random
import string
import time
import os

date = time.strftime("%d%m%Y_%H%M%S")
tmp = tempfile.gettempdir()

class constant():
    folder_name = '.'
    _prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    file_name_results = 'sys_log_{rand}_{current_time}'.format(
        rand=_prefix,
        current_time=date
    )
    max_help = 27
    CURRENT_VERSION = '{}.{}.{}'.format(random.randint(1,5), random.randint(0,9), random.randint(0,9))
    output = None
    modules_dic = {}
    nb_password_found = 0  # Total password found
    password_found = []  # Tab containing all passwords used for dictionary attack
    stdout_result = []  # Tab containing all results by user
    pypykatz_result = {}
    finalResults = {}
    profile = {
        'APPDATA': u'{drive}:\\Users\\{user}\\AppData\\Roaming\\',
        'USERPROFILE': u'{drive}:\\Users\\{user}\\',
        'HOMEDRIVE': u'{drive}:',
        'HOMEPATH': u'{drive}:\\Users\\{user}',
        'ALLUSERSPROFILE': u'{drive}:\\ProgramData',
        'COMPOSER_HOME': u'{drive}:\\Users\\{user}\\AppData\\Roaming\\Composer\\',
        'LOCALAPPDATA': u'{drive}:\\Users\\{user}\\AppData\\Local',
    }
    username = u''
    keepass = {}
    hives = {
        'sam': os.path.join(
            tmp,
            ''.join([random.choice(string.ascii_lowercase) for x in range(6, 12)]) + '.tmp'),
        'security': os.path.join(
            tmp,
            ''.join([random.choice(string.ascii_lowercase) for x in range(6, 12)]) + '.dat'),
        'system': os.path.join(
            tmp,
            ''.join([random.choice(string.ascii_lowercase) for x in range(6, 12)]) + '.log')
    }
    quiet_mode = False
    st = None
    drive = u'C'
    user_dpapi = None
    system_dpapi = None
    lsa_secrets = None
    is_current_user = False  # If True, Windows API are used otherwise dpapi is used
    user_password = None
    wifi_password = False  # Check if the module as already be done
    module_to_exec_at_end = {
        "winapi": [],
        "dpapi": [],
    }
    dpapi_cache = {}
