import csv

class Excel:
    def __init__(self,fields,rows):
        print("Excel created")
        self.fields = fields
        self.rows = rows
        # name of csv file 
        self.filename = "colors.csv"

    def main(self):   
        # writing to csv file 
        with open(self.filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(self.fields)
            for i in range(0,len(self.rows)-3,3): 
                l = [self.rows[i],self.rows[i+1],self.rows[i+2]]
                # writing the data rows 
                csvwriter.writerow(l)

                l = list()

