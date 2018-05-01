#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Preethi Vaidyanathan
# px1621@rit.edu
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
    This script is called directly by the compiler and does 3 things:

        1. reads filenames
        #. calls the widget tool for the files
        #. ...

    Update information is contained in the git commit messages.

    See this project on `BitBucket.org <https://bitbucket.org/PVNathan/interactivegui/overview>`_
'''

## FUTURE IMPORTS FOR SWITCHING TO PYTHON 3.0 FROM 2.6+ (NEEDS TO BE IN EACH MODULE)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from __future__ import division;            # http://legacy.python.org/dev/peps/pep-0238/
from __future__ import absolute_import;     # http://legacy.python.org/dev/peps/pep-0328/
from __future__ import print_function;      # http://legacy.python.org/dev/peps/pep-3105/
from __future__ import unicode_literals;    # http://legacy.python.org/dev/peps/pep-3112/
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# IMPORT THE ImageLabeling PACKAGE
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from ImageLabeling import *;
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------



# THIS SECTION WILL ONLY RUN WHEN THIS MODULE IS CALLED DIRECTLY BY THE PYTHON INTERPRETER (COMPILER)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
if ( __name__ == '__main__' ):

    
    # PROVIDE A LIST OF CUSTOMIZATION DATA FOR INITIALIZING AN INSTANCE OF A QApplication (ONLY ONE MAY RUN AT A TIME)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    QtApplicationParamsList = [];
    
    CurrentQtApplicationObject = PySideQtGUI.QApplication( QtApplicationParamsList );
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    RootPathStr = os.path.expanduser( '~/ImageAnnotationSoftware/' );
   

    ImageFilePathStr = os.path.join( RootPathStr, 'SnagImages' );
    
    SegmentLabelsFilePathStr = os.path.join( RootPathStr, 'SnagSegmentLabels' );
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # SETUP THE LIST OF IMAGES
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------

    ImageFileExtensionStrList = [ '.jpg', '.jpeg', '.png', '.tiff', '.bmp' ];

    ImageFileFolderContentsStrList = os.listdir( ImageFilePathStr );
    # Remove any image or file not present in the folder or which you don't want to be included in the GUI
    # RemoveImagesFiles = ['example.jpg','.DS_Store'];
    for item in RemoveImagesFiles:
        if item in ImageFileFolderContentsStrList: 
            ImageFileFolderContentsStrList.remove(item);
        #fi
    #rof
    ImageFileFolderContentsStrList = sorted(ImageFileFolderContentsStrList, key=lambda x: (int(re.sub('\D','',x)),x));

    # Get the files from above list that are only images
    ImageFileNameStrList = [];
    for CrntFileNameStr in ImageFileFolderContentsStrList:
        CrntFileExtensionStr = ( os.path.splitext( CrntFileNameStr )[1] );
        if ( CrntFileExtensionStr.lower() in ImageFileExtensionStrList ):
            ImageFileNameStrList.append( CrntFileNameStr );
        #fi

    #rof


    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # CREATE WINDOW OBJECT, DRAW IT, BRING IT INTO FOCUS (FOR THE OS)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    AppWindow = AppWidgetTools.SegmentationToolWindowClass(
                                                            RootPathStr,
                                                            ImageFilePathStr, 
                                                            SegmentLabelsFilePathStr, 
                                                            ImageFileNameStrList
                                                          );

    AppWindow.show();
    AppWindow.raise_();
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # EXIT PYTHON WHEN THE QApplication HAS FINISHED EXECUTING (RUNNING)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    sys.exit( CurrentQtApplicationObject.exec_() );
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    
#fi 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
