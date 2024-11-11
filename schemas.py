from pydantic import BaseModel, model_validator, ValidationError

class SearchInfo(BaseModel):
    viewSize: int
    count: int
    searchTerm: str


class SearchItem(BaseModel):
    id: str
    modelNumber: str
    price: str
    salePrice: str
    #discount: str
    title: str
    subTitle: str
    rating: str
    ratingCount: str
    
    @model_validator(mode='before')
    @classmethod
    def extract_price_data(cls, values):
        '''
        price_data = values.get('priceData', {})
        values['price'] = price_data.get('price')
        values['salePrice'] = price_data.get('salePrice')
        values['discount'] = price_data.get('discountText')
        return values
        '''
        if values.get('rating') == None:
            values['rating'] = -1
        values['id'] = values.get('productId')
        values['modelNumber'] = values.get('modelId')
        values['title'] = values.get('displayName')

        values['price'] = str(values.get('price'))
        values['salePrice'] = str(values.get('salePrice'))
        values['rating'] = str(values.get('rating'))
        values['ratingCount'] = str(values.get('ratingCount'))

        return values


class ItemDetial(BaseModel):
    brand: str
    sale: str
    gender: str
    outlet: str
    color: str
    @model_validator(mode='before')
    @classmethod
    def cast(cls, values):
         values['sale'] = str(values.get('sale'))
         values['outlet'] = str(values.get('outlet'))
         return values


class ItemAvailability(BaseModel):
    sku: str
    availability: str
    size: str
    @model_validator(mode='before')
    @classmethod
    def cast(cls, values):
         values['size'] = str(values.get('size'))
         values['availability'] = str(values.get('availability'))
         return values


