import matplotlib.pyplot as plt
import pandas as pd
from abc import ABC, abstractmethod

class Analysis(ABC):
    @abstractmethod
    def performAnalysis(self):
        pass

class BranchAnalysis(Analysis):
    def performAnalysis(self):
        df = pd.read_csv(r'C:\APDP_DEMO\Food_City.csv')
        year = int(input("Enter Year | "))
        month = int(input("Enter Month | "))
        print("REGISTRATIONS SUMMARY BY BRANCH FOR THE MONTH", month, "OF YEAR", year)
        filtered_df = df.loc[(df['Year'] == year) & (df['Month'] == month)]
        result = filtered_df.groupby('Branch')['Quantity'].sum().reset_index()
        print("MONTHLY REGISTRATIONS SUMMARY")
        print(result)
        plt.bar(result['Branch'], result['Quantity'], width=0.6, color=['pink', 'lightblue', 'purple'])
        plt.xlabel("Branches")
        plt.ylabel("Registrations")
        plt.title("Registration Analysis By Branch")
        plt.show()

class PriceAnalysis(Analysis):
    def performAnalysis(self):
        df = pd.read_csv(r'C:\APDP_DEMO\Food_City.csv')
        products = input("Enter Product name | ")
        filtered_df = df.loc[(df['Products'] == products)]
        x = filtered_df["Day"]
        y = filtered_df["Price"]
        print(filtered_df)
        plt.plot(x, y, marker='o')
        plt.xlabel("Day")
        plt.ylabel("Price")
        title = "Price Analysis of " + products
        plt.title(title)
        plt.show()

class WeeklyAnalysis(Analysis):
    def performAnalysis(self):
        # load data file into panda frame
        df = pd.read_csv(r'C:\APDP_DEMO\Food_City.csv')
        #input Year
        year = int(input("Enter Year | "))
        #input Month
        month = int(input("Enter Month | "))
        # input first day of the week 
        day1 = int(input("Enter starting days of the week | "))
        # filter data for 7 days starting from input day
        day2 = day1 + 6
        filtered_df = df.loc[(df['Day'] >= day1) & (df['Day'] <= day2) & (df['Year'] == year) & (df['Month'] == month)]
        # add up enroll quantities for each branch
        result = filtered_df.groupby('Branch')['Quantity'].sum().reset_index()
        # display summary result in tabular form
        print("Sales SUMMARY")
        print(result)
        # draw bar chart - branches for X axis , quantities for Y axis
        plt.bar(result['Branch'], result['Quantity'], width=0.6, color=['orange', 'lightgreen', 'blue'])
        plt.xlabel("Branches")
        plt.ylabel("Sales")
        plt.title("Weekly Sales Analysis By Branch")
        plt.show()

class PreferenceAnalysis(Analysis):
    def performAnalysis(self):
        df = pd.read_csv(r'C:\APDP_DEMO\Food_City.csv')
        result = df.groupby('Products')['Quantity'].sum().reset_index()
        print(result)
        print("Product Preference Analysis")
        plt.bar(result['Products'], result['Quantity'], width=0.6, color=['pink', 'green', 'purple'])
        plt.xlabel("Products")
        plt.ylabel("Registrations")
        plt.title("Preference Analysis")
        plt.show()

class DistributionAnalysis(Analysis):
    def performAnalysis(self):
        df = pd.read_csv(r'C:\APDP_DEMO\Food_City.csv')
        result = df.groupby('Branch').sum().reset_index()
        print(result)
        plt.pie(result["Quantity"], labels=result["Branch"], autopct='%1.1f%%')
        plt.title("Distribution Analysis By Branch")
        plt.show()

class ProcessStrategy:
    def executeStrategy(self, analysis_object):
        analysis_object.performAnalysis()

class StrategySelector:
    def openMenu(self):
        while True:
            print("Sampath Food City (PVT) Ltd - Registrations Analysis")
            print("1 - Analysis By Branch")
            print("2 - Price Analysis of Products")
            print("3 - Weekly Analysis of Supermarket Network")
            print("4 - Product Preference Analysis")
            print("5 - Distribution Analysis")
            print("6 - Exit")
            choice = int(input("Enter Choice [1|2|3|4|5|6] | "))
            if choice < 1 or choice > 6:
                print("Invalid Choice")
            else:
                ps = ProcessStrategy()
                if choice == 1:
                    ba_object = BranchAnalysis()
                    ps.executeStrategy(ba_object)
                elif choice == 2:
                    wa_object = PriceAnalysis()
                    ps.executeStrategy(wa_object)
                elif choice == 3:
                    pa_object = WeeklyAnalysis()
                    ps.executeStrategy(pa_object)
                elif choice == 4:
                    pf_object = PreferenceAnalysis()
                    ps.executeStrategy(pf_object)
                elif choice == 5:
                    da_object = DistributionAnalysis()
                    ps.executeStrategy(da_object)
                elif choice == 6:
                    break
        print("******** END *********")

class Admin:
    count = 0
    def __init__(self, username, password):
        if Admin.count == 0:
            self.username = username
            self.password = password
            Admin.count += 1
        else:
            print("Admin already exists")

    def logon(self):
        print("Sampath Food City (PVT) Ltd - Data Analysis System")
        print("-----------------------------------------------------")
        un = input("Enter User Name | ")
        pw = input("Enter Password | ")
        if un == self.username and pw == self.password:
            s1 = StrategySelector()
            s1.openMenu()
        else:
            print("Incorrect User Name OR Password")

# main
a1 = Admin("Admin", "123")
a1.logon()

