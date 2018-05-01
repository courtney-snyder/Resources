# -*- coding: utf-8 -*-
"""
STK and Python Integration
""" 

# Set up your python workspace
from win32api import GetSystemMetrics
from time import sleep
import csv
import datetime
import comtypes
from comtypes.client import CreateObject

# Get reference to running STK instance
uiApplication    = CreateObject("STK11.Application")

uiApplication.Visible=True
uiApplication.UserControl=True

# Get our IAgStkObjectRoot interface
root=uiApplication.Personality2

from comtypes.gen import STKUtil
from comtypes.gen import STKObjects
counter = 0
ping = 0
max_index = 0
time = 0
secondsInDay = 86400
starttime = []
stoptime = []
startlist = []
endlist = []
writer = csv.writer(open("output.csv",'w'))
writer2 = csv.writer(open("longest.csv",'w'))
writer.writerow(['Location','Start Access','Stop Access'])
#remove last 3 miliseconds because datetime can only work with 6

def writeAccessRows(start,stop,name):
    for i in range(len(start)):
        csvrow = [name,start[i],stop[i]]
        writer.writerow(csvrow)
       
def format_time(time):
    
    temp = time[:-3]
    timeo = datetime.datetime.strptime(temp,'%d %b %Y %H:%M:%S.%f')
    timeob = datetime.datetime.strftime(timeo,'%d %b %Y %H:%M:%S.%f')
    return timeob

def to_seconds(time):
    seconds = (time.hour * 60 + time.minute) * 60 + time.second + time.microsecond
    return seconds

def find_longest_access(start,stop,name):
    max = []
    for i in range(len(start)):
        max.append(stop[i]-start[i])
            
    sub_list= max
    sub_list.sort()
    max_index = max.index(sub_list[-1])
    writer2.writerow([name,start[max_index],stop[max_index]])
    return str(sub_list[-1]),max_index 
            
def addAccessStartList(start):
    for i in range(len(start)):
        s = start[i]
        t = format_time(s)
        starttime = datetime.datetime.strptime("27 Apr 2018 00:00:00.000000", '%d %b %Y %H:%M:%S.%f')
        st = datetime.datetime.strptime(t,'%d %b %Y %H:%M:%S.%f')
        seconds = st-starttime
        startlist.append(seconds.total_seconds())

def addAccessEndList(end):
    for i in range(len(end)):
        s = end[i]
        t = format_time(s)
        starttime = datetime.datetime.strptime("27 Apr 2018 00:00:00.000000", '%d %b %Y %H:%M:%S.%f')
        st = datetime.datetime.strptime(t,'%d %b %Y %H:%M:%S.%f')
        seconds = st-starttime
        endlist.append(seconds.total_seconds())
        
def information(target,name):
    
    access = satellite.GetAccessToObject(target)
    access.ComputeAccess()

#Get the Access AER Data Provider
    accessDP         = access.DataProviders.Item('Access Data')
    accessDP2        = accessDP.QueryInterface(STKObjects.IAgDataPrvInterval)
    results          = accessDP2.Exec(scenario2.StartTime, scenario2.StopTime)
    accessStartTimes = results.DataSets.GetDataSetByName('Start Time').GetValues()
    accessStopTimes  = results.DataSets.GetDataSetByName('Stop Time').GetValues()
    appendToStart(accessStartTimes)
    appendToStop(accessStopTimes)
    addAccessStartList(accessStartTimes)
    addAccessEndList(accessStopTimes)
    writeAccessRows(accessStartTimes,accessStopTimes,name)
    
    print(find_longest_access(starttime,stoptime,name)) 
    print(" from " + accessStartTimes[max_index] + " to " + accessStopTimes[max_index] + " at " + name)
    print("\n")
    starttime.clear()
    stoptime.clear()

def appendToStart(start):
    for i in range(len(start)):
        s = start[i]
        t = format_time(s)
        st = datetime.datetime.strptime(t,'%d %b %Y %H:%M:%S.%f')
#        seconds = to_seconds(st)
        starttime.append(st)
    
def appendToStop(stop):
    for i in range(len(stop)):
        s = stop[i]
        t = format_time(s)
        st = datetime.datetime.strptime(t,'%d %b %Y %H:%M:%S.%f')
#        seconds = to_seconds(st)
        stoptime.append(st)
        



####PLACEHOLDER FOR SOLAR PANEL DATA

