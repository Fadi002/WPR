-----
this project is dead
new project: https://github.com/Fadi002/unshackle


### <p align="center">Windows Password Removal</p>
<p align="center">
<strong>Windows Password Removal can remove passwords or change passwords for windows only, I made it because why not
</strong>
</p>
<br>

-----
### <p align="center"> Features </p>

<br><br>
<strong>+ Very easy to use</strong>
<br>
<strong>+ So fast and easy to install and uninstall</strong>
<br>
<strong>- You need to setup it manually</strong>
<br>
![cli](https://media.discordapp.net/attachments/1023225858133069844/1035681368623042601/unknown.png?width=823&height=427)
<br><br>

-----
### <p align="center">Setup</p>
<strong>Setup and compile</strong>
```
Requirements {
    Hiren’s BootCD PE from : https://www.hirensbootcd.org/ (not mine)
    size : 2.89GB
    Python (recommended 3.9): https://python.org
    Rufus : http://rufus.ie/
    A Brain OFC
}

Setup python and compile (you can skip this if you download the exe from releases) {
    step 1: Open the installer as administrator. Then click add to path button and install it.
    
    For compile {
        Step 1: just open cmd as administrator, then type "pip install pyinstaller". After that, open another cmd on the repo directory and type "pyinstaller --onefile WPR.py"
        Step 2: You should see a folder named "dist"
        Step 3: You will see WPR.exe inside it.
    }

}


Setup {
    Step 1: Burn Hiren’s BootCD PE.iso image using Rufus.
    Step 2: Copy WPR.exe to the USB.
    Step 3: Boot from the USB.
    Step 4: Go to your system partition, then go to windows\system32
    Step 5: Rename sethc.exe to sethc.exe.old
    Step 6: Rename WPR.exe to sethc.exe
    Step 7: Copy it to windows\system32
    Step 8: Reboot your system.
    Step 9: Press the shift button on your keyboard 5 times.
    Step 10: Now you can use the tool.
}

Uninstall WPR {
    Step 1 : Boot from the usb.
    Step 2 : Go to windows\system32
    Step 3 : Remove sethc.exe
    Step 4 : Rename sethc.exe.old to sethc.exe
    Step 5 : Reboot to your system.
}

```
```
Tutorial video : Soon
5 Stars = More features
```
-----

### <p align="center">Disclaimer</p>

<br><br>
* ***Please use this program only for educational purposes.***
* ***It is not meant to be used in any malicious way, and I decline any responsibility for what you do with it.***
<br><br>
-----

### <p align='center'>LICENSE WARNING</p>
<br>
<strong>MIT License </strong>

Copyright (c) 2022 Fadi1337

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
