import pandas as pd
import xlsxwriter


class JoinWorksheets():
    
    def __Init__(self):
        pass
    
    def combine_worksheets(self, workbookFile, cellSpacing):
        """ This function combines all the worksheets in an input Excel document into one worksheet with spacing.
            The name of each worksheet is used as a title for the data pasted into the single worksheet.
            
            args:
                workbookFile: Workbook with multiple worksheets to be combined
                cellSpacing: number of cells to leave between each pasted worksheet
        """
        dfDict = pd.read_excel(workbookFile, sheet_name=None)
        writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
        keyList = [k for k, v in dfDict.items()]
        valuesLen = [len(v) for k, v in dfDict.items()]
        
        titleIndex=[]
        firstPasteRow = 1

        dfDict[keyList[0]].to_excel(writer, sheet_name = "combined", index=False, startrow=firstPasteRow+1)
        titleIndex.append(firstPasteRow)
        cntr = 0
        
        for k in range(1, len(keyList)):
            startrow = valuesLen[cntr] +  titleIndex[cntr] + cellSpacing 
            titleIndex.append(startrow)
        
            dfDict[keyList[k]].to_excel(writer, sheet_name = "combined", index=False, startrow = startrow+1)
            cntr += 1

        worksheet = writer.sheets['combined']
        sheetIndex = dict(zip(keyList, titleIndex))

        #paste the sheet names
        for sheetName, row in sheetIndex.items():
            worksheet.write(row-1, 0, sheetName)

        writer.save()