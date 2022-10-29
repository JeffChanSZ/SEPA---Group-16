# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    column_name = ["Scale", "TweetID", "Date", "Query", "User", "Comments"]

    df = pd.read_csv("input.csv", names=column_name, encoding='latin-1')
    df['Comments'] = 'str: '+df['Comments']
    df.to_csv('str.csv')
def new():
    column_name = ["Scale", "TweetID", "Date", "Query", "User", "Comments"]
    df = pd.read_csv("data.csv", names=column_name, encoding='latin-1')
    df['Comments']=df['Comments'].str.replace("omg|lol|lmao|OMG|LOL|LMAO","").str.strip()
    df.to_csv('MR1.csv')

def new1():
    column_name = ["Scale", "TweetID", "Date", "Query", "User", "Comments"]
    df = pd.read_csv("data.csv", names=column_name, encoding='latin-1')
    df['Comments'] = df["Comments"].str.replace(r'.*(\w)\1', "").str.strip()
    df.to_csv('MR2.csv')

def test():
    df = pd.read_csv("old files/test cardif.csv", encoding='latin-1')
    df['str violation'] = df['label_str']==df['label']
    df['upper violation'] = df['label_upper']==df['label']
    print(df['str violation'].value_counts())
    print(df['upper violation'].value_counts())

    df.to_csv('test_output_cardif.csv')

def fs():
    df = pd.read_csv("sentimentrating.csv", encoding='latin-1')
    df['compare'] = (df["daisy"]!= df["CALLUM"])|(df["daisy"]!= df["Doris"])| (df["daisy"]!= df["William"])
    (df["CALLUM"]!= df["William"])|(df["CALLUM"]!= df["Doris"])| (df["William"]!= df["Doris"])
    ##output rows with no disagreements
    print(df['compare'])
    print(df['compare'].sum())
    df = df[df['compare'] == False]

    df.to_csv('fs_filtered.csv')


def MRs(n,m,p):
    df = pd.read_csv("output_NLP.csv", encoding='latin-1')

    df['original_label'] = df['original_label'].str.replace('n', n)
    df['original_label'] = df['original_label'].str.replace('m', m)
    df['original_label'] = df['original_label'].str.replace('p', p)
    print(df['original_label'].value_counts())
    df['MR1_label'] = df['MR1_label'].str.replace('1 star', 'Negative')
    df['MR1_label'] = df['MR1_label'].str.replace('2 stars', 'Negative')
    df['MR1_label'] = df['MR1_label'].str.replace('3 stars', 'Neutral')
    df['MR1_label'] = df['MR1_label'].str.replace('4 stars', 'Positive')
    df['MR1_label'] = df['MR1_label'].str.replace('5 stars', 'Positive')

    df['MR2_label'] = df['MR2_label'].str.replace('1 star', 'Negative')
    df['MR2_label'] = df['MR2_label'].str.replace('2 stars', 'Negative')
    df['MR2_label'] = df['MR2_label'].str.replace('3 stars', 'Neutral')
    df['MR2_label'] = df['MR2_label'].str.replace('4 stars', 'Positive')
    df['MR2_label'] = df['MR2_label'].str.replace('5 stars', 'Positive')

    df['MR3_label'] = df['MR3_label'].str.replace('1 star', 'Negative')
    df['MR3_label'] = df['MR3_label'].str.replace('2 stars', 'Negative')
    df['MR3_label'] = df['MR3_label'].str.replace('3 stars', 'Neutral')
    df['MR3_label'] = df['MR3_label'].str.replace('4 stars', 'Positive')
    df['MR3_label'] = df['MR3_label'].str.replace('5 stars', 'Positive')

    df['MR4_label'] = df['MR4_label'].str.replace('1 star', 'Negative')
    df['MR4_label'] = df['MR4_label'].str.replace('2 stars', 'Negative')
    df['MR4_label'] = df['MR4_label'].str.replace('3 stars', 'Neutral')
    df['MR4_label'] = df['MR4_label'].str.replace('4 stars', 'Positive')
    df['MR4_label'] = df['MR4_label'].str.replace('5 stars', 'Positive')

    df['MR5_label'] = df['MR5_label'].str.replace('1 star', 'Negative')
    df['MR5_label'] = df['MR5_label'].str.replace('2 stars', 'Negative')
    df['MR5_label'] = df['MR5_label'].str.replace('3 stars', 'Neutral')
    df['MR5_label'] = df['MR5_label'].str.replace('4 stars', 'Positive')
    df['MR5_label'] = df['MR5_label'].str.replace('5 stars', 'Positive')

    df['MR6_label'] = df['MR6_label'].str.replace('1 star', 'Negative')
    df['MR6_label'] = df['MR6_label'].str.replace('2 stars', 'Negative')
    df['MR6_label'] = df['MR6_label'].str.replace('3 stars', 'Neutral')
    df['MR6_label'] = df['MR6_label'].str.replace('4 stars', 'Positive')
    df['MR6_label'] = df['MR6_label'].str.replace('5 stars', 'Positive')

    df['MR7_label'] = df['MR7_label'].str.replace('1 star', 'Negative')
    df['MR7_label'] = df['MR7_label'].str.replace('2 stars', 'Negative')
    df['MR7_label'] = df['MR7_label'].str.replace('3 stars', 'Neutral')
    df['MR7_label'] = df['MR7_label'].str.replace('4 stars', 'Positive')
    df['MR7_label'] = df['MR7_label'].str.replace('5 stars', 'Positive')

    df['MR8_label'] = df['MR8_label'].str.replace('1 star', 'Negative')
    df['MR8_label'] = df['MR8_label'].str.replace('2 stars', 'Negative')
    df['MR8_label'] = df['MR8_label'].str.replace('3 stars', 'Neutral')
    df['MR8_label'] = df['MR8_label'].str.replace('4 stars', 'Positive')
    df['MR8_label'] = df['MR8_label'].str.replace('5 stars', 'Positive')

    df['MR9_label'] = df['MR9_label'].str.replace('1 star', 'Negative')
    df['MR9_label'] = df['MR9_label'].str.replace('2 stars', 'Negative')
    df['MR9_label'] = df['MR9_label'].str.replace('3 stars', 'Neutral')
    df['MR9_label'] = df['MR9_label'].str.replace('4 stars', 'Positive')
    df['MR9_label'] = df['MR9_label'].str.replace('5 stars', 'Positive')

    df['compare1']=(df['original_label']==p) &(df['MR1_label']==p)


    df['compare2']=(df['original_label']==n) &(df['MR2_label']==n)

    df['compare3']=((df['original_label']==p) & (df['MR3_label']==p))

    df['compare3.5']=((df['original_label']==m) & (df['MR3_label']==p))|((df['original_label']==m )&(df['MR3_label']==m) )

    df['compare4']=((df['original_label']==n) & (df['MR4_label']==n))

    df['compare4.5']=((df['original_label']==m) & (df['MR4_label']==n))|((df['original_label']==m )&(df['MR4_label']==m) )

    df['compare5']=(df['original_label']==df['MR5_label'])
    df['compare6']=(df['original_label']==df['MR6_label'])
    df['compare7']=(df['original_label']==df['MR7_label'])
    df['compare8']=(df['original_label']==df['MR8_label'])
    df['compare9']=(df['original_label']!=df['MR9_label'])

    #true means no violation
    print(df['compare1'].value_counts())
    print(df['compare2'].value_counts())
    print(df['compare3'].value_counts())
    print(df['compare3.5'].value_counts())

    print(df['compare4'].value_counts())
    print(df['compare4.5'].value_counts())

    print(df['compare5'].value_counts())
    print(df['compare6'].value_counts())
    print(df['compare7'].value_counts())
    print(df['compare8'].value_counts())

    print(df['compare9'].value_counts())
    print(df['original_label'].value_counts())
    df.to_csv('MR_testing_output_nlp.csv')


