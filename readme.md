



# setup guide
# Mac
1. install brew command   https://phoenixnap.com/kb/install-homebrew-on-mac
2. install testract exe using brew https://github.com/tesseract-ocr/tessdoc#5xx 
2. install python 3.8.5 using brew
  
pytesseract                                       0.3.10
pytest                                            7.1.3
pytest-html                                       3.1.1
PyAutoGUI                                         0.9.53
numpy                                             1.23.3
opencv-python                                     4.6.0.66

5. calibrate screen and pyautogui screen
6. Run the test

# known issue
  Multiple text need to be sorted from top to bottom
  
# dependencies

testrect version 5
pyautogui
numpy
open cv

 pytest -p no:logging  ./../EOTest/**share**.py  --html=report.html
API method:
  getLocation(text,index=0)
  clicOnText(text,index=0)
  waitForTextToVisible(text,index)
  wait(seconds)
  isTextVisible()
  clickUsingAxis(horizonntal=0,vertical=0,text,index=0)
  PerfomVerticalScrollAtlocation(by_pixel)
  moveTo(text,index)
  clickCordinate(x,y)
  rightContextClick(text,index=0)
  leftContextClick(text,index=0)

  
  