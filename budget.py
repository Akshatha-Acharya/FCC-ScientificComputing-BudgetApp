class Category:
    ledger = []
    category = ""
    balance = 0.0
    
    def __init__(self,category):
        self.category = category
        self.ledger = []
    
    def deposit(self,amount,desc=""):
        dict = {}
        dict['amount'] = amount
        dict['description'] = desc
        self.ledger.append(dict)
        self.balance += amount
    
    def withdraw(self,amount,desc=""):
        bool = self.check_funds(amount)
        if(bool):
            withdrawamount = float('-' + str(amount))
            self.deposit(withdrawamount,desc)
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self , amount , destCategory):
        desc = "Transfer to " + destCategory.category
        bool = self.withdraw(amount,desc)
        if(bool):
            dest_desc = "Transfer from " + self.category
            destCategory.deposit(amount,dest_desc)
            return True
        return False
    
    def check_funds(self, amount):
        if (self.balance >= amount):
            return True
        return False
    
    def __str__(self): 
        #title string
        title = self.category.center(30, "*") + '\n'
        #content
        content_list = []
        for object in self.ledger:
            decimal_amt = "{:.2f}".format(object['amount'])
            amt = '{:>7}'.format(decimal_amt)+'\n'
            desc = '{:<23}'.format(object['description'][:23])
            content_list.append(desc+amt)
        content = ""
        for line in content_list:
            content += line 
        #total
        total = 'Total: '+str(self.balance)
        return(title + content + total)


def create_spend_chart(categories):
    title = "Percentage spent by category" + '\n'
    
    percentage_list = calculate_percent(categories)
    bars = ''
    for i in range(100,-10,-10):
        line = '{:>3}'.format(str(i)) + '|'
        for j in range(len(percentage_list)):
            if((percentage_list[j] % 10) < 5):
                percentage_list[j] = round(percentage_list[j]/10)*10         
            if(percentage_list[j] >= i):
                line = line + ' o '
            else:
                line = line + ' '*3
        if(i == 0):
            length = len(line)
        bars += line + ' \n'
    
    horizontalline = '-'*(length-3)
    hline = "{0:>{1}}".format(horizontalline, length+1) + '\n'
    
    length_list = []
    for i in range(0,len(categories)):
        length = len(categories[i].category)
        length_list.append(length)

    labels = ''
    for i in range(0,max(length_list)):
        line = " "*4
        for k in range(0,len(categories)):
            if(i<len(categories[k].category)):
                line += ' ' + str(categories[k].category)[i] + ' '
            else:
                line += ' '*3
        labels += line + ' \n'
    labels = labels.rstrip('\n')
    bar_chart = title + bars + hline + labels
    return bar_chart

def calculate_percent(categories):
    percentage_list = []
    total_list = []
    total_spends = 0
    for i in range(len(categories)):
        ledger = categories[i].ledger
        total = 0
        for j in ledger:
            if str(j['amount']).startswith('-'):
                total += float(str(j['amount'])[1:])
        total_list.append(total)
        total_spends += total

    for i in range(len(categories)):
        percent = int((total_list[i] / total_spends) * 100)
        percentage_list.append(percent)

    return percentage_list