# Appium-Testing
Functional tests for Rider Verification app.

Setup Instructions

NOTE: This guide assumes you have Android Studio up and running
NOTE:  After you change PATH stuff, restart your Command Prompt

Download node and npm tools 
•	Add npm and nodejs to your system PATH 
•	My path:   C:\Program Files\nodejs

Install Appium
•	Open Admin command prompt
  - npm install -g appium
• Add Appium to to the system PATH
  -	My path: C:\Program Files (x86)\Appium

Test Appium
•	Open Admin command prompt and run:
  -	appium

Download/install the newest JDK (You probably have the JDK, just double check the paths)
•	Set JAVA_HOME to be your JDK path
  -	My path: C:\Program Files\Java\jdk1.8.0_111
•	Add the JDK bin to your system PATH
  -	My path: C:\Program Files\Java\jdk1.8.0_111\bin

Download/install the Android SDK (You probably have the Android SDK, just double check the paths)
•	Set ANDROID_HOME to your Android SDK path (likely in user variables)
  -	My path:  C:\Users\loren.brown\AppData\Local\Android\sdk
•	Add “tools” to your system PATH (likely in user variables)
  -	My path: C:\Users\loren.brown\AppData\Local\Android\sdk\tools
•	Add “platform-tools” to your system PATH (likely in user variables)
  -	My path: C:\Users\loren.brown\AppData\Local\Android\sdk\platform-tools

Download Apache Ant
•	Decompress and move to somewhere that is not your downloads folder
  -	I put mine in “tools” directory on the C drive
•	Add Ant to your system PATH (not sure if just the bin is required or not so I did both)
  -	My path: C:\tools\apache-ant-1.10.0
  -	My path: C:\tools\apache-ant-1.10.0\bin

Download Apache Maven
•	Decompress and move to somewhere that is not your downloads folder
  -	I put mine in “tools” directory on the C drive
•	Set M2HOME to the “maven” directory
  -	My path: C:\tools\apache-maven-3.3.9\
•	Set M2 to the “maven/bin” directory
  -	My path:  C:\tools\apache-maven-3.3.9\bin
•	Add “bin” to your system PATH (I know it is redundant but do it)
  -	My path:  C:\tools\apache-maven-3.3.9\bin

Install Python 2.7
•	Make sure python27 is in you system PATH
  -	My path:  C:\tools\python2   (NOTE: this is a weird path)
•	Add “scripts” to your system PATH (this enables pip)
  -	My path:  C:\tools\python2\Scripts   (NOTE: this is a weird path)
•	Test the “pip” command

Install the Appium python plugin (cmd)
•	pip install Appium-Python-Client

Create your test script 
•	Examples can be found here https://github.com/appium/sample-code/tree/master/sample-code/examples/python 
•	NOTE:  The “platformVersion” and “app” variables need to be changed   

Run your Android emulator
•	Just leave it running….

Run your Python script
•	Python your_script.py
