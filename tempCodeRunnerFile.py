def dtClick(self):
        #Perform Delaunay Triangulation
        
        #Get input data (points)
        points = ui.Canvas.getPoints()
    
        #Run DT
        a = Algorithms()
        dt= a.delaunayTriangulation(points) 
        
        #Set results (dt)
        ui.Canvas.setDT(dt)
        
        #Repaint
        self.Canvas.repaint()
        
        
    def contourLinesClick(self):
         #Compute contour lines
         
         #Get dt
         dt = ui.Canvas.getDT()
         
         #Calculate contours
         a = Algorithms()
         contour_lines = a.createContourLines(dt, self.zmin, self.zmax, self.dz)
         
         #Set countours to Draw class
         ui.Canvas.setContourLines(contour_lines)
         
         #Repaint canvas
         self.Canvas.repaint()
         
    
    def settingsClick(self):
        #Show settings
        self.dialog.exec()
        
        #Update parameters
        self.zmin = self.ui_dialog.getZmin()
        self.zmax = self.ui_dialog.getZmax()
        self.dz = self.ui_dialog.getdZ()
        
        print(self.zmin)
        
    
    def analyzeSlopeClick(self):
        #Analyze slope
        
        #Get DT
        dt = ui.Canvas.getDT()
        
        #Get triangles
        triangles = ui.Canvas.getTriangles()
        #Analyze slope
        a = Algorithms()
        a.analyzeDTMSlope(dt, triangles)
        
        #Set results
        ui.Canvas.setTriangles(triangles)
        
        #Repaint
        self.Canvas.repaint()
        
    def pointsChanged(self):
        #View/Hide points
        view_points = self.actionPoints.isChecked()
        
        #Set status
        ui.Canvas.setViewPoints(view_points)
        
        #Repaint
        self.Canvas.repaint()
        
        
    def DTChanged(self):
        #View/Hide DT
        view_DT = self.actionDT.isChecked()
        
        #Set status
        ui.Canvas.setViewDT(view_DT)
        
        #Repaint
        self.Canvas.repaint()
        
    def contourLinesChanged(self):
        #View/Hide Contour lines
        view_contour_lines = self.actionContourLines.isChecked()
        
        #Set status
        ui.Canvas.setViewContourLines(view_contour_lines)
        
        #Repaint
        self.Canvas.repaint()
        
        
    def slopeChanged(self):
        #View/Hide slope
        view_slope = self.actionSlope.isChecked()
        
        #Set status
        ui.Canvas.setViewDT(view_slope)
        
        #Repaint
        self.Canvas.repaint()    

    def aspectChanged(self):
        view_aspect = self.actionSlope.isChecked()
        ui.Canvas.view_slope = view_aspect
        self.Canvas.repaint()
        
    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "DTM analysis"))
        self.menuFile.setTitle(_translate("MainForm", "File"))
        self.menuView.setTitle(_translate("MainForm", "View"))
        self.menuAnalysis.setTitle(_translate("MainForm", "Analysis"))
        self.menuClear.setTitle(_translate("MainForm", "Clear"))
        self.menuSettings.setTitle(_translate("MainForm", "Settings"))
        self.toolBar.setWindowTitle(_translate("MainForm", "toolBar"))
        self.actionOpen.setText(_translate("MainForm", "Open"))
        self.actionOpen.setToolTip(_translate("MainForm", "Open file"))
        self.actionExit.setText(_translate("MainForm", "Exit"))
        self.actionExit.setToolTip(_translate("MainForm", "Close application"))
        self.actionPoints.setText(_translate("MainForm", "Points"))
        self.actionDT.setText(_translate("MainForm", "DT"))
        self.actionSlope.setText(_translate("MainForm", "Slope"))
        self.actionAspect.setText(_translate("MainForm", "Aspect"))
        self.actionDTM.setText(_translate("MainForm", "DTM"))
        self.actionDTM.setToolTip(_translate("MainForm", "Create DTM"))
        self.actionContour_lines.setText(_translate("MainForm", "Contour lines"))
        self.actionContour_lines.setToolTip(_translate("MainForm", "Ceate contour lines"))
        self.actionAnalyzeSlope.setText(_translate("MainForm", "Analyze Slope"))
        self.actionAnalyzeSlope.setToolTip(_translate("MainForm", "Analyze DTM Slope"))
        self.actionAnalyzeAspect.setText(_translate("MainForm", "Analyze Aspect"))
        self.actionClear_data.setText(_translate("MainForm", "Clear data"))
        self.actionClear_all.setText(_translate("MainForm", "Clear all"))
        self.actionParameters.setText(_translate("MainForm", "Parameters"))
        self.actionParameters.setToolTip(_translate("MainForm", "Setting parameters"))
        self.actionContourLines.setText(_translate("MainForm", "Contour lines"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec())
