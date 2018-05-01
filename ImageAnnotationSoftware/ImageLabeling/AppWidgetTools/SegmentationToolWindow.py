#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Preethi Vaidyanathan
# preetivaidya1@gmail.com
# http://mvrl.cis.rit.edu
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# FUTURE IMPORTS FOR SWITCHING TO PYTHON 3.0 FROM 2.6+ (NEEDS TO BE IN EACH MODULE)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from __future__ import division;            # http://legacy.python.org/dev/peps/pep-0238/
from __future__ import absolute_import;     # http://legacy.python.org/dev/peps/pep-0328/
from __future__ import print_function;      # http://legacy.python.org/dev/peps/pep-3105/
from __future__ import unicode_literals;    # http://legacy.python.org/dev/peps/pep-3112/
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# COLLECTED IMPORTS MODULE
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from .._Imports import *;

from . import SegmentSelectorGraphicsViewWidget;
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------



# MAIN APPLICATION WINDOW CLASS FOR THE SEGMENTATION LABELLING TOOL
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
class SegmentationToolWindowClass( PySideQtGUI.QWidget ):
    

    # CLASS INITIALIZATION METHOD
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__( self, RootPathStr, ImageFilePathStr, SegmentLabelsFilePathStr, ImageFileNameStrList, ParentObj= None ):
        '''
            Class initialization method docstring.
        '''
        
        # INITIALIZE THE BASE CLASS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        PySideQtGUI.QWidget.__init__( self, ParentObj );            # INITIALIZE THE DEFAULT QWidget CLASS
        
        self.showMaximized();                                       # SHOW THE WINDOW MAXIMIZED FOR THE SCREEN
        
        self.setMouseTracking( True );                              # TO KEEP TRACK OF WHERE THE MOUSE IS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        # PARSE THE INPUTS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.RootPathStr = ( RootPathStr );
        
        self.ImageFilePathStr = ( ImageFilePathStr );
        
        self.SegmentLabelsFilePathStr = ( SegmentLabelsFilePathStr );
                
        self.ImageFileNameStrList = ( ImageFileNameStrList );
        
        self.CurrentDisplayImageIndexInt = ( 0 );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
                

        # CREATE A QSplitter FOR A COLLAPSABLE LAYOUT
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.MainLayoutSplitter = PySideQtGUI.QSplitter();
        self.MainLayoutSplitter.setOrientation( PySideQtCore.Qt.Horizontal );

        self.LeftSideWidgetObj = PySideQtGUI.QWidget();
        self.RghtSideWidgetObj = PySideQtGUI.QWidget();

        self.LeftSideWidgetLayoutObj = PySideQtGUI.QVBoxLayout();
        self.RghtSideWidgetLayoutObj = PySideQtGUI.QVBoxLayout();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # SETUP THE DATA-FILE FILE NAMES AS LISTS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ImageListWidgetObj = PySideQtGUI.QListWidget();

        self.SelectedImageFilePathNameStrList = [];
        
        self.SelectedSegmentLabelsFilePathNameStrList = [];

        self.ImageSegmentLabelsDict = {};
        
        self.ImagePixelMappingObjList = [];
        
        self.ImageGraphicsSceneObjList = [];
        
        for CrntImageFileNameStr in self.ImageFileNameStrList:

            ( CrntImageBaseNameStr, CrntImageExtensionStr ) = os.path.splitext( CrntImageFileNameStr );

            self.SelectedImageFilePathNameStrList.append( os.path.join( ImageFilePathStr, CrntImageFileNameStr ) );

            self.SelectedSegmentLabelsFilePathNameStrList.append( os.path.join( SegmentLabelsFilePathStr, ( 'Aud' + CrntImageBaseNameStr + '_allwords.txt' ) ) );

            
            # ADD IMAGE TO LIST OF IMAGES
            self.ImageListWidgetObj.addItem( PySideQtGUI.QListWidgetItem( CrntImageFileNameStr ) );

            
            # CALL METHOD TO PARSE THE INPUTS (LABELS LIST) - see last section where method is defined
            self.ParseSegmentLabels( CrntImageBaseNameStr );

            
            # CREATE THE PIXEL MAPS
            self.ImagePixelMappingObjList.append( PySideQtGUI.QPixmap( self.SelectedImageFilePathNameStrList[-1] ) );

            # CREATE THE GRAPHICS SCENES FOR EACH IMAGE
            self.ImageGraphicsSceneObjList.append( PySideQtGUI.QGraphicsScene() );
            
            self.ImageGraphicsSceneObjList[-1].addPixmap( self.ImagePixelMappingObjList[-1] );
            
            self.ImageGraphicsSceneObjList[-1].setSceneRect( self.ImagePixelMappingObjList[-1].rect() );

        #rof
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # CREATE THE IMAGES LIST ON LEFT SIDE
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ImageListLabelObj = PySideQtGUI.QLabel(
                                                     '<html>' +
                                                     '<h3>Images from:</h3>' +
                                                     '<p>' + self.ImageFilePathStr + '</p>' +
                                                     '</html>'
                                                   );

        
        self.InstructionsLabelObj = PySideQtGUI.QLabel(
                                                        '<html>' +
                                                        '<h2>Instructions:</h2>' +
                                                        '<p>Press <b>s</b> key to start segmenting the image.</p>' +
                                                        '<p>To annotate press the <b>Enter</b> (<b>Return</b>) key to label the annotation.</p>' +
                                                        '<p>Switch images by selecting the file name from the list above.</p>' +
                                                        '<p>Load any existing annotation(s) for the image and enter Viewing Mode by pressing <b>v</b> key.</p>' +
                                                        '<p>When in viewing mode, press the <b>v</b> key to turn off the annotation viewing.</p>' +
                                                        '</html>'
                                                      );

        self.LeftSideWidgetLayoutObj.addWidget( self.ImageListLabelObj );

        self.LeftSideWidgetLayoutObj.addWidget( self.ImageListWidgetObj );

        # self.LeftSideWidgetLayoutObj.addWidget( self.InstructionsLabelObj );

        self.ImageListWidgetObj.setCurrentRow( self.CurrentDisplayImageIndexInt );

        self.ImageListWidgetObj.itemSelectionChanged.connect( self.ChangeSceneObject );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # CREATE THE PIXEL POSITION LABEL
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ImagePixelMouseLabelObject = PySideQtGUI.QLabel( 'Move mouse over the image...' );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        


        # CREATE THE GRAPHICSVIEW (pass the image path and labels list for the current image)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        CurrentImageFileNameStr = self.SelectedImageFilePathNameStrList[ self.CurrentDisplayImageIndexInt ];
       
        CurrentSegmentsStrList = self.ImageSegmentLabelsDict[ os.path.splitext( self.ImageFileNameStrList[ self.CurrentDisplayImageIndexInt ] )[0] ];

        self.ImageCustomizedGraphicsViewObj = SegmentSelectorGraphicsViewWidget.SegmentSelectorGraphicsViewClass(
                                                        MainWindowObj=              self,
                                                        SceneObj=                   self.ImageGraphicsSceneObjList[ self.CurrentDisplayImageIndexInt ],
                                                        RootPathStr=                self.RootPathStr,
                                                        CurrentImageIndexInt=       self.CurrentDisplayImageIndexInt,
                                                        ImageFilesNameStrList=      self.SelectedImageFilePathNameStrList,
                                                        ImageIntList=               self.ImageFileNameStrList,
                                                        ImageSegmentLabelsDict=     self.ImageSegmentLabelsDict
                                                                                                                );

        self.setWindowTitle( ( 'Segmentation Labelling Tool | Labelling Image: ' + os.path.basename( CurrentImageFileNameStr ) ) );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
                

        # CREATE THE PIXEL POSITION LABEL
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ImagePixelMouseLabelObject = PySideQtGUI.QLabel( 'Move mouse over the image...' );
        self.ImagePixelMouseLabelObject.setAlignment( PySideQtCore.Qt.AlignLeft );

        self.ImagePixelSizeLabelObject = PySideQtGUI.QLabel( ( 'Image Size: ' + str( self.ImagePixelMappingObjList[0].size().toTuple() ) ) );
        self.ImagePixelSizeLabelObject.setAlignment( PySideQtCore.Qt.AlignRight );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # SET THE RIGHT-SIDE LAYOUT
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ImageInfoLabelsLayoutObj = PySideQtGUI.QHBoxLayout();
        
        self.ImageInfoLabelsLayoutObj.addWidget( self.ImagePixelMouseLabelObject );
        
        self.ImageInfoLabelsLayoutObj.addWidget( self.ImagePixelSizeLabelObject ); 
        

        self.RghtSideWidgetLayoutObj.addWidget( self.ImageCustomizedGraphicsViewObj );
        
        self.RghtSideWidgetLayoutObj.addLayout( self.ImageInfoLabelsLayoutObj );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # SETUP THE WINDOW (WIDGET) LAYOUT
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.MainLayoutObj = PySideQtGUI.QVBoxLayout();

        
        self.LeftSideWidgetObj.setLayout( self.LeftSideWidgetLayoutObj );
        self.LeftSideWidgetObj.setFixedSize(100,500);
        
        self.RghtSideWidgetObj.setLayout( self.RghtSideWidgetLayoutObj );

        
        self.MainLayoutSplitter.addWidget( self.LeftSideWidgetObj );
        
        self.MainLayoutSplitter.addWidget( self.RghtSideWidgetObj );
        
        
        self.MainLayoutObj.addWidget( self.MainLayoutSplitter );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # SET THE LAYOUT (show the widget) AND TITLE
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.setLayout( self.MainLayoutObj );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # RETURNS NOTHING, THE __new__ METHOD CREATES THE CLASS INSTANCE (THE OBJECT)
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------


    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # METHOD FOR EXTRACTING THE SEGMENT NAMES AND PIXEL VALUES FROM THE LABELS FILE
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def ParseSegmentLabels( self, CurrentImageStr ): 
        '''
            The segment labels file contains a list of all the possible names for the selected segments.
        '''

        # THE LABELS FILE IS A LIST OF ALL THE TOKENS FROM THE NARRATIVES THAT ARE READ IN ONE BY ONE AND APPEND TO A VARIABLE
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        SegmentLabelsFileObject = codecs.open( self.SelectedSegmentLabelsFilePathNameStrList[-1], 'r', 'utf-8' );
        
        SegmentLabelsFileLineStringsList = map( (lambda LineStr: LineStr[ 0 : -1 : 1 ]), SegmentLabelsFileObject.readlines() );

        SegmentLabelsFileObject.close();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        # IMAGE LABEL DICTIONARY
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ImageSegmentLabelsDict[ CurrentImageStr ] = SegmentLabelsFileLineStringsList;
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
       
        # INTERNAL METHOD RETURNS NOTHING
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # SWAP THE SELECTED SCENE OBJECT
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def ChangeSceneObject( self ):
        '''
            This method provides the processes for swapping-out the scene in the QGraphicsView object.
        '''

        # GET THE IMAGE PATH STRING AND THE LIST OF LABELS FOR THIS PARTICULAR IMAGE FROM THE LIST
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        SelectedRowInt = ( self.ImageListWidgetObj.currentRow() );

        NewSceneObj = ( self.ImageGraphicsSceneObjList[ self.ImageListWidgetObj.currentRow() ] );

        self.ImageCustomizedGraphicsViewObj.setScene( NewSceneObj );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # INCREMENT THE CURRENT IMAGE COUNTER
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.CurrentDisplayImageIndexInt = ( self.CurrentDisplayImageIndexInt + 1 );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # UPDATE THE WINDOW TITLE
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        CurrentImageFileNameStr = self.SelectedImageFilePathNameStrList[ SelectedRowInt ];

        CurrentSegmentsStrList = self.ImageSegmentLabelsDict[ os.path.splitext( self.ImageFileNameStrList[ SelectedRowInt ] )[0] ];
        
        self.setWindowTitle( ( 'Segmentation Labelling Tool | Labelling Image: ' + os.path.basename( CurrentImageFileNameStr ) ) );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------


        # RESET THE GRAPHICSVIEW VARIABLES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ImageCustomizedGraphicsViewObj.NumOriginalSceneItemsInt = ( 1 );
        self.ImageCustomizedGraphicsViewObj.ImageSgmtNumber = ( 0 );
        self.ImageCustomizedGraphicsViewObj.ImageSgmtPixelDict = ( [] ); 
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # FORCE REDRAW
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.update();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # NOTHING RETURNED | INTERNAL METHOD
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

#ssalc
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# THIS SECTION WILL ONLY RUN WHEN THIS MODULE IS CALLED DIRECTLY BY THE PYTHON INTERPRETER (COMIPLER)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
if ( __name__ == '__main__' ):

    # WHY WOULD YOU WANT TO CALL THIS MODULE DIRECTLY?!
    pass;

#fi 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
