from django import forms


class ItemSearchForm(forms.Form):
    item_name = forms.CharField()


class CartForm(forms.Form):
    item_id = forms.IntegerField()
    buy_num = forms.IntegerField()


class OrderForm(forms.Form):
    name = forms.CharField(label="名前")
    address = forms.CharField(label="住所")
    email = forms.EmailField(label="メールアドレス")
    