def fss(n,m,p):
    df = pd.read_csv("MR_testing_output_nlp.csv", encoding='latin-1')
    df['original_label'] = df['original_label'].str.replace('n', n)
    df['original_label'] = df['original_label'].str.replace('m', m)
    df['original_label'] = df['original_label'].str.replace('p', p)

    df2=pd.read_csv("fs_filtered.csv", encoding='latin-1')
    df2['daisy'] = df2['daisy'].str.replace('n', n)
    df2['daisy'] = df2['daisy'].str.replace('m', m)
    df2['daisy'] = df2['daisy'].str.replace('p', p)
    df3=pd.merge(df,df2,on='Comments_x')

    #compare 1= true so there is no violtion for mr1
    #mr label is dif to human
    df3['fs1']=(df3['compare1']==True) & (df3['daisy']!=df3['MR1_label'])
    df3['fs2']=(df3['compare2']==True) & (df3['daisy']!=df3['MR2_label'])
    df3['fs3']=(df3['compare3']==True) & (df3['daisy']!=df3['MR3_label'])
    df3['fs3.5']=(df3['compare3.5']==True) & (df3['daisy']!=df3['MR3_label'])
    df3['fs4']=(df3['compare4']==True) & (df3['daisy']!=df3['MR4_label'])
    df3['fs4.5']=(df3['compare4.5']==True) & (df3['daisy']!=df3['MR4_label'])

    df3['fs5']=(df3['compare5']==True) & (df3['daisy']!=df3['MR5_label'])
    df3['fs6']=(df3['compare6']==True) & (df3['daisy']!=df3['MR6_label'])
    df3['fs7']=(df3['compare7']==True) & (df3['daisy']!=df3['MR7_label'])
    df3['fs8']=(df3['compare8']==True) & (df3['daisy']!=df3['MR8_label'])
    df3['fs9']=(df3['compare9']==True) & (df3['daisy']!=df3['MR9_label'])

    print(df3['fs1'].value_counts())
    print(df3['fs2'].value_counts())
    print(df3['fs3'].value_counts())
    print(df3['fs3.5'].value_counts())
    print(df3['fs4'].value_counts())
    print(df3['fs4.5'].value_counts())
    print(df3['fs5'].value_counts())
    print(df3['fs6'].value_counts())
    print(df3['fs7'].value_counts())
    print(df3['fs8'].value_counts())
    print(df3['fs9'].value_counts())

    df3.to_csv('fs_final_nlp.csv')
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    MRs("Negative","Neutral","Positive")
    fss("Negative","Neutral","Positive")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
