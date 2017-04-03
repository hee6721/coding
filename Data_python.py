import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

def main() :
    
    df = pd.read_csv('Data.csv', delimiter=",")
    df['Period'] = pd.to_datetime(df['Period'])

    fig = plt.figure()

    ax1 = fig.add_subplot(211)
    ax1.yaxis.grid()
    max_y_ax1 = df['Actual'].max()  + 55
    ax1.set_ylim([0,max_y_ax1 ])

    ax1_1 = ax1.twinx()
    max_y_ax1_1 = df['Target'].max()  + 50 
    ax1_1.set_ylim([0,max_y_ax1_1 ])

    ax1.bar(df['Period'].values, df['Actual'], color='gray', width = 5, alpha = 0.4, align='center', edgecolor = "gray")
    ax1.tick_params(labelsize=6)
    ax1.axes.get_xaxis().set_visible(False)
    ax1.set_ylabel('Actual', size = 8)
    ax1.set_title('Month of Period', size = 8)  
    rects1 = ax1.patches

    ax1_1.bar(df['Period'].values, df['Target'], color='orange', width = 15, alpha = 0.4,  align='center', edgecolor = "orange")
    ax1_1.tick_params(labelsize=6, labelright=True)
    ax1_1.axes.get_xaxis().set_visible(False)
    ax1_1.set_ylabel('Target', size = 8)
    rects1_1 = ax1_1.patches

    ax2 = fig.add_subplot(212, sharex=ax1)
    ax2.yaxis.grid()
    x= df['Period'].values
    y = df['Actual'] - df['Target']

    colors = []
    for value in list(y): 
        if value < 0:
            colors.append('pink')
        else:
            colors.append('aquamarine')

    ax2.bar(x, y, width = 5, color=colors, align = 'center', edgecolor = colors)
    ax2.tick_params(labelsize=6)
    max_y_ax2 = (df['Actual'] - df['Target']).max() + 50
    min_y_ax2 = (df['Actual'] - df['Target']).min() - 50 
    ax2.set_ylim([min_y_ax2, max_y_ax2])
    ax2.set_xlim([datetime.date(2015, 12, 20), datetime.date(2016, 12,10 )])
    ax2.set_ylabel('Delta', size  = 8)
    rects2 = ax2.patches
    
    plt.subplots_adjust(hspace = .001)
    labels = list(y)

    L1 = list(df['Actual'])
    L2 = list(df['Target'])
    L3 = [max(l1, l2) for l1, l2 in zip(L1, L2)]

    for tx2, label in zip(rects2, labels):
        height = tx2.get_height()
        if float(label) >= 0 : 
            ax2.text(tx2.get_x() + tx2.get_width()/2, height + 5, label, ha='center', va='bottom', size = 8)
        else : 
            ax2.text(tx2.get_x() + tx2.get_width()/2, (height*-1) -30 , label, ha='center', va='bottom', size = 8)

    for tx1,tx1_1, label, l in zip(rects1,rects1_1, labels, L3):

        height = tx1.get_height()
        if label >0:
            ax1.text(tx1.get_x() + tx1.get_width()/2, l + 5, label, ha='center', va='bottom', size = 8)
        else : 
            ax1_1.text(tx1_1.get_x() + tx1_1.get_width()/2, l + 5, label, ha='center', va='bottom', size = 8)
    plt.savefig('Data_python.png')
    
if __name__==  "__main__"  : 
    main()

