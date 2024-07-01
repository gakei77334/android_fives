# Virgin Fives App Automation Script

This Python script automates the daily 'FIVES' game on the Virgin Fives app using ADB (Android Debug Bridge) and PIL (Python Imaging Library). The script is designed to perform specific interactions with an Android device to select football players daily, if selections are available.

**Key Features:**
* Device Interaction: Automates waking the device, unlocking it, opening the Virgin Fives app, and navigating through the interface.
* Pixel Color Analysis: Captures screenshots and analyzes specific pixel values to determine the availability of players for selection.
* Automated Workflow: Continuously checks for player availability and makes selections based on the analysis.
* Scheduled Operations: Executes tasks at specified intervals, including putting the device to sleep and clearing open windows.

**Technologies Used:**
* Python
* ADB (Android Debug Bridge)
* PIL (Python Imaging Library)
* NumPy

**Automated Actions:**
* The script performs the following actions in a loop:
* Wakes the device and swipes to unlock.
* Opens the Virgin Fives app.
* Navigates to the 'FIVES' game section.
* Captures screenshots and analyzes specific pixel colors to check player availability.
* Selects available players based on pixel color analysis.
* Puts the device to sleep and waits for the next cycle.

**Pixel Color Analysis:**
* Captures screenshots at specified coordinates.
* Analyzes the red channel value of the pixel to decide on the next action.
* Executes specific taps based on the pixel color analysis to select players.
