from datetime import date
from datetime import timedelta

global today
global d1
global RangeDates
global jsonurl
global csvurl
global localjsonfile
global localcsvfile
global localaggregateddata
global localpivotdata
global OutputFile

global GraphTitle, WatermarkTitle, WatermarkSubtitle, ExtraAnnotations
global PaperColour
global PlotbgColour
global PrimaryColour
global FamilyFont
global lines, leftx, centerx, rightx, topy, middley, bottomy, OutsidePlotRight, OutsidePlotUp, OutsidePlotDown

###############
#Datetime variables
###############
yesterday = date.today()-timedelta(days = 1)
d0 = yesterday.strftime("%d-%m-%Y")
today = date.today()
d1 = today.strftime("%d-%m-%Y")
RangeDates = 150

###############
#Data
###############
#from https://data.rivm.nl/covid-19/
jsonurl= 'https://data.rivm.nl/covid-19/COVID-19_aantallen_gemeente_per_dag.json'
csvurl= 'https://lcps.nu/wp-content/uploads/covid-19.csv'
localjsonfile='RIVM_data.json'
localcsvfile='lcps.csv'
localaggregateddata='covid_aggregated.csv'
localpivotdata='covid_pivot.csv'
OutputFile="COVID"


###############
##Layout
###############
GraphTitle= "COVID-19 cases in the Netherlands<br><i>Source: RIVM, LCPS. Updated on " + d1 + "</i>"
WatermarkTitle = "Graph by Henk Leerssen"
WatermarkSubtitle = "Weekly and monthly data<br>are moving averages"
PrimaryColour = "#041C3E"
PaperColour= "#E3EDFD"
PlotbgColour= "#FFFFFF"
FamilyFont = "Open Sans, Helvetica"
ExtraAnnotations = "Drag to zoom in<br>Doubleclick to zoom out"

# vertical lines to add, specified by x-position
lines = {'Intelligent lockdown':'2020-03-23','Eastern':'2020-04-12', 'Lessen restrictions, commercial testing':'2020-06-01',
         'Curfew at midnight for hospitality':'2020-09-18', 'Mouthmasks obligatory':'2020-12-01','Closing of hospitality sector':'2020-10-15',
         'First vaccins':'2021-01-06', 'Curfew at 21:00':'2021-01-23'}
leftx = 0.01
centerx =0.44
rightx =0.93
topy =0.99
middley = 0.44
bottomy = 0.005
OutsidePlotRight = 1.02
OutsidePlotUp = 1.05
OutsidePlotDown = -0.04