import csv

def savetocsv(jobs):
  file=open('vacation.csv',mode='w')
  writer=csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'link'])
  for job in jobs:
    writer.writerow(list(job.values()))
 
  return