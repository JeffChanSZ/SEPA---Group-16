
#JC
#from sklearn.metrics import roc_auc_score, confusion_matrix,f1_score


#JC
class ResultData(object):
      def __init__(self):
          self.cm=confusion_matrix()
          self.totalRow=0;
          self.truePositive=0;
          self.trueNegative=0;
          self.predictedPositive=0;
          self.predictedNegative=0;
          self.predictedNeutral=0;




