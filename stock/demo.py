__author__ = 'jjzhu'
import numpy as np
import talib
import tushare as ts
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import confusion_matrix
from sklearn.utils import shuffle
from sklearn import  svm


import matplotlib.pyplot as plt
import platform
import os
import logging
import logging.config


def logger_conf():
    """
    load basic logger configure
    :return: configured logger
    """

    if platform.system() is 'Windows':

        logging.config.fileConfig(os.path.abspath('./')+'\\logging.conf')
    elif platform.system() is 'Linux':
                logging.config.fileConfig(os.path.abspath('./')+'/logging.conf')
    elif platform.system() is 'Darwin':
            logging.config.fileConfig(os.path.abspath('./') + '/logging.conf')
    logger = logging.getLogger('simpleLogger')
    return logger


class Analyze:
    def __init__(self, code='600036'):
        self.code = code
        self.my_logger = logger_conf()

    def get_train_data(self):
       # df = ts.get_h_data("600036", start="2002-01-01", end="2016-11-1",index=True)  # 浙大网新code
        df = ts.get_hist_data("600036")  # 浙大网新code
        close = np.array(df['close'])[::-1]  # 逆序
        # --涨跌标签
        # 最后一天是不用的
        target = [0]*(len(close)-1)
        for i in range(len(close)-1):
            if close[i] < close[i+1]:
                target[i] = 1  # 涨
            elif close[i] == close[i+1]:
                target[i] = 0  # 不变
            else:
                target[i] = -1  # 跌
        df = shuffle(df)
        close = np.array(df['close'])[::-1]  # 逆序
        turnover = np.array(df['turnover'])
        volume = np.array(df['volume'])  # 交易量
        open = np.array(df['open'])  # 开盘价
        low = np.array(df['low'])  # 最低价
        high = np.array(df['high'])  # 最高价
        price_change = np.array(df['price_change'])  # 价格变动
        p_change = np.array(df['p_change'])  # 涨跌幅
        ma5 = np.array(df['ma5'])
        ma10 = np.array(df['ma10'])
        ma20 = np.array(df['ma20'])
        v_ma5 = np.array(df['v_ma5'])
        v_ma10 = np.array(df['v_ma10'])
        v_ma20 = np.array(df['v_ma20'])
        # 计算macd（ 前面33天为NAN）
        macd, macd_signal, macd_hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
        # 威廉指标
        # 前13天是nan
        willr = talib.WILLR(np.array(df['high']), np.array(df['low']), np.array(df['close']))
        # rsi 前14天NAN
        rsi = talib.RSI(close)
        # 能量潮指标
        obv = talib.OBV(close, volume)
        # ROC 前十天NAN
        roc = talib.ROC(close)
        # SAR 停损转向操作点指标
        sar = talib.SAR(high, low)
        # TRIX 三重指数平滑移动平均
        TRIX = talib.TRIX(close)
        # CCI 顺势指标
        CCI = talib.CCI(high, low, close)
        # KAMA 适应性移动平均线
        KAMA = talib.KAMA(close)
        # EMA 指数平均数指标
        EMA = talib.EMA(close)
        # BOP 均势指标
        BOP = talib.BOP(open, high, low, close)
        NUM = 88
        length = len(close[NUM:-1])
        # print(close[NUM:-1])
        # print(length)
        train_data = np.row_stack((close[NUM:-1].reshape(1, length),
                                   turnover[NUM:-1].reshape(1, length),
                                   volume[NUM:-1].reshape(1, length),
                                   open[NUM:-1].reshape(1, length),
                                   low[NUM:-1].reshape(1, length),
                                   high[NUM:-1].reshape(1, length),
                                   price_change[NUM:-1].reshape(1, length),
                                   p_change[NUM:-1].reshape(1, length),
                                   ma5[NUM:-1].reshape(1, length),
                                   ma10[NUM:-1].reshape(1, length),
                                   ma20[NUM:-1].reshape(1, length),
                                   v_ma5[NUM:-1].reshape(1, length),
                                   v_ma10[NUM:-1].reshape(1, length),
                                   v_ma20[NUM:-1].reshape(1, length),
                                   macd[NUM:-1].reshape(1, length),
                                   willr[NUM:-1].reshape(1, length),
                                   rsi[NUM:-1].reshape(1, length),
                                   obv[NUM:-1].reshape(1, length),
                                   sar[NUM:-1].reshape(1, length),
                                   roc[NUM:-1].reshape(1, length),
                                   TRIX[NUM:-1].reshape(1, length),
                                   CCI[NUM:-1].reshape(1, length),
                                   KAMA[NUM:-1].reshape(1, length),
                                   EMA[NUM:-1].reshape(1, length),
                                   BOP[NUM:-1].reshape(1, length)

                                   ))
        target_data = np.array(target[NUM:])  # 去了前NUM天的数据
        min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))  # 归一化？
        pro_train_data = min_max_scaler.fit_transform(train_data).T  # 矩阵转置
        return pro_train_data, target_data

    # def train(self):
    #     self.my_logger.info('hello')
    #     train_data, target_data = self.get_train_data()
    #     crf = RandomForestClassifier(max_depth=40, random_state=2)
    #     score = cross_val_score(crf, train_data, target_data, cv=10)
    #     print(score)
    #     print(score.mean())
    #     # svm算法训练结果
    #     xyz=svm.SVC(C=2.0,random_state=200)
    #     another_score=cross_val_score(xyz, train_data, target_data, cv=10)
    #     print(another_score.mean())



    def print_grid_search_info(self, model_n, param):
        self.my_logger.info('grid search.....')
        self.my_logger.info('Model: ' + model_n)
        self.my_logger.info('parameters:')
        self.my_logger.info(param)

    def print_best_params(self, params, gs):
        """
        print best parameters
        :param params: grid search parameters
        :param gs: grid search result
        :return: null
        """
        self.my_logger.info('Best score: %0.6f' % gs.best_score_)
        self.my_logger.info('Best parameters set:')
        best_parameters = gs.best_estimator_.get_params()
        for param_name in sorted(params.keys()):
            print('\t%s: %r' % (param_name, best_parameters[param_name]))

    def validation(self):
        train_data, target_data = self.get_train_data()
        model_params = {
            'max_depth': tuple([_+1 for _ in range(3,30)])
        }

        # s_train_data, s_test_data, s_train_target, s_test_target = train_test_split(train_data, target_data, test_size=0.3, random_state=0)
        regr_rf = RandomForestClassifier(n_estimators=30)
        # 网格搜索
        grid_scv = GridSearchCV(regr_rf, param_grid=model_params, n_jobs=-1, verbose=0)
        self.print_grid_search_info('RandomForestClassifier', model_params)
        grid_scv.fit(train_data, target_data)
        score_one = cross_val_score(grid_scv, train_data, target_data, cv=10)
        self.print_best_params(model_params,grid_scv)
        print (score_one.mean())
        #self.grid_C(model_params, grid_scv)
        #self.train()
        # regr_rf.fit(s_train_data, s_train_target)
        # pre = regr_rf.predict(s_test_data)
        # cm = confusion_matrix(s_test_target, pre)  # 混淆矩阵
        # print(cm)
        # plt.matshow(cm)
        # plt.title('随机森林分类的混淆矩阵')
        # plt.colorbar()
        # plt.show()
    def validation_svm(self):
        train_data, target_data = self.get_train_data()
        model_params_C = {
            'C':[10,0.00001,1000,10000]
        }
        svm_rf = svm.SVC(kernel="poly",random_state=20)
        grid_C = GridSearchCV(svm_rf, param_grid=model_params_C,cv=3,n_jobs=1, verbose=0)
        #print(grid_C)
        print (grid_C.fit(train_data, target_data).best_params_)


    def start(self):
        #self.validation()
        self.validation_svm()

if __name__ == '__main__':
    ana = Analyze()
    ana.start()