if __name__ == '__main__':
    print("Enter the orbit pattern for the CougSat1")
    print("1. Circular")
    print("2. Critically Inclined")
    print("3. Critically Inclined, Sun Sync")
    print("4. Geosynchronous")
    print("5. Molniya")
    print("6. Repeating Ground Trace")
    print("7. Repeating Sun Sync")
    print("8. Sun Synchronous")
    orbitPattern = input('')
    
    print("Enter the ground station for the CougSat1")
    print("1. Pullman")
    print("2. Tri-Cities")
    print("3. Everett")
    print("4. Vancouver")
    print("5. Spokane")
    
    groundStation = input('')
    
    root.NewScenario("CougSat")
    scenario = root.CurrentScenario

    scenario2 = scenario.QueryInterface(STKObjects.IAgScenario)
    scenario2.SetTimePeriod('27 Apr 2018 00:00:00.00','+24hr')
    
    root.Rewind();

    satellite= scenario.Children.New(STKObjects.eSatellite, "CougSat")
    
    #placeholder for orbit selection
    
    #placeholder to insert dae file
  
    #### Solar panels will be initialized to start towards the sun
    root.ExecuteCommand('VO */Satellite/CougSat InitializeSolarPanelsToSun Enable Yes')
    
    #### Set weight in kg of the satellite
    
    root.ExecuteCommand('SetMass */Satellite/CougSat Value 1.33')
    
    #### Antennae properties
    #Antenna <AntObjectPath> {Options} <AttributePath> [<Value>] [<Unit>]
    #http://help.agi.com/stk/index.htm#../Subsystems/connectCmds/Content/cmd_Antenna.htm
    
    #### Initialization of Modelling Exposure of Solar panels over an interval or orbit
    #http://help.agi.com/stk/index.htm#../Subsystems/connectCmds/Content/cmd_VOSolarPanel.htm
    
    ####Satellite Temperature parameterss
    #SEET <VehiclePath> VehTemperature {TempOptions}
    #http://help.agi.com/stk/index.htm#../Subsystems/connectCmds/Content/cmd_SEETVehTemperature.htm
    
    #### Propagate
    
    root.ExecuteCommand('SetState */Satellite/CougSat Classical TwoBody "' + scenario2.StartTime + '" "'+ scenario2.StopTime +'" 60 ICRF "'+ scenario2.StartTime + '" 7200000.0 0.0 90 0.0 0.0 0.0')
    if orbitPattern == "1":
        root.ExecuteCommand('OrbitWizard */Satellite/CougSat Circular ModelFile "C:\\Users\\Mitchell\\Documents\\cubesat.dae"')
    if orbitPattern == "2":
        root.ExecuteCommand('OrbitWizard */Satellite/CougSat CriticallyInclined ModelFile "C:\\Users\\Mitchell\\Documents\\cubesat.dae"')
    if orbitPattern == "3":
        root.ExecuteCommand('OrbitWizard */Satellite/CougSat CriticallyInclinedSunSync ModelFile "C:\\Users\\Mitchell\\Documents\\cubesat.dae"')
    if orbitPattern == "4":
        root.ExecuteCommand('OrbitWizard */Satellite/CougSat Geosynchronous ModelFile "C:\\Users\\Mitchell\\Documents\\cubesat.dae"')
    if orbitPattern == "5":
        root.ExecuteCommand('OrbitWizard */Satellite/CougSat Molniya ModelFile "C:\\Users\\Mitchell\\Documents\\cubesat.dae"')
    if orbitPattern == "6":
        root.ExecuteCommand('OrbitWizard */Satellite/CougSat RepeatingGroundTrace ModelFile "C:\\Users\\Mitchell\\Documents\\cubesat.dae"')
    if orbitPattern == "7":
        root.ExecuteCommand('OrbitWizard */Satellite/CougSat RepeatingSunSync ModelFile "C:\\Users\\Mitchell\\Documents\\cubesat.dae"')
    if orbitPattern == "8":
        root.ExecuteCommand('OrbitWizard */Satellite/CougSat SunSynchronous ModelFile "C:\\Users\\Mitchell\\Documents\\cubesat.dae"')
  
    
    if groundStation == "1":
        target           = scenario.Children.New(STKObjects.eFacility,"Pullman")
        targetP          = target.QueryInterface(STKObjects.IAgFacility)
        targetP.Position.AssignGeodetic(46.7319,-117.1542,0)#pullman
        information(target,"Pullman")
        
    if groundStation == "2":
        target2          = scenario.Children.New(STKObjects.eFacility,"Spokane");
        targetS          = target2.QueryInterface(STKObjects.IAgFacility)
        targetS.Position.AssignGeodetic(47.6612,-117.4052,0)#spokane
        information(target2,"Spokane")
        
    if groundStation == "3":    
        target3         = scenario.Children.New(STKObjects.eFacility,"TriCities");
        targetT          = target3.QueryInterface(STKObjects.IAgFacility)
        targetT.Position.AssignGeodetic(46.3313,-119.2638,0)#tri cities
        information(target3,"Tri Cities") 
        
    if groundStation == "4":
        target4          = scenario.Children.New(STKObjects.eFacility,"Everett");
        targetE          = target4.QueryInterface(STKObjects.IAgFacility)
        targetE.Position.AssignGeodetic(48.005,-122.1974,0)#everett
        information(target4,"Everett")
        
    if groundStation == "5":
        target5         = scenario.Children.New(STKObjects.eFacility,"Vancouver");
        targetV          = target5.QueryInterface(STKObjects.IAgFacility)
        targetV.Position.AssignGeodetic(45.7318,-122.6321,0) #vancouver
        information(target5,"Vancouver")
        
    root.ExecuteCommand('Animate * Start End')
    print(startlist)
    print(endlist)
    while(time < secondsInDay):
        if time > endlist[counter] and len(endlist) - 1 > counter:
            counter = counter + 1
        if time > startlist[counter] and time < endlist[counter]:
            ping = 1
            print("You can now ping CougSat")
            print(counter)
        
        sleep(0.001)
        time = time + 1
        ping = 0
    print("end")
    #boolean value to figure out how to make sure that the software is still animating
    
    #while running, wait for command from user
    
    