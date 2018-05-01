#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Preethi Vaidyanathan
# px1621@rit.edu
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
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------



# POP-UP WINDOW CLASS WITH A DROP-DOWN LIST FOR ASSIGN LABELS TO PIXELS
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
class CheckboxSelectPopUpClass( PySideQtGUI.QWidget ):
    

    # CLASS INTERNAL GLOBAL VARIABLES --- (OVERRIDDEN) CLASS INITIALIZATION METHOD
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__( self, GraphicsViewObj, RootPathStr, ImageFilePathNameString, LabelsStringsList, SegmentPixelsList, AppTimeString, parent= None ):

        # INITIALIZE THE BASE CLASS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        PySideQtGUI.QWidget.__init__( self, parent );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------


        # PARSE THE INPUTS | ATTACH THEM TO THE CLASS TO BE USED BY THE OTHER METHODS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.GraphicsViewObj = ( GraphicsViewObj );

        self.RootPathStr = ( RootPathStr );
        
        self.ImageFilePathNameString = ( ImageFilePathNameString );
        
        self.LabelsStringsList = ( LabelsStringsList );

        self.SegmentPixelsList = ( SegmentPixelsList );
        
        self.AppTimeString = ( AppTimeString );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------

        
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------------------------------------------------------------------


        # CREATE THE BUTTON GROUP AND THEN INSERT CHECKBOX BUTTONS INTO THE BUTTON GROUP
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.CheckboxButtonGroup = PySideQtGUI.QButtonGroup();
        
        self.CheckboxButtonsLayoutObject = PySideQtGUI.QGridLayout();

        self.CheckboxButtonsList = [];

        RowCount = ( 0 );
        ColCount = ( 0 );
        # sorting to present the labels in alphabetic order
        self.LabelsStringsList.sort();

        for CurrentLabelString in self.LabelsStringsList:
        
            self.CheckboxButtonsList.append( PySideQtGUI.QCheckBox( CurrentLabelString ) );
        
            self.CheckboxButtonGroup.addButton( self.CheckboxButtonsList[-1] );
        
            self.CheckboxButtonsLayoutObject.addWidget( self.CheckboxButtonsList[-1], RowCount, ColCount );

            RowCount += ( 1 );

            if ( RowCount == 18 ):

                ColCount += ( 1 );
                RowCount = ( 0 );

            #fi
        
        #rof

        self.CheckboxButtonGroup.setExclusive( False );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------


        # CREATE THE OK BUTTON
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.OKPushButtonObject = PySideQtGUI.QPushButton( 'Select' );
       
        self.OKPushButtonObject.clicked.connect( self.StoreSelection );                
        # ------------------------------------------------------------------------------------------------------------------------------------------------------


        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # SETUP THE WIDGET LAYOUT
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.MainLayoutObject = PySideQtGUI.QVBoxLayout();        
        
        self.SelectionTitleObj = PySideQtGUI.QLabel( '<html><b>Detailed Segment Labels</b></html>' );
        self.SelectionTitleObj.setAlignment( PySideQtCore.Qt.AlignCenter );

        self.MainLayoutObject.addWidget( self.SelectionTitleObj );
        
        self.MainLayoutObject.addLayout( self.CheckboxButtonsLayoutObject );
        
        self.MainLayoutObject.addWidget( self.OKPushButtonObject );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        # SET THE LAYOUT AND TITLE
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.setLayout( self.MainLayoutObject );
        
        self.setWindowTitle( 'Select Labels for Segment...' );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------


        # RETURNS NOTHING, THE __new__ METHOD CREATES THE CLASS INSTANCE (THE OBJECT)
        return ( None );
    #fed


    # (OVERRIDDEN) WIDGET LEAVING METHOD | CALLED WHEN MOUSE HAS JUST LEFT THE AREA OF THE WIDGET
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def StoreSelection( self ):
        '''
            This is a custom method to connect to the \'Select\' button whenever it is clicked.
        '''

        # CREATE AN EMPTY STRING THEN FILL IT WITH THE COMMA SEPARATED NAMES OF THE BUTTONS THAT ARE CURRENTLY SELECTED
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.SelectedSegmentLabelsString = ( '' );

        for CurrentButtonObject in self.CheckboxButtonGroup.buttons():

            if ( CurrentButtonObject.isChecked() ):
                
                if not ( self.SelectedSegmentLabelsString == '' ):

                    self.SelectedSegmentLabelsString += ( ',' );

                #fi

                self.SelectedSegmentLabelsString += ( CurrentButtonObject.text() );

            #fi

        #rof
        # ------------------------------------------------------------------------------------------------------------------------------------------------------


        # CREATE/APPEND AN OUTPUT FILE WITH LATEST CLICK DATA (POSITION, SEGMENT NAME, AND LIST OF DETAILED LABELS)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        ( ImageFilePathString, ImageFileNameString ) = os.path.split( self.ImageFilePathNameString );

        ( ImageFileBaseNameStr, ImageFileExtStr ) = os.path.splitext( ImageFileNameString );

        NewFileNameStr = ( ImageFileBaseNameStr + '_' + self.AppTimeString + '.txt' );

        # self.SavePath = os.path.join(self.RootPathStr,'AtlantaReferenceAlignments');
        # self.SavePath = os.path.join(self.RootPathStr,'CDIReferenceAlignments');
        self.SavePath = os.path.join(self.RootPathStr,'SnagReferenceAlignments');
        # ImageLabellingDataFilePathNameString = os.path.join( self.SavePath, 'Cara_Original', NewFileNameStr );
         ImageLabellingDataFilePathNameString = os.path.join( self.SavePath, 'Original', NewFileNameStr );
        # ImageLabellingDataFilePathNameString = os.path.join( self.SavePath, 'P_Demog', NewFileNameStr );
        # ImageLabellingDataFilePathNameString = os.path.join( self.SavePath, 'P_Possible', NewFileNameStr );


        self.ImageLabellingDataFileObject = codecs.open( ImageLabellingDataFilePathNameString, 'a', 'utf-8' );
        
        # self.ImageLabellingDataFileObject.write( ImageFilePathString + '\n' );
        # self.ImageLabellingDataFileObject.write( ImageFileNameString + '\n' );

        self.ImageLabellingDataFileObject.write( self.SelectedSegmentLabelsString + '\n' );
        
        for VertexTpl in self.SegmentPixelsList:

            self.ImageLabellingDataFileObject.write( str( VertexTpl ) + '\n' );

        #rof

        self.ImageLabellingDataFileObject.write( '\n' );        

        self.ImageLabellingDataFileObject.close();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------

        
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.LabelAnnotationCentroid();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        # CLOSE THE POP-UP
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.close();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # RETURN NOTHING | THIS IS AN INTERNAL METHOD
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # (OVERRIDDEN) WIDGET LEAVING METHOD | CALLED WHEN MOUSE HAS JUST LEFT THE AREA OF THE WIDGET
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def LabelAnnotationCentroid( self ):
        '''
            
        '''

        # FIND CENTER OF REGION AND PLACE LABELS AS A STRING
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        ( XPixelsLst, YPixelsLst ) = zip( *self.SegmentPixelsList );

        XCenterFlt = ( sum( XPixelsLst ) / float( len( XPixelsLst ) ) );
        YCenterFlt = ( sum( YPixelsLst ) / float( len( YPixelsLst ) ) );

        LabelItemObj = PySideQtGUI.QGraphicsTextItem();

        LabelItemObj.setDefaultTextColor( PySideQtCore.Qt.black );
        LabelItemObj.setFont( PySideQtGUI.QFont( 'Source Code Pro', 10 ) );
        LabelItemObj.setPlainText( self.SelectedSegmentLabelsString );
        LabelItemObj.setPos( XCenterFlt, YCenterFlt );

        ( self.GraphicsViewObj.scene() ).addItem( LabelItemObj );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # RETURN NOTHING | THIS IS AN INTERNAL METHOD
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
