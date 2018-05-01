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
from . import CheckboxSelectPopUpWidget;
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# CUSTOMIZED QGraphicsView CLASS WITH OVERRIDDEN MOUSE-OVER METHODS FOR PIXEL LABELLING
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
class SegmentSelectorGraphicsViewClass( PySideQtGUI.QGraphicsView ):
    
    # INTERNAL CLASS (OBJECT) GLOBAL VARIABLES
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    SGMNT_MODE = ( False );

    VIEW_MODE = ( False );

    NumOriginalSceneItemsInt = ( 1 );
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
        

    # CLASS INITIALIZATION METHOD
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__( self, MainWindowObj, SceneObj, RootPathStr, CurrentImageIndexInt, ImageFilesNameStrList, ImageIntList, ImageSegmentLabelsDict, parent= None ):
        
        # INITIALIZE THE BASE CLASS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        PySideQtGUI.QGraphicsView.__init__( self, parent );
        
        self.setMouseTracking( True );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #PARSE THE INPUTS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.MainWindowObj = ( MainWindowObj );

        self.RootPathStr = ( RootPathStr );

        self.CurrentImageIndexInt = CurrentImageIndexInt;
        
        self.ImageFilesNameStrList = ImageFilesNameStrList;
        
        self.ImageIntList = ImageIntList;
        
        self.ImageSegmentLabelsDict = ImageSegmentLabelsDict;

        self.setScene( SceneObj );
        
        self.setAlignment( PySideQtCore.Qt.AlignCenter );
        
        self.setRenderHints( PySideQtGUI.QPainter.Antialiasing |
                             PySideQtGUI.QPainter.TextAntialiasing |
                             PySideQtGUI.QPainter.SmoothPixmapTransform );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        # CREATE A TIME STRING FOR WHEN THIS INSTANCE WAS CREATED | USED TO LABEL SEPARATE INSTANCES OF RESULTS FILES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.AppTimeString = ( time.strftime( '%Y-%m-%d_%H-%M-%S_%Z', time.localtime( time.time() ) ) );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        # SETUP THE ANNOTATION PEN COLORS/STYLES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.SgmntPolygonQPenObj = PySideQtGUI.QPen(
                                                     PySideQtCore.Qt.green,
                                                     2,
                                                     PySideQtCore.Qt.SolidLine,
                                                     PySideQtCore.Qt.RoundCap,
                                                     PySideQtCore.Qt.RoundJoin
                                                   );

        self.SgmntNextPointQPenObj = PySideQtGUI.QPen(
                                                       PySideQtGUI.QColor( 0, 0, 255, 128 ),
                                                       1,
                                                       PySideQtCore.Qt.SolidLine,
                                                       PySideQtCore.Qt.RoundCap,
                                                       PySideQtCore.Qt.RoundJoin
                                                     );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # SETUP THE MOUSE CURSOR
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.CrosshairMouseCursorObject = PySideQtGUI.QCursor();
        self.CrosshairMouseCursorObject.setShape( PySideQtCore.Qt.CrossCursor );
        
        self.NormalMouseCursorObject = PySideQtGUI.QCursor();
        self.NormalMouseCursorObject.setShape( PySideQtCore.Qt.ArrowCursor );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------

        # DICTIONARY FOR CAPTURING CURRENT SEGMENT (NUMBERED INCREMENTALLY) AS KEYWORDS AND THE PIXELS OF THE BOUNDARY AS THE VALUES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.ImageSgmtNumber = 0;
        self.ImageSgmtPixelDict = []; 
        # ------------------------------------------------------------------------------------------------------------------------------------------------------


        # RETURN NOTHING | THE IMPLICIT self.__new__() METHOD WILL BE CALLED TO CREATE THE CLASS INSTANCE (THE OBJECT) AFTER THIS METHOD RETURNS
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # (OVERRIDDEN) WIDGET ENTERING METHOD | CALLED WHEN MOUSE HAS JUST ENTERED THE AREA OF THE WIDGET
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def keyPressEvent( self, NewKeyPressEventObj ):
        '''
            This is an overridden method for modifying the widget behaviour whenever the mouse enters into the screen area of the widget. Here when mouse enters the 
            screen area and the key s is pressed the segmentation mode is toggled. The mouse cursor changes from North-West Arrow symbol to a Crosshair or vice-versa 
            indicating whether segmentation is enabled or not.
        '''
        
        # KEYPRESS EVENTS
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        if ( NewKeyPressEventObj.key() == PySideQtCore.Qt.Key_S ):
            '''
                Assigning the vertices for the annotation region.
            '''
                        
            # TOGGLE SEGMENTATION MODE WHENEVER "S" IS PRESSED
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            self.CurrentSgmtPixelList = []; 
        
            self.SGMNT_MODE = not( self.SGMNT_MODE ); 
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            

            # CHANGE THE MOUSE CURSOR
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            if ( self.SGMNT_MODE ):
            
                # SEGMENTATION ENABLED
                self.setCursor( self.CrosshairMouseCursorObject );

            else:

                # SEGMENTATION DISABLED
                self.setCursor( self.NormalMouseCursorObject );

            #fi
            # --------------------------------------------------------------------------------------------------------------------------------------------------    

        elif ( (NewKeyPressEventObj.key() == PySideQtCore.Qt.Key_Enter) or (NewKeyPressEventObj.key() == PySideQtCore.Qt.Key_Return) ):
            '''
                Labelling the annotation region.
            '''
            
            # DISABLE THE SEGMENTATION MODE
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            self.SGMNT_MODE = ( False );
            
            self.setCursor( self.NormalMouseCursorObject );
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            

            # 
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            self.CurrentSgmtPixelList.append( self.CurrentImagePixelPosIntTuple );
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            
            
            # CHANGE THE RUBBER-BAND LINE COLORS 
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            self.scene().items()[0].setPen( self.SgmntPolygonQPenObj );
            self.scene().items()[1].setPen( self.SgmntPolygonQPenObj );

            self.NumOriginalSceneItemsInt += ( 3 );
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            

            # 
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            SelectedRowInt = ( self.MainWindowObj.ImageListWidgetObj.currentRow() );
            

            self.ImageFilePathNameString = ( self.ImageFilesNameStrList[ SelectedRowInt ] );
            
            self.ImageSegmentLabelsList = ( self.ImageSegmentLabelsDict[ str( SelectedRowInt + 1 ) ] );
            
            self.CurrentLabelPopUpObject = CheckboxSelectPopUpWidget.CheckboxSelectPopUpClass(
                                                                                               GraphicsViewObj=           self,
                                                                                               RootPathStr=               self.RootPathStr,
                                                                                               ImageFilePathNameString=   self.ImageFilePathNameString,
                                                                                               LabelsStringsList=         self.ImageSegmentLabelsList,
                                                                                               SegmentPixelsList=         self.CurrentSgmtPixelList,
                                                                                               AppTimeString=             self.AppTimeString
                                                                                             );
                
            self.CurrentLabelPopUpObject.show();
            self.CurrentLabelPopUpObject.raise_();
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            
        elif ( NewKeyPressEventObj.key() == PySideQtCore.Qt.Key_V ):
            '''
                Load the vertex data and show the annotation.
            '''
            
            # TOGGLE SEGMENTATION VIEWING MODE
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            self.VIEW_MODE = not ( self.VIEW_MODE );
            
            self.setCursor( self.NormalMouseCursorObject );
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            

            # IF IN THE VIEW MODE | LOAD THE VERTEX DATA AND DRAW THE ANNOTATION/SEGMENTATION POLYGON
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            if ( self.VIEW_MODE ):
                
                self.LoadVertexData();

            #fi
            # --------------------------------------------------------------------------------------------------------------------------------------------------

        elif ( ( NewKeyPressEventObj.key() == PySideQtCore.Qt.Key_Delete ) or ( NewKeyPressEventObj.key() == PySideQtCore.Qt.Key_Backspace ) ):
            '''
                Delete the most recent annotation region vertex.
            '''
            
            # DELETE THE LAST ADDED POLYGON POINT FROM THE LIST
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            self.DeleteLastPolygonPoint();
            # --------------------------------------------------------------------------------------------------------------------------------------------------
            
        #fi

        # RETURN NOTHING | THIS IS AN INTERNAL METHOD
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # (OVERRIDDEN) WIDGET SEGMENT METHOD | CALLED WHEN MOUSE HAS ENTERED THE AREA OF THE WIDGET AND KEY S HAS BEEN PRESSED TO ENABLE SEGMENTATION
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def mouseMoveEvent( self, NewMouseMoveEventObject ):
        '''
            This is an overridden method for modifying the widget behaviour whenever the mouse leaves the screen area of the widget.
            Whenever the mouse enters the screen and key s is pressed the segmentation mode is turned on and every movement of the mouse is captured in a file. 
        '''

        # GET THE NEW MOUSE LOCATION
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.CurrentImagePixelPosIntTuple = ( self.mapToScene( NewMouseMoveEventObject.pos() ).toTuple() );
        
        self.CurrentImagePixelPosIntTupleStr = str( self.CurrentImagePixelPosIntTuple );
        
        self.CurrentImagePixelPosQPoint = self.TupleToQPointF( self.CurrentImagePixelPosIntTuple );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        # UPDATE THE MAIN WINDOW'S TEXT LABELS FOR SHOWING THE MOUSE POSITION
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.MainWindowObj.ImagePixelMouseLabelObject.setText( 'Mouse at: ' + self.CurrentImagePixelPosIntTupleStr );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # IF IN SEGEMENTATION MODE | REMOVE PREVIOUS LINES AND DRAW NEW CONNECTING LINES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        if ( self.SGMNT_MODE ):
            
            if ( len( self.CurrentSgmtPixelList ) > 0 ):

                if ( len( self.scene().items() ) == ( self.NumOriginalSceneItemsInt + 2 ) ):
                
                    self.scene().removeItem( self.scene().items()[0] );
                    self.scene().removeItem( self.scene().items()[0] );

                #fi

                NextPointBegSideLineObj = PySideQtCore.QLineF(
                                                               self.TupleToQPointF( self.CurrentSgmtPixelList[0] ),
                                                               self.CurrentImagePixelPosQPoint
                                                             );

                NextPointEndSideLineObj = PySideQtCore.QLineF(
                                                               self.TupleToQPointF( self.CurrentSgmtPixelList[-1] ),
                                                               self.CurrentImagePixelPosQPoint
                                                             );

                ( self.scene() ).addLine( NextPointBegSideLineObj, self.SgmntNextPointQPenObj );
                ( self.scene() ).addLine( NextPointEndSideLineObj, self.SgmntNextPointQPenObj );

            #fi

        #fi
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # UPDATE THE GUI TO DISPLAY THE CHANGES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.update();
        PySideQtCore.QCoreApplication.processEvents();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # RETURN NOTHING | THIS IS AN INTERNAL METHOD
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------


    # (OVERRIDDEN) WIDGET SEGMENT METHOD | CALLED WHEN MOUSE HAS ENTERED THE AREA OF THE WIDGET AND KEY S HAS BEEN PRESSED TO ENABLE SEGMENTATION
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def mousePressEvent( self, NewMousePressEventObject ):
        '''
            This is an overridden method for modifying the widget behaviour whenever the mouse is moving. 
        '''

        # GET THE NEW MOUSE LOCATION
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.CurrentImagePixelPosIntTuple = ( self.mapToScene( NewMousePressEventObject.pos() ).toTuple() );
        
        self.CurrentImagePixelPosQPoint = self.TupleToQPointF( self.CurrentImagePixelPosIntTuple );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        
        # IF IN SEGEMENTATION MODE | STORE THE NEW POLYGON VERTEX
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        if ( self.SGMNT_MODE ):
            
            self.CurrentSgmtPixelList.append( self.CurrentImagePixelPosIntTuple );

            if ( len( self.CurrentSgmtPixelList ) > 1 ):

                if ( len( self.scene().items() ) == ( self.NumOriginalSceneItemsInt + 2 ) ):
                
                    self.scene().removeItem( self.scene().items()[0] );
                    self.scene().removeItem( self.scene().items()[0] );

                #fi

                NewPolygonSideLineObj = PySideQtCore.QLineF(
                                                             self.TupleToQPointF( self.CurrentSgmtPixelList[-2] ),
                                                             self.TupleToQPointF( self.CurrentSgmtPixelList[-1] )
                                                           );

                ( self.scene() ).addLine( NewPolygonSideLineObj, self.SgmntPolygonQPenObj );

                self.NumOriginalSceneItemsInt += ( 1 );

            #fi

        #fi
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # UPDATE THE GUI TO DISPLAY THE CHANGES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.update();
        PySideQtCore.QCoreApplication.processEvents();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # RETURN NOTHING | THIS IS AN INTERNAL METHOD
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------


    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    # DATA EDIT METHOD | DELETE SEGEMENTATION POLYGON VERTEX FROM LIST OF VERTICES
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def DeleteLastPolygonPoint( self ):
        '''
            A customized method for deleting the last polygon vertex from the list of vertices for the segmentation.
        '''

        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        if ( self.SGMNT_MODE ):
            
            if ( len( self.CurrentSgmtPixelList ) > 1 ):

                if ( len( self.scene().items() ) == ( self.NumOriginalSceneItemsInt + 2 ) ):
                
                    self.scene().removeItem( self.scene().items()[0] );
                    self.scene().removeItem( self.scene().items()[0] );

                #fi

                self.scene().removeItem( self.scene().items()[0] );

                self.NumOriginalSceneItemsInt -= ( 1 );
                
                LastPointValueTuple = self.CurrentSgmtPixelList.pop( -1 );

            #fi

        #fi
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # UPDATE THE GUI TO DISPLAY THE CHANGES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        self.update();
        PySideQtCore.QCoreApplication.processEvents();
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # RETURN NOTHING | THIS IS AN INTERNAL METHOD
        return ( None );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # DATA EDIT METHOD | DELETE SEGEMENTATION POLYGON VERTEX FROM LIST OF VERTICES
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def TupleToQPointF( self, InputPointTuple ):
        '''
            A helper method.
        '''

        # CREATE A QPointF OBJECT FROM A TUPLE OF TWO VALUES (x,y) FOR A POINT IN AN IMAGE
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        OutputQPointObj = PySideQtCore.QPointF( InputPointTuple[0], InputPointTuple[1] );
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # RETURN THE POINT AS QPointF OBJECT
        return ( OutputQPointObj );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # LOAD DATA METHOD | LOAD THE ANNOTATION POLYGON VERTICES FROM THE TEXT FILE AND CREATE LINES FOR THE POLYGON
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def LoadVertexData( self ):
        '''
            A helper method.
        '''

        # LOAD THE DATA INTO A LIST OF TUPLES
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        SgmntPolygonTupleList = []; # code goes here...
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # CREATE A QPointF OBJECT FROM A TUPLE OF TWO VALUES (x,y) FOR A POINT IN AN IMAGE
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        for ( PrevPointTuple, CrntPointTuple ) in ( SgmntPolygonTupleList[ 0 : -1 : 1 ], SgmntPolygonTupleList[ 1 : : 1 ] ):

            NewPolygonSideLineObj = PySideQtCore.QLineF(
                                                         self.TupleToQPointF( PrevPointTuple ),
                                                         self.TupleToQPointF( CrntPointTuple )
                                                       );

            ( self.scene() ).addLine( NewPolygonSideLineObj, self.SgmntPolygonQPenObj );

            self.NumOriginalSceneItemsInt += ( 1 );

        #rof
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        

        # RETURN THE POINT AS QPointF OBJECT
        return ( OutputQPointObj );
    #fed
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
#ssalc
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# THIS SECTION WILL ONLY RUN WHEN THIS MODULE IS CALLED DIRECTLY BY THE PYTHON INTERPRETER (COMIPLER)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
if ( __name__ == '__main__' ):

    # WHY WOULD YOU WANT TO CALL THIS MODULE DIRECTLY?!
    pass;

#fi 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
