# Hello Pytest w. Appium

1. **Install Prerequisites**:
   - Install Android Studio and set up an Android Virtual Device (AVD).
   - Install Appium and ensure the Appium server is running.
   - Install Python and the Appium-Python-Client library using:

```bash
pip install Appium-Python-Client
```

2. **Start the Android Emulator**:

   - Open Android Studio.
   - Go to **Tools > Device Manager** and start your configured Android emulator.

3. **Start the Appium Server**:
   - Open the Appium Desktop application or run the Appium server from the command line:

```bash
appium
```

4. **Verify the Emulator and Appium Setup**:
   - Ensure the emulator is running by executing:

```bash
adb devices
```

You should see the emulator listed as a connected device. - Ensure the Appium server is running on `http://localhost:4723`.

5. **Run the Script**:
   - Save the provided script as `test_hello_appium.py`.
   - Run the script using Python:

```bash
python test_hello_appium.py
```

6. **Expected Output**:
   - The script will launch the Chrome browser on the emulator, navigate to `https://www.paulserban.eu`, print the page title, and close the browser after 5 seconds.

If you encounter issues, ensure:

- The `desired_caps` dictionary matches your emulator's configuration.
- The Appium server is running and accessible.
