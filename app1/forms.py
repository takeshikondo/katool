from django import forms

class PredictForm(forms.Form):
    input1 = forms.IntegerField(
        label='最寄駅の距離',
        required=True,
    )

    input2 = forms.IntegerField(
        label='駅利用者人数(2015)',
        required=True,
    )

    input3 = forms.IntegerField(
        label='車通行量',
        required=True,
    )

    input4 = forms.IntegerField(
        label='エリア数5分',
        required=True,
    )

    input5 = forms.IntegerField(
        label='人口総数5分',
        required=True,
    )

    input6 = forms.IntegerField(
        label='世帯数5分',
        required=True,
    )

    input7 = forms.IntegerField(
        label='昼間人口総数5分',
        required=True,
    )

    input8 = forms.IntegerField(
        label='エリア数10分',
        required=True,
    )

    input9 = forms.IntegerField(
        label='人口総数10分',
        required=True,
    )

    input10 = forms.IntegerField(
        label='世帯数10分',
        required=True,
    )

    input11 = forms.IntegerField(
        label='昼間人口総数10分',
        required=True,
    )

class PredictForm2(forms.Form):
    input1 = forms.IntegerField(
        label='営業時間',
        required=True,
    )

    input2 = forms.IntegerField(
        label='座席数',
        required=True,
    )

    input3 = forms.IntegerField(
        label='最寄駅の距離',
        required=True,
    )

    input4 = forms.IntegerField(
        label='駅利用者人数(2015)',
        required=True,
    )

    input5 = forms.IntegerField(
        label='昼間人口総数1km',
        required=True,
    )

FUNC_CHOICES = (
    ('func1', '売上分析'),
    ('func2', '費用分析'),
    ('func3', '利益分析'),
    ('func4', '郊外店売上予測'),
    ('func5', '駅前店売上予測'),
    ('func6', 'RFM分析'),
    ('func7', '画像分析'),
    ('func8', '店舗情報'),
)

class FuncForm(forms.Form):
    func = forms.ChoiceField(
        label='機能',
        widget=forms.RadioSelect,
        choices=FUNC_CHOICES,
        required=True,
    )

SALES_CHOICES = (
    ('c1', '店舗別売上'),
    ('c2', '地域別売上'),
    ('c3', '売上順位'),
)

class SalesForm(forms.Form):
    choice = forms.ChoiceField(
        label='売上',
        widget=forms.RadioSelect,
        choices=SALES_CHOICES,
        required=True,
    )

class SalesChartForm(forms.Form):
    shop_id = forms.IntegerField(
        label='店舗ID',
        required=True,
    )

class SalesAreaForm(forms.Form):
    area_id = forms.IntegerField(
        label='地域ID',
        required=True,
    )

class SalesOrderForm(forms.Form):
    year = forms.IntegerField(
        label='年',
        required=True,
    )

    month = forms.IntegerField(
        label='月',
        required=True,
    )
    
class ShopInfoForm(forms.Form):
    shop_id = forms.IntegerField(
        label='店舗ID',
        required=True,
    )    