#======================================================== file = noWait.py =====
#= Program to determine no wait staff allocation for MTSS                      =
#===============================================================================
#= Notes:                                                                      =
#=  1) Need Python 3.6 or later installed                                      =
#===============================================================================
#= Execute: Command line as noWait.py                                          =
#===============================================================================
#= Sample execution: (as noWait.py < noWait_input.txt)                         =
#=                                                                             =
#=   =====================================================================     =
#=   ==         Results from no wait model for staff allocation         ==     =
#=   =====================================================================     =
#=   == System parameters (inputs):                                            =
#=   ==   Number of classrooms                             = 50                =
#=   ==   Total number of at risk students                 = 300               =
#=   ==   T2 Lite: Number of students per teacher or aide  = 5                 =
#=   ==   T2 Lite: Probability of responding               = 0.7               =
#=   ==   Evaluation: Number of students per psychologist  = 20                =
#=   ==   T2 Heavy: Number of students per interventionist = 12                =
#=   =====================================================================     =
#=   == Staffing needed for no wait (outputs):                                 =
#=   ==   Number of teacher aides    =  60                                     =
#=   ==   Number of psychologists    =  5                                      =
#=   ==   Number of interventionists =  8                                      =
#=   =====================================================================     =
#=                                                                             =
#= For input file (as noWait_input.txt)                                        =
#=                                                                             =
#=   50       # Number of classrooms                                           =
#=   300      # Total number of at risk students                               =
#=   5        # T2 Lite: Number of students per teacher or aide                =
#=   0.70     # T2 Lite: Probability respond to T2 Lite                        =
#=   20       # Evaluation: Number of students per psychologist                =
#=   12       # T2 Heavy: Number of students per interventionist               =
#=                                                                             =
#===============================================================================
#= Author: Ken Christensen (christen@cse.usf.edu)                              =
#===============================================================================
#= History: KJC (07/05/21) - Genesis from noWaitModel_v2.py                    =
#===============================================================================
import math

# Function to compute staffing for no wait
def computeNoWait(numClassrooms, totalAtRiskStu, numStuPerTeacherOrAide,       \
    probRespond, numStuPerPsychologist, numStuPerInterventionist):

  # Distribute at risk students to classrooms evenly
  numAtRiskStu = [0]*numClassrooms
  for i in range(totalAtRiskStu):
    j = i % numClassrooms
    numAtRiskStu[j] += 1

  # Calculation for number of aides needed beyond capacity of teachers
  numAides = 0
  for i in range(numClassrooms):
    numAides += math.ceil((numAtRiskStu[i]/numStuPerTeacherOrAide) - 1)

  # Calculation for total number ofat risk students after T2 Lite response
  totalAtRiskStu = math.ceil((1.0 - probRespond) * totalAtRiskStu)

  # Calculation for number of psychologists needed
  numPsychologists = math.ceil(totalAtRiskStu / numStuPerPsychologist)

  # Calculation for number of T2 Heavy interventionists needed
  numInterventionists = math.ceil(totalAtRiskStu / numStuPerInterventionist)

  # Return results from calculations
  return(numAides, numPsychologists, numInterventionists)

# *** Run as console application if this is main ***
if (__name__ == "__main__"):

  # Input system parameters (no validity checking)
  inString = input("Number of classrooms: ")
  numClassrooms = int(inString.split()[0])
  inString = input("Total number of at risk students: ")
  totalAtRiskStu = int(inString.split()[0])
  inString = input("T2 Lite: Number of students per teacher or aide: ")
  numStuPerTeacherOrAide = int(inString.split()[0])
  inString = input("T2 Lite: Probability of responding: ")
  probRespond = float(inString.split()[0])
  inString = input("Evaluation: Number of students per psychologist: ")
  numStuPerPsychologist = int(inString.split()[0])
  inString = input("T2 Heavy: Number of students per interventionist: ")
  numStuPerInterventionist = int(inString.split()[0])

  # Call computeNoWait() to calculate staffing needs
  numAides, numPsychologists, numInterventionists =                            \
  computeNoWait(numClassrooms, totalAtRiskStu, numStuPerTeacherOrAide,         \
    probRespond, numStuPerPsychologist, numStuPerInterventionist)

  # Output system parameters and calculated staffing needs
  print()
  print("=====================================================================")
  print("==         Results from no wait model for staff allocation         ==")
  print("=====================================================================")
  print("== System parameters (inputs):")
  print("==   Number of classrooms                             =",
    numClassrooms)
  print("==   Total number of at risk students                 =",
    totalAtRiskStu)
  print("==   T2 Lite: Number of students per teacher or aide  =",
    numStuPerTeacherOrAide)
  print("==   T2 Lite: Probability of responding               =",
    probRespond)
  print("==   Evaluation: Number of students per psychologist  =",
    numStuPerPsychologist)
  print("==   T2 Heavy: Number of students per interventionist =",
    numStuPerInterventionist)
  print("=====================================================================")
  print("== Staffing needed for no wait (outputs):");
  print("==   Number of teacher aides    = ", numAides)
  print("==   Number of psychologists    = ", numPsychologists)
  print("==   Number of interventionists = ", numInterventionists)
  print("=====================================================================")
