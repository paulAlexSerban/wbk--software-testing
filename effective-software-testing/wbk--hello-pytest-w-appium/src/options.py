from appium.options.android import UiAutomator2Options

def get_android_options():
    options = UiAutomator2Options()
    options.device_name = "Android Emulator"
    options.platform_name = "Android"
    options.browser_name = "Chrome"
    options.automation_name = "UiAutomator2"
    options.new_command_timeout = 300
    options.uiautomator2_server_launch_timeout = 60000
    options.uiautomator2_server_install_timeout = 60000
    options.adb_exec_timeout = 20000
    options.android_install_timeout = 90000
    options.auto_grant_permissions = True
    options.no_reset = False
    options.full_reset = False
    options.dont_stop_app_on_reset = False
    return options