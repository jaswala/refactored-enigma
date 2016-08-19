#Result2TDR.py sample file
import csv,os,datetime
import dataextract as tde
 
#Step 1: Create the Extract File and open the .csv
try:
    tdefile = tde.Extract('mediacom.tde')
except:
    os.remove('mediacom.tde')
    tdefile = tde.Extract('mediacom.tde')
 
csvReader = csv.reader(open('T3-KPIs.csv','rb'), delimiter=',')
 
#Step 2: Create the tableDef
tableDef = tde.TableDefinition()
tableDef.addColumn('cal_date', tde.Type.DATE)
#tableDef.addColumn('device_type', tde.Type.CHAR_STRING)
#tableDef.addColumn('region', tde.Type.CHAR_STRING)
#tableDef.addColumn('dma', tde.Type.CHAR_STRING)
tableDef.addColumn('visits', tde.Type.INTEGER)
#tableDef.addColumn('bounce_visits', tde.Type.INTEGER)
#tableDef.addColumn('hnd_visits', tde.Type.INTEGER)
#tableDef.addColumn('email_leads_web_sessions', tde.Type.INTEGER)
#tableDef.addColumn('email_leads', tde.Type.INTEGER)
tableDef.addColumn('inventory_searches', tde.Type.INTEGER)
tableDef.addColumn('sales_phone_contacts', tde.Type.INTEGER)
tableDef.addColumn('service_phone_contacts', tde.Type.INTEGER)
tableDef.addColumn('email_contacts', tde.Type.INTEGER)
#tableDef.addColumn('vin_visits', tde.Type.INTEGER)
#tableDef.addColumn('vdp_views', tde.Type.INTEGER)
#tableDef.addColumn('vdp_visits', tde.Type.INTEGER)
#tableDef.addColumn('ctc_sales', tde.Type.INTEGER)
#tableDef.addColumn('ctc_service', tde.Type.INTEGER)
#tableDef.addColumn('phone_calls', tde.Type.INTEGER)
 
#Step 3: Create the table in the image of the tableDef
table = tdefile.addTable('Extract',tableDef)
 
#Step 4: Loop through the csv, grab all the data, put it into rows
#and insert the rows into the table
newrow = tde.Row(tableDef)
csvReader.next() #Skip the first line since it has the headers
for line in csvReader:
    date = datetime.datetime.strptime(line[0], "%Y-%m-%d")
    newrow.setDate(0, date.year, date.month, date.day)
    #newrow.setCharString(1, str(line[1]))
    #newrow.setCharString(2, str(line[2]))
    #newrow.setCharString(3, str(line[3]))
    newrow.setInteger(1,int(line[1]))
    newrow.setInteger(2,int(line[2]))
    newrow.setInteger(3,int(line[3]))
    newrow.setInteger(4,int(line[4]))
    newrow.setInteger(5,int(line[5]))
    newrow.setInteger(6,int(line[6]))
    #newrow.setInteger(18,int(line[18]))
    table.insert(newrow)
 
#Step 5: Close the tde
tdefile.close()