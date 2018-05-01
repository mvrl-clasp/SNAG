README
--------------------------------------------------------------------------------------------------------------------------------

A PySide (Qt) application for annotating image regions with labels. Please read License.txt for license information.


Dependencies
================================================================================================================================

Developed and tested in OS X Yosemite (10.10.3) and OS X Mavericks (10.9).

Other versions may work, but these are the versions we have tested with:

* Pillow (Python Image Library) 2.8.1
* PySide 1.2.2
  * Qt 4.8.6

If you have Python and have a bash (shell) terminal, you should be able to install these with: ::  
    
    sudo -E pip install --upgrade pillow;
    sudo -E pip install --upgrade pyside;

or you can download the latest git source for PySide and build it directly (update your local qmake path): ::  

    sudo -E pip install -e git+https://github.com/PySide/pyside-setup.git#egg=PySide --install-option="--qmake=/usr/bin/qmake-4.8"


Note: You cannot use PySide with Qt versions 5+, it only works with versions 4.x, and has not yet been updated. If you would like to work with the latest Qt features in version 5.x, you will need to switch-over to developing natively in C++ instead of Python. This may be substantially more complex and daunting, depending on your programming experience, so please carefully consider the feature differences between Qt5 and Qt4. We would not recommend jumping into Qt5 unless you are prepared for project management with multiple code-files in C++.


Editor Layout
================================================================================================================================

All our code is written using Sublime Text 3 (Beta), and these are the relevant font and display settings: ::  
    { 
      "wrap_width": 160,
      "rulers": [ 121 ],
      "font_size": 9,
      "font_face": "Source Code Pro",
      "tab_size": 4
    }

Our preference is to use comment dividers to separate the code scopes and algorithmic procedures, and these comment lines extend to the "ruler" width for a consistent aesthetic.


Links and References
================================================================================================================================

* PySide: https://wiki.qt.io/Category:LanguageBindings::PySide
* Qt Download Archive: http://download.qt.io/archive/qt/4.8/
* PySide source: https://pypi.python.org/packages/source/P/PySide/PySide-1.2.2.tar.gz
* PySide Documentation Site: https://wiki.qt.io/PySideDocumentation
