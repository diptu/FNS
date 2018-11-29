from haystack import indexes
from properties.models import Ad


class AdIndex(indexes.SearchIndex, indexes.Indexable):
    text    = indexes.CharField(document=True, use_template=True)
    title   = indexes.CharField(model_attr='title')

    def get_model(self):
        return Ad

    
