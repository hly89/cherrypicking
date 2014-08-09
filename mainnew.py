from PyQt4 import QtGui, QtCore
import sys
from cherry import Ui_mainform
from LineEdit import LineEdit
import numpy as np
import pandas as pd
import globalvar
from itertools import chain
import string

class cherryView(QtGui.QMainWindow, Ui_mainform):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        control_list = ['Positive', 'Negative']
        gene_list = ['ARK5_5', 'ARK5_6', 'ARK5_7', 'ZAK_6']
        self.addcomb(1, 2, control_list)  # index starts from 0!
        self.addLineEdit(1, 3, gene_list)
        # hiden the table view
        # self.tableView.hide()
        self.tabWidget.removeTab(1)
        self.tabWidget.hide()

		
		# save the data from sourcePlate
        #sp1 = []
        #self.model.setHeaderData(ID, Qt.Horizontal, QVariant("ID"))
        #self.model.select()

        #signal with slot
        self.Plate.cellChanged.connect(self.cell_changed)
        self.upload.clicked.connect(self.loadFile)
        self.sourcePlate.clicked.connect(self.loadSourcePlate)
        self.sourcePlate_2.clicked.connect(self.loadSourcePlate2)
        self.picking.clicked.connect(self.cherrypicking)
        self.save.clicked.connect(self.savepair)
        self.Type_choice.activated['QString'].connect(self.type)
        #self.tableview.dataChanged.connect(self.pair_changed)

    def loadSourcePlate(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        inputFile = open(fileName)
        #inputData = inputFile.readlines()
        inputData = inputFile.read().splitlines()
        inputFile.close()
        inputHeader = inputData[0]
        Header = [ header for header in inputHeader.split('\t') ]
        #print(len(Header))
        #for head in inputHeader
        inputData = inputData[1:]
        sp1 = []
        #sp1 = pd.DataFrame(inputData)
        for item in inputData:
			row = [ string for string in item.split('\t') ]
			#print(row)
			sp1.append(row)
        sp1 = pd.DataFrame(sp1, columns=Header)
        sp1['Well'] = sp1.Row+sp1.Col
        #print(sp1.head())
        globalvar.sp1 = sp1
        self.upload.setEnabled(True)
		
    def loadSourcePlate2(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        inputFile = open(fileName)
        #inputData = inputFile.readlines()
        inputData = inputFile.read().splitlines()
        inputFile.close()
        inputHeader = inputData[0]
        Header = [ header for header in inputHeader.split('\t') ]
        #print(len(Header))
        #for head in inputHeader
        inputData = inputData[1:]
        sp1 = []
        #sp1 = pd.DataFrame(inputData)
        for item in inputData:
            row = [ string for string in item.split('\t') ]
            sp1.append(row)
        sp1 = pd.DataFrame(sp1, columns=Header)
        #sp1['Well'] = sp1.Row+sp1.Col
        #print(sp1.head())
        globalvar.sp2 = sp1
        self.upload.setEnabled(True)


    # to use auto complete, change table cell to line edit
    def addLineEdit(self, row, col, items):
        edit = QtGui.QLineEdit()
        lineEdit = LineEdit(edit)
        model = QtGui.QStandardItemModel()
        for i, word in enumerate(items):
            item = QtGui.QStandardItem(word)
            model.setItem(i, 0, item)
        lineEdit.setModel(model)
        lineEdit.setModelColumn(0)
        self.Plate.setCellWidget(row, col, lineEdit)

    # add combox for specific cell in the table
    def addcomb(self, row, col, items):
        comb = QtGui.QComboBox()
        comb.addItems(items)
        self.Plate.setCellWidget(row, col, comb)
    def tabs(self, name):
        self.tab2 = QtGui.QWidget()
        #self.tab3.setObjectName(name)
        #self.platetab3 = QtGui.QTableWidget(self.tab3)
        self.tabWidget.addTab(self.tab2, name)
        self.platetab2 = QtGui.QTableWidget(self.tab2)
        self.platetab2.setEnabled(True)
        self.platetab2.setGeometry(QtCore.QRect(0, 0, 1091, 471))
        self.platetab2.setCornerButtonEnabled(True)
        self.platetab2.setRowCount(16)
        self.platetab2.setColumnCount(24)
        self.platetab2.setObjectName("platetab2")
        self.platetab2.setColumnCount(24)
        self.platetab2.setRowCount(16)
        item = QtGui.QTableWidgetItem("A")
        self.platetab2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem("B")
        self.platetab2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem("C")
        self.platetab2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem("D")
        self.platetab2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem("E")
        self.platetab2.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem("F")
        self.platetab2.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem("G")
        self.platetab2.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem("H")
        self.platetab2.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem("I")
        self.platetab2.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem("J")
        self.platetab2.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem("K")
        self.platetab2.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem("L")
        self.platetab2.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem("M")
        self.platetab2.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem("N")
        self.platetab2.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem("O")
        self.platetab2.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem("P")
        self.platetab2.setVerticalHeaderItem(15, item)
        self.platetab2.horizontalHeader().setVisible(True)
        self.platetab2.horizontalHeader().setCascadingSectionResizes(True)
        self.platetab2.horizontalHeader().setDefaultSectionSize(80)
        self.platetab2.horizontalHeader().setMinimumSectionSize(30)
        self.platetab2.verticalHeader().setDefaultSectionSize(30)
        return self.platetab2

    def loadFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        inputFile = open(fileName)
        inputData = inputFile.read().splitlines()
        inputFile.close()

		
        self.model = QtGui.QStandardItemModel(self)
        self.tableview.setModel(self.model)
        self.model.dataChanged.connect(self.pair_changed)
        inputHeader = inputData[0]
        Header = [ header for header in inputHeader.split('\t') ]
        if(globalvar.type=="gene"):
            print("gene")
        else:
            if(set(Header).issubset(set(['Index', 'Drug1', 'Drug2', 'Range1', 'Range2', 'Destination Plate Barcode']))==False):
                QtGui.QMessageBox.warning(self, 'Error', 'The input format is not correct. Please check the input file or chose the correct experiment type!', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                return
        self.tabWidget.show()
        #for head in inputHeader
        sp = []
        inputData = inputData[1:]
        for item in inputData:
            rowItem = [
                QtGui.QStandardItem(string)
                for string in item.split()
            ]
            #print(rowItem)
            # for string in item.split():
            #cell = QtGui.QStandardItem(string)
            self.model.appendRow(rowItem)
        for item in inputData:
			row = [ string for string in item.split('\t') ]
			#print(row)
			sp.append(row)
        sp = pd.DataFrame(sp, columns=Header)

        # self.model.setHeaderData(inputHeader)
        header = inputHeader.split()
        for i, j in enumerate(header):
			#print j
			self.model.setHeaderData(i, QtCore.Qt.Horizontal, QtCore.QVariant(j))
        
        #self.platetab2.horizontalHeader().setVisible(True)
        
        self.Plate.hide()
        globalvar.pairlist = sp
        flag = True
        if(globalvar.type=="gene"):
            self.show_plate_rna(sp)
            #self.picking.setEnabled(True)
        else:
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), "Drug Pair")
            #self.show_plate_drug(sp)
            # check if all drugs in the source plate
            drug1 = sp['Drug1']
            drug2 = sp['Drug2']
            drug = set(chain(drug1, drug2))
            #drug = pd.DataFrame(drug)
            #match_res = drug.isin(globalvar.sp2['Supplier Ref'])
            #print(match_res)
            for each_drug in drug:
                #print(each_drug)
                match_res = globalvar.sp2[globalvar.sp2['Supplier Ref']== each_drug].index
                if(len(match_res)==0):
                    QtGui.QMessageBox.warning(self, 'Error', 'Drug '+each_drug+' cannot be found in the source plate!', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    flag = False
                    break
            if(flag):
                self.show_plate_drug(sp)
        if(flag):
            self.picking.setEnabled(True)

        
		
		
    def show_plate_rna(self, sp):
        # get the plate info
        plate_id = set(globalvar.pairlist['plate'])
		# sort the plate id
        plate_id = sorted(plate_id)
        #print(plate_id)
        # designed plate info
        row_dp = range(2,14)
        col_dp = range(2,22)

			
        plate_list = {}
        for i, item in enumerate(plate_id):
			
			plate_list[i] = self.tabs("Plate"+str(i+1))
			globalvar.platetab_idx.append(self.tabWidget.currentIndex()+1)
        for i, item in enumerate(plate_id):
			# subset of the plate info
			#plate_info = sp.query('plate'=='1')
			plate_info = sp.loc[(sp.plate == item), :]
			#print(plate_info)
			for row in plate_info.index:
					rna1 = plate_info.at[row, 'rna1']
					rna2 = plate_info.at[row, 'rna2']
			# get the index info
					index_plate = plate_info.at[row, 'index']
					index_plate = int(index_plate)-1
			# devide the plate into three rows and five columns so in total 15 4*4 array
			# which row
					if(index_plate/5==0):
						rindex = row_dp[0:4]
					elif(index_plate/5==1):
						rindex = row_dp[4:8]
					else:
						rindex = row_dp[8:13]
			# which column
					if(index_plate%5==0):
						columns = col_dp[0:4]
					elif(index_plate%5==1):
						columns = col_dp[4:8]
					elif(index_plate%5==2):
						columns = col_dp[8:12]
					elif(index_plate%5==3):
						columns = col_dp[12:16]
					else:
						columns = col_dp[16:20]
						
					for rid, rowid in enumerate(rindex):
						for cid, colid in enumerate(columns):
							if(rid==0 and cid!=0):
								sirna = QtGui.QLineEdit()
								sirna.setText(rna1)
								#print(cid)
								plate_list[i].setCellWidget(rowid, colid, sirna)
							elif(rid!=0 and cid==0):
								sirna = QtGui.QLineEdit()
								sirna.setText(rna2)
								plate_list[i].setCellWidget(rowid, colid, sirna)
							elif(rid!=0 and cid!=0):
								sirna = QtGui.QLineEdit()
								sirna.setText(rna1+";"+rna2)
								plate_list[i].setCellWidget(rowid, colid, sirna)
							#else:
								#sirna = QtGui.QLineEdit()
								#sirna.setText("control")
								#self.platetab2.setCellWidget(rowid, colid, sirna)
			
			
			# positive control
			row_pctr = [1,1,1,2,2,6,6,6,10,10,12,12,14,14,14,14]
			col_pctr = [2,11,21,6,14,2,10,18,6,14,1,22,6,10,14,18]
			# add color the control position 
			for idx_ctr, ctr in enumerate(row_pctr):
				plate_list[i].setItem(ctr, col_pctr[idx_ctr], QtGui.QTableWidgetItem())
				plate_list[i].item(ctr, col_pctr[idx_ctr]).setBackground(QtGui.QColor(0,0,0))
        
			# negative control
			row_pctr = [1,1,1,1,1,2,2,2,5,5,6,6,8,8,10,10,10,14,14,14,14,14]
			col_pctr = [4,8,12,16,20,2,10,18,1,22,6,14,1,22,2,10,18,4,8,12,16,20]
			for idx_ctr, ctr in enumerate(row_pctr):
				plate_list[i].setItem(ctr, col_pctr[idx_ctr], QtGui.QTableWidgetItem())
				plate_list[i].item(ctr, col_pctr[idx_ctr]).setBackground(QtGui.QColor(128,128,128))
				
				
    def show_plate_drug(self, sp):
        # get the plate info
        plate_id = set(globalvar.pairlist['Destination Plate Barcode'])
		# sort the plate id
        #plate_id = sorted(plate_id)
        #print(plate_id)
        # designed plate info
        row_dp = range(0,17)
        col_dp = range(0,24)
			
        plate_list = {}
        for i, item in enumerate(plate_id):
			
			plate_list[i] = self.tabs("Plate"+str(i+1))
			globalvar.platetab_idx.append(self.tabWidget.currentIndex()+1)
        for i, item in enumerate(plate_id):
			# subset of the plate info
			#plate_info = sp.query('plate'=='1')
			plate_info = sp.loc[(sp['Destination Plate Barcode'] == item), :]
			#print(plate_info)
			for row in plate_info.index:
				drug1 = plate_info.at[row, 'Drug1']
				drug1_sp = globalvar.sp2[globalvar.sp2['Supplier Ref']==drug1]
				drug1_name = ''.join(set(drug1_sp['Name']))
				#print(drug1_name)
				drug2 = plate_info.at[row, 'Drug2']
				drug2_sp = globalvar.sp2[globalvar.sp2['Supplier Ref']==drug2]
				drug2_name = ''.join(set(drug2_sp['Name']))
				# get the index info
				index_plate = plate_info.at[row, 'Index']
				index_plate = int(index_plate)
				#index_plate = int(index_plate)-1
				# devide the plate into three rows and five columns so in total 15 4*4 array
				# which row
				if(index_plate%2==0):
					# row 2
					rindex = row_dp[8:16]
				else:
					# row 1
					rindex = row_dp[0:8]
				# which column
				if(index_plate==1 or index_plate==2):
					vol_col = col_dp[0:8]
				elif(index_plate==3 or index_plate==4):
					vol_col = col_dp[8:16]
				else:
					vol_col = col_dp[16:24]
				# color the cells for drug1
				drug1_range = plate_info.at[row, 'Range1']
				if(drug1_range=='H'):
					col_tmp = vol_col[0]
					vol_col.pop(0)
					for col_id in vol_col:
						if(col_id==1 or col_id==9 or col_id==17):
							plate_list[i].setItem(rindex[0], col_id, QtGui.QTableWidgetItem(drug1_name))
							plate_list[i].item(rindex[0], col_id).setBackground(QtGui.QColor(255, 105, 180))
						else:
							plate_list[i].setItem(rindex[0], col_id, QtGui.QTableWidgetItem())
							plate_list[i].item(rindex[0], col_id).setBackground(QtGui.QColor(255, 105, 180))
				else:
					col_tmp = vol_col[0]
					vol_col.pop(0)
					for col_id in vol_col:
						if(col_id==1 or col_id==9 or col_id==17):
							plate_list[i].setItem(rindex[0], col_id, QtGui.QTableWidgetItem(drug1_name))
							plate_list[i].item(rindex[0], col_id).setBackground(QtGui.QColor(0, 250, 154))
						else:
							plate_list[i].setItem(rindex[0], col_id, QtGui.QTableWidgetItem())
							plate_list[i].item(rindex[0], col_id).setBackground(QtGui.QColor(0, 250, 154))
				# color the cells for drug2
				drug2_range = plate_info.at[row, 'Range2']
				if(drug2_range=='H'):
					#row_tmp = rindex
					rindex.pop(0)
					for row_id in rindex:
						if(row_id==1 or row_id==9):
							plate_list[i].setItem(row_id, col_tmp, QtGui.QTableWidgetItem(drug2_name))
						else:
							plate_list[i].setItem(row_id, col_tmp, QtGui.QTableWidgetItem())
						plate_list[i].item(row_id, col_tmp).setBackground(QtGui.QColor(255, 105, 180))
				else:
					#row_tmp = rindex
					rindex.pop(0)
					for row_id in rindex:
						if(row_id==1 or row_id==9):
							plate_list[i].setItem(row_id, col_tmp, QtGui.QTableWidgetItem(drug2_name))
						else:
							plate_list[i].setItem(row_id, col_tmp, QtGui.QTableWidgetItem())
						plate_list[i].item(row_id, col_tmp).setBackground(QtGui.QColor(0, 250, 154))
				# positive control
				row_pctr = [0,0,0,8,8,8]
				col_pctr = [0,8,16,0,8,16]
				# add color the control position 
				for idx_ctr, ctr in enumerate(row_pctr):
					plate_list[i].setItem(ctr, col_pctr[idx_ctr], QtGui.QTableWidgetItem())
					plate_list[i].item(ctr, col_pctr[idx_ctr]).setBackground(QtGui.QColor(119, 136, 153))
        
				# negative control
				row_pctr = [7,7,7,15,15,15]
				col_pctr = [7,15,23,7,15,23]
				for idx_ctr, ctr in enumerate(row_pctr):
					plate_list[i].setItem(ctr, col_pctr[idx_ctr], QtGui.QTableWidgetItem())
					plate_list[i].item(ctr, col_pctr[idx_ctr]).setBackground(QtGui.QColor(255, 20, 147))
    def cell_changed(self):
        cur_col = self.Plate.currentColumn()
        cur_row = self.Plate.currentRow()
        cur_text = self.Plate.currentItem().text()
        tableItem = QtGui.QLineEdit()
        tableItem.setText(str(cur_text))
        self.Plate.setCellWidget(1, 7, tableItem)
	
	# Choosing the type of the experiments, gene or drug combo
    def type(self, items):
		# set the type to be the one chosen  by users
		globalvar.type = items
		
		
		
		
    def pair_changed(self):
        #cur_col = self.tableview.currentColumn()
        #cur_row = self.tableview.currentRow()
		data = []
		for row in range(self.model.rowCount()):
			data.append([])
			for column in range(self.model.columnCount()):
				index = self.model.index(row, column)
				#print(str(self.model.data(index).toString()))
				data[row].append(str(self.model.data(index).toString()))
		data = pd.DataFrame(data)
		globalvar.pairlist = data
		globalvar.pairlist_change = True
		for item in globalvar.platetab_idx:
			print(item)
			self.tabWidget.removeTab(item)
		
		
    def savepair(self):
		pair = globalvar.pairlist
		pair.columns = ["rna1", "rna2", "cell.line", "plate", "index", "type"]
		outputFile = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'TXT(*.txt)')
		#print(outputFile)
		pair.to_csv(outputFile, sep='\t', header=True, index=False)

	# the main part of cherry picking
    def cherrypicking(self):
		if(globalvar.type=="gene"):
			self.rna()
		else:
			self.drugcombo()
		
    def rna(self):
		# get the unique sRNA name
		rna1 = set(globalvar.pairlist['rna1'])
		rna2 = set(globalvar.pairlist['rna2'])
		rna1 = set(chain(rna1, rna2))
		rnatypes = np.zeros(shape=(len(rna1),5))
		rnatypes = pd.DataFrame(rnatypes)
		sourcewell = rnatypes
		sourcewell = pd.DataFrame(sourcewell)
		for i, item in enumerate(rna1):
			#print(type(item))
			gene_symbol = list(globalvar.sp1.iloc[:,6])
			gene_symbol2 = list(globalvar.sp2.iloc[:,6])
			if(item in gene_symbol):
				# get the index for gene_symbol==item
				idx = [j for j, x in enumerate(gene_symbol) if x==item]
				rnatypes.iloc[i, 1:4] = list(globalvar.sp1.iloc[idx, 11])
				# save the plate ID
				rnatypes.iloc[i, 4] = globalvar.sp1.iloc[1, 0]
				sourcewell.iloc[i, 4] = globalvar.sp1.iloc[1, 0]
				sourcewell.iloc[i, 1:4] = list(globalvar.sp1.iloc[idx, 12])
			elif(item in gene_symbol2):
				idx = [j for j, x in enumerate(gene_symbol2) if x==item]
				#print(idx)
				rnatypes.iloc[i, 1:4] = list(globalvar.sp2.iloc[idx, 11])
				# save the plate ID
				rnatypes.iloc[i, 4] = globalvar.sp2.iloc[1, 0]
				sourcewell.iloc[i, 4] = globalvar.sp2.iloc[1, 0]
				sourcewell.iloc[i, 1:4] = list(globalvar.sp2.iloc[idx, 12])
		rnatypes.iloc[:, 0] = list(rna1)
		sourcewell.iloc[:, 0] = list(rna1)
		rnatypes.columns = ['name', 'siRNA1', 'siRNA2', 'siRNA3', 'sourceplate']
		sourcewell.columns = ['name', 'w1', 'w2', 'w3', 'sourceplate']
		#print(sourcewell)
		cell_line = globalvar.pairlist['cell.line']
		cline_num = set(cell_line)
		# designed plate info
		row_dp = map(chr, range(65, 91))[2:14]
		col_dp = range(3,23)

		# the echo file
		echo = []
		# transfer volumn info
		vol = [[80]*4]*4 
		vol = pd.DataFrame(vol)
		vol.iloc[0,:] = 160
		vol.iloc[:,0] = 160
		for cline in cline_num:
			subset_cl = globalvar.pairlist[globalvar.pairlist['cell.line']== cline]
	# get the plate info
			plate_sub = subset_cl['plate']
			plate = set(plate_sub)
	#print(plate)
			for each_plate in plate:
		#idx = [j for j, x in enumerate(plate_sub) if x==each_plate]
		#subset_plate = subset_cl.iloc[idx, : ]
				subset_plate = subset_cl[subset_cl['plate']==each_plate]
				for row in subset_plate.index:
					rna1 = subset_plate.at[row, 'rna1']
			# index for the sourcewell and rnatypes
			#idx_sourcewell1 = [ii for ii, xx in enumerate(sourcewell['name']) if xx== rna1]
					sourcewell1 = sourcewell[sourcewell['name']==rna1]
					rnatype1 = rnatypes[rnatypes['name']==rna1]
					rna2 = subset_plate.at[row, 'rna2']
					sourcewell2 = sourcewell[sourcewell['name']==rna2]
					rnatype2 = rnatypes[rnatypes['name']==rna2]
			# get the index info
					index_plate = subset_plate.at[row, 'index']
					index_plate = int(index_plate)-1
			# devide the plate into three rows and five columns so in total 15 4*4 array
			# which row
					if(index_plate/5==0):
						vol.index = row_dp[0:4]
					elif(index_plate/5==1):
						vol.index = row_dp[4:8]
					else:
						vol.index = row_dp[8:13]
				
			# which column
					if(index_plate%5==0):
						vol.columns = col_dp[0:4]
					elif(index_plate%5==1):
						vol.columns = col_dp[4:8]
					elif(index_plate%5==2):
						vol.columns = col_dp[8:12]
					elif(index_plate%5==3):
						vol.columns = col_dp[12:16]
					else:
						vol.columns = col_dp[16:20]
				
			# for the first siRNA
					vol1 = vol.iloc[:,1:4]
					for row_idx in range(0,4):
						for col_idx in range(0,3):
							echo_row = []
					# rna name
							echo_row.append(rna1)
					# rna type
							echo_row.append(rnatype1.iloc[0, col_idx+1])
					# rna source well
							echo_row.append(sourcewell1.iloc[0, col_idx+1])
					# rna source plate id
							echo_row.append(sourcewell1.iloc[0, 4])
					# rna vol
							echo_row.append(vol1.iloc[row_idx, col_idx])
					# destination well
							echo_row.append(vol1.index[row_idx]+str(vol1.columns[col_idx]))
							# plate index
							echo_row.append('MDA231_'+str(each_plate)+'_siRNAcombo')
							echo.append(echo_row)
			
			# for the second siRNA
					vol2 = (vol.iloc[1:4, :]).transpose()
			
					for row_idx in range(0,4):
						for col_idx in range(0,3):
							echo_row = []
					# rna name
							echo_row.append(rna2)
					# rna type
							echo_row.append(rnatype2.iloc[0, col_idx+1])
					# rna source well
							echo_row.append(sourcewell2.iloc[0, col_idx+1])
					# rna source plate id
							echo_row.append(sourcewell2.iloc[0, 4])
					# rna vol
							echo_row.append(vol2.iloc[row_idx, col_idx])
					# destination well
							echo_row.append(str(vol2.columns[col_idx])+str(vol2.index[row_idx]))
							# plate index
							echo_row.append('MDA231_'+str(each_plate)+'_siRNAcombo')
							echo.append(echo_row)
			#vol.index = row_name
			#vol.columns = col_name
			

		echo = pd.DataFrame(echo)
		
		dest_barcode = ['MDA231_1_siRNAcombo', 'MDA231_2_siRNAcombo', 'MDA231_3_siRNAcombo']
# add controls: 22 negative ctrs and 16 positive ctrs
		Ndest_well = ["B5", "B9", "B13", "B17", "B21", "C3", "C11", "C19", "F2", "F23", "G7", "G15", "I2", "I23", "K3", "K11", "K19", "O5", "O9", "O13", "O17", "O21"]
		Pdest_well = ["B3", "B12", "B22", "C7", "C15", "G3", "G11", "G19", "K7", "K15", "M2", "M23", "O7", "O11", "O15", "O19"]
		Ncontrol = pd.DataFrame( {'RNA': ['NegCtr']*22*3, 'RNAtype': ['CTR']*22*3, 'source_well': ['F3']*22*3,'Source_Plate_Barcode': ['ctr']*22*3, 'Transfer Volume': [40]*22*3,'Destination Well': Ndest_well*3, 'Destination Plate Barcode': dest_barcode*22})
		Pcontrol = pd.DataFrame( {'RNA': ['PosCtr']*16*3, 'RNAtype': ['CTR']*16*3, 'source_well': ['C3']*16*3,'Source_Plate_Barcode': ['ctr']*16*3, 'Transfer Volume': [40]*16*3,'Destination Well': Pdest_well*3, 'Destination Plate Barcode': dest_barcode*16})
		control = pd.concat([Ncontrol, Pcontrol], ignore_index=True)
		echo.columns = ['RNA', 'RNAtype', 'source_well', 'Source_Plate_Barcode', 'Transfer Volume', 'Destination Well', 'Destination Plate Barcode']
		echo = pd.concat([echo, control], ignore_index=True)
		echo['Source_Plate_Type'] = '384PP_AQ_BP2'

#writer = pd.ExcelWriter('output.xlsx')
#echo.to_excel(writer, 'Sheet1')
		outputFile = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')
		#print(outputFile)
		echo.to_csv(outputFile, sep=',', header=True, index=False)
		#print(echo)
#writer.save()
		
    def drugcombo(self):
		dst_dilution = [['D', 'C', 'B', 'B', 'B', 'A', 'A'], ['D', 'D', 'D', 'C', 'B', 'B', 'B']]
		# the transfer volume for different dilutions
		transfer_v = [[25, 7.5, 2.5, 7.5, 25, 7.5, 25], [2.5, 7.5, 25, 7.5, 2.5, 7.5, 25]]
		# designed plate info
		row_dp = map(chr, range(63, 91))[2:18]
		col_dp = range(1,25)
		# the echo file
		echo = []
		# generating echo file
		# get the plate info
		plate_sub = globalvar.pairlist['Destination Plate Barcode']
		#Solvent = globalvar.sp2['Solvent'][0]
		plate = set(plate_sub)
		#plate = sorted(plate)
		for each_plate in plate:
			subset_plate = globalvar.pairlist[globalvar.pairlist['Destination Plate Barcode']==each_plate]
			for row in subset_plate.index:
				# side A of the plate
				drug1 = subset_plate.at[row, 'Drug1']
				drug2 = subset_plate.at[row, 'Drug2']
				# get the index info
				index_plate = subset_plate.at[row, 'Index']
				index_plate = int(index_plate)
				# which row
				if(index_plate%2==0):
					# row 2
					vol_index = row_dp[8:16]
				else:
					# row 1
					vol_index = row_dp[0:8]

				# which column
				if(index_plate==1 or index_plate==2):
					vol_col = col_dp[0:8]
				elif(index_plate==3 or index_plate==4):
					vol_col = col_dp[8:16]
				else:
					vol_col = col_dp[16:24]
            
				# for the first drug 8*7 
				# find the range of the first drug 
				range_info = subset_plate.at[row, 'Range1']
				if(range_info=='H'):
					#drug1_conc = dst_conc[0]
					drug1_dilution = dst_dilution[0]
					drug1_transfer = transfer_v[0]
				else:
					#drug1_conc = dst_conc[1]
					drug1_dilution = dst_dilution[1]
					drug1_transfer = transfer_v[1]
        
				for row_idx in range(0,8):
					dilution_id = 0
					for col_idx in range(1,8):
						
						if(row_idx!=7 or col_idx!=7):
							echo_row = []
							drug_sp = globalvar.sp2[globalvar.sp2['Supplier Ref']==drug1]
							drug_id = int(drug_sp[drug_sp['Dilution']==drug1_dilution[dilution_id]].index)
							# drug1 name
							echo_row.append(drug1)
							# drug1 source well
							echo_row.append(drug_sp.at[drug_id, 'SrcWell'])
							# drug1 source well Row
							echo_row.append(drug_sp.at[drug_id, 'Srow'])
							# drug1 source well Column
							echo_row.append(drug_sp.at[drug_id, 'Scol'])
							# drug1 source plate id
							echo_row.append(drug_sp.at[drug_id, 'Source Plate'])
							# drug1 transfer volume
							echo_row.append(drug1_transfer[col_idx-1])
							# destination well
							echo_row.append(vol_index[row_idx]+str(vol_col[col_idx]))
							# destination well row
							echo_row.append(vol_index[row_idx])
							# destination well column
							echo_row.append(str(vol_col[col_idx]))
							# destination plate id
							echo_row.append(subset_plate.at[row, 'Destination Plate Barcode'])
							# add the source plate type
							if(drug_sp.at[drug_id, 'Solvent']=='DMSO'):
								echo_row.append("384PP_DMSO2")
							else:
								echo_row.append("384PP_AQ_BP2")
							echo.append(echo_row)
						dilution_id = dilution_id+1
        
				# for the second drug 7*8 
				# find the range of the second drug 
				range_info = subset_plate.at[row, 'Range2']
				if(range_info=='H'):
					drug2_dilution = dst_dilution[0]
					drug2_transfer = transfer_v[0]
				else:
					drug2_dilution = dst_dilution[1]
					drug2_transfer = transfer_v[1]
        
				for row_idx in range(0,8):
					dilution_id = 0
					for col_idx in range(1,8):
						if(row_idx!=7 or col_idx!=7):
							echo_row = []
							drug_sp = globalvar.sp2[globalvar.sp2['Supplier Ref']==drug2]
							drug_id = int(drug_sp[drug_sp['Dilution']==drug2_dilution[dilution_id]].index)
							# drug2 name
							echo_row.append(drug2)
							# drug2 source well
							echo_row.append(drug_sp.at[drug_id, 'SrcWell'])
							# drug2 source well Row
							echo_row.append(drug_sp.at[drug_id, 'Srow'])
							# drug2 source well Column
							echo_row.append(drug_sp.at[drug_id, 'Scol'])
							# drug2 source plate id
							echo_row.append(drug_sp.at[drug_id, 'Source Plate'])
							# drug1 transfer volume
							echo_row.append(drug2_transfer[col_idx-1])
							# destination well
							echo_row.append(vol_index[col_idx]+str(vol_col[row_idx]))
							# destination well row
							echo_row.append(vol_index[col_idx])
							# destination well column
							echo_row.append(str(vol_col[row_idx]))
							# destination plate id
							echo_row.append(subset_plate.at[row, 'Destination Plate Barcode'])
							# add the source plate type
							if(drug_sp.at[drug_id, 'Solvent']=='DMSO'):
								echo_row.append("384PP_DMSO2")
							else:
								echo_row.append("384PP_AQ_BP2")
							echo.append(echo_row)
						dilution_id = dilution_id+1
			# add negative ctr
			dw = ['A1', 'A9', 'A17', 'I1', 'I9', 'I17']
			dw_r = ['A', 'A', 'A', 'I', 'I', 'I']
			dw_c = ['1', '9', '17', '1', '9', '17']
			drug_sp = globalvar.sp2[globalvar.sp2['Supplier Ref']=='dmso']
			neg_idx = drug_sp.index
			len_neg = len(drug_sp['SrcWell'])
			len_dw = len(dw)
			if(len_neg>=len_dw):
				id_ctr = range(0, len_neg)
			else:
				id_ctr = range(0, len_neg)*6
			for neg_id, each_neg in enumerate(dw):
				echo_row = []
				ctr_idx = neg_idx[id_ctr[neg_id]]
				# drug2 name
				echo_row.append('dmso')
				# drug2 source well
				echo_row.append(drug_sp.at[ctr_idx, 'SrcWell'])
				# drug2 source well Row
				echo_row.append(drug_sp.at[ctr_idx, 'Srow'])
				# drug2 source well Column
				echo_row.append(drug_sp.at[ctr_idx, 'Scol'])
				# drug2 source plate id
				echo_row.append(drug_sp.at[ctr_idx, 'Source Plate'])
				# drug1 transfer volume
				echo_row.append(50)
				# destination well
				echo_row.append(each_neg)
				# destination well row
				echo_row.append(dw_r[neg_id])
				# destination well column
				echo_row.append(dw_c[neg_id])
				# destination plate id
				echo_row.append(each_plate)
				# add the source plate type
				if(drug_sp.at[ctr_idx, 'Solvent']=='DMSO'):
					echo_row.append("384PP_DMSO2")
				else:
					echo_row.append("384PP_AQ_BP2")
				echo.append(echo_row)

			# add positive ctr
			dw = ['H8', 'H16', 'H24', 'P8', 'P16', 'P24']
			dw_r = ['H', 'H', 'H', 'P', 'P', 'P']
			dw_c = ['8', '16', '24', '8', '16', '24']
			drug_sp = globalvar.sp2[globalvar.sp2['Supplier Ref']=='BzCl']
			neg_idx = drug_sp.index
			len_neg = len(drug_sp['SrcWell'])
			len_dw = len(dw)
			if(len_neg>=len_dw):
				id_ctr = range(0, len_neg)
			else:
				id_ctr = range(0, len_neg)*6
			for neg_id, each_neg in enumerate(dw):
				echo_row = []
				ctr_idx = neg_idx[id_ctr[neg_id]]
				# drug2 name
				echo_row.append('BzCl')
				# drug2 source well
				echo_row.append(drug_sp.at[ctr_idx, 'SrcWell'])
				# drug2 source well Row
				echo_row.append(drug_sp.at[ctr_idx, 'Srow'])
				# drug2 source well Column
				echo_row.append(drug_sp.at[ctr_idx, 'Scol'])
				# drug2 source plate id
				echo_row.append(drug_sp.at[ctr_idx, 'Source Plate'])
				# drug1 transfer volume
				echo_row.append(25)
				# destination well
				echo_row.append(each_neg)
				# destination well row
				echo_row.append(dw_r[neg_id])
				# destination well column
				echo_row.append(dw_c[neg_id])
				# destination plate id
				echo_row.append(each_plate)
				if(drug_sp.at[ctr_idx, 'Solvent']=='DMSO'):
					echo_row.append("384PP_DMSO2")
				else:
					echo_row.append("384PP_AQ_BP2")
				echo.append(echo_row)
		echo = pd.DataFrame(echo)
		echo.columns = ['Drug', 'Source Well', 'SRow', 'SCol', 'Source Plate Barcode', 'Transfer Volume', 'Destination Well', 'DRow', 'DCol', 'Destination Plate Barcode', 'Source Plate Barcode']
		outputFile = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')
		echo.to_csv(outputFile, sep=',', header=True, index=False)



# def main(self):
#self.show()

app = QtGui.QApplication(sys.argv)
window = cherryView(None)
window.show()
app.exec_()

