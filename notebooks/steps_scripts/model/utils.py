from sklearn.base import TransformerMixin 

class StringCaster(TransformerMixin):
    def fit(self,X,y=None):
        return self

    def transform(self,X,y=None):
        return X.astype(str)
