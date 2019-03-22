from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from . import forms
import os
import pandas as pd
import numpy as np


def func_choice(request):

   if request.method == 'POST':
       #ret = request.POST['func']
       ret = request.POST.get('func')

       if ret == 'func1':
           return redirect('app1:app1_sales')
       elif ret == 'func4':
           return redirect('app1:app1_predict')
       elif ret == 'func5':
           return redirect('app1:app1_predict2')
       elif ret == 'func8':
           return redirect('app1:app1_shop_info')

       else:
            form = forms.FuncForm()

   else:
       form = forms.FuncForm()

   d = {
       'form': form
   }
   return render(request, 'app1/func_choice.html', d)

def predict(request):
    import xgboost as xgb
      
    models = []
    for i in range(100):
        model_name = './app1/src/xgb_'+str(i)+'.model'
        m = xgb.XGBRegressor()
        m.load_model(model_name)
        models.append(m)

    if request.method == 'POST':
        #form = forms.PredictForm(request.POST, request.FILES)
        form = forms.PredictForm(request.POST)

        if form.is_valid():
            #model = xgb.XGBRegressor()
            #model.load_model('./app1/src/xgb.model')

            input1 = form.cleaned_data['input1']
            input2 = form.cleaned_data['input2']
            input3 = form.cleaned_data['input3']
            input4 = form.cleaned_data['input4']
            input5 = form.cleaned_data['input5']
            input6 = form.cleaned_data['input6']
            input7 = form.cleaned_data['input7']
            input8 = form.cleaned_data['input8']
            input9 = form.cleaned_data['input9']
            input10 = form.cleaned_data['input10']
            input11 = form.cleaned_data['input11']

            inputs = np.array([input1, input2, input3, input4, input5,
                               input6, input7, input8, input9, input10, input11])
            inputs = np.expand_dims(inputs, axis=0)

            preds = []
            for i in range(100):
                m = models[i]
                pred = m.predict(inputs)[0]
                preds.append(pred)

            mean = np.mean(np.array(preds))
            std = np.std(np.array(preds))

            mean_str = '{:,}'.format(int(mean))
            std_str = '{:,}'.format(int(std))

            jan = '{:,}'.format(int(mean / 12 * 1.0))
            feb = '{:,}'.format(int(mean / 12 * 0.95))
            mar = '{:,}'.format(int(mean / 12 * 1.04))
            apr = '{:,}'.format(int(mean / 12 * 0.97))
            may = '{:,}'.format(int(mean / 12 * 0.98))
            jun = '{:,}'.format(int(mean / 12 * 0.94))
            jul = '{:,}'.format(int(mean / 12 * 0.97))
            aug = '{:,}'.format(int(mean / 12 * 1.02))
            sep = '{:,}'.format(int(mean / 12 * 0.96))
            oct = '{:,}'.format(int(mean / 12 * 1.02))
            nov = '{:,}'.format(int(mean / 12 * 1.0))
            dec = '{:,}'.format(int(mean / 12 * 1.1))
            
            d = {
                'mean': mean_str,
                'std': std_str,
                'jan': jan,
                'feb': feb,
                'mar': mar,
                'apr': apr,
                'may': may,
                'jun': jun,
                'jul': jul,
                'aug': aug,
                'sep': sep,
                'oct': oct,
                'nov': nov,
                'dec': dec,
            }

            return render(request, 'app1/predict_output.html', d)

        else:
            return HttpResponse('invalid form')

    else:
        form = forms.PredictForm()

    d = {
            'form': form
    }

    return render(request, 'app1/predict_input.html', d)

def predict2(request):

    if request.method == 'POST':
        form = forms.PredictForm2(request.POST)

        if form.is_valid():

            input1 = form.cleaned_data['input1']
            input2 = form.cleaned_data['input2']
            input3 = form.cleaned_data['input3']
            input4 = form.cleaned_data['input4']
            input5 = form.cleaned_data['input5']

            # to be modified later
            b0 = 1717.4545771907906
            b1 = 268.6052
            b2 = 93.0831
            b3 = -11.3042
            b4 = 0.01289
            b5 = -0.0006

            mean = b0 + b1*input1 + b2*input2 + b3*input3 + b4*input4 + b5*input5
            mean_str = '{:,}'.format(int(mean))

            jan = '{:,}'.format(int(mean / 12 * 1.0))
            feb = '{:,}'.format(int(mean / 12 * 0.95))
            mar = '{:,}'.format(int(mean / 12 * 1.04))
            apr = '{:,}'.format(int(mean / 12 * 0.97))
            may = '{:,}'.format(int(mean / 12 * 0.98))
            jun = '{:,}'.format(int(mean / 12 * 0.94))
            jul = '{:,}'.format(int(mean / 12 * 0.97))
            aug = '{:,}'.format(int(mean / 12 * 1.02))
            sep = '{:,}'.format(int(mean / 12 * 0.96))
            oct = '{:,}'.format(int(mean / 12 * 1.02))
            nov = '{:,}'.format(int(mean / 12 * 1.0))
            dec = '{:,}'.format(int(mean / 12 * 1.1))

            d = {
                'mean': mean_str,
                'jan': jan,
                'feb': feb,
                'mar': mar,
                'apr': apr,
                'may': may,
                'jun': jun,
                'jul': jul,
                'aug': aug,
                'sep': sep,
                'oct': oct,
                'nov': nov,
                'dec': dec,
            }

            return render(request, 'app1/predict_output2.html', d)

        else:
            return HttpResponse('invalid form')

    else:
        form = forms.PredictForm2()

    d = {
            'form': form
    }

    return render(request, 'app1/predict_input2.html', d)

def sales_choice(request):

   if request.method == 'POST':
       ret = request.POST.get('choice')

       if ret == 'c1':
           return redirect('app1:app1_sales_chart')

       elif ret == 'c2':
           return redirect('app1:app1_sales_area')

       elif ret == 'c3':
           return redirect('app1:app1_sales_order')

       else:
            form = forms.SalesForm()

   else:
       form = forms.SalesForm()

   d = {
       'form': form
   }
   return render(request, 'app1/sales_choice.html', d)

def sales_chart(request):
    
    file = './static/app1/temp_image/chart.png'
    if os.path.isfile(file):
        os.remove(file)

    if request.method == 'POST':
                  
        form = forms.SalesChartForm(request.POST)

        if form.is_valid():
            import matplotlib.pyplot as plt
            
            path = './static/app1/'
            df_info = pd.read_csv(path+'info.csv')
            df_sales = pd.read_csv(path+'sales.csv')
                    
            shop_id = form.cleaned_data['shop_id']
            df_temp = df_sales[df_sales['id']==shop_id]
            df_temp = df_temp.sort_values('time').reset_index(drop=True)
            
            if len(df_temp) == 0:
                return render(request, 'app1/sales_chart_output2.html')
            
            name = df_info[df_info['id']==shop_id]['name'].values[0]
            sales = df_temp['sales'].values
            
            year_s = int(df_temp['time'].values[0]/100)
            month_s = int(df_temp['time'].values[0] - year_s*100)
            year_e = int(df_temp['time'].values[-1]/100)
            month_e = int(df_temp['time'].values[-1] - year_e*100)
            
            d = {
                'shop_id': shop_id,
                'name': name,
                'year_s': year_s,
                'month_s': month_s,
                'year_e': year_e,
                'month_e': month_e,
                'mean': '{:,}'.format(int(np.mean(sales))),
                'std': '{:,}'.format(int(np.std(sales))),
                'max': '{:,}'.format(int(np.max(sales))),
                'min': '{:,}'.format(int(np.min(sales))),
            }
            
            plt.figure(figsize=(5, 3))
            plt.plot(sales)
            plt.grid(True)
            plt.savefig(path+'temp_image/chart.png')
            plt.close()

            return render(request, 'app1/sales_chart_output1.html', d)
           
        else:
            return HttpResponse('invalid form')

    else:
        form = forms.SalesChartForm()

    d = {
            'form': form
    }

    return render(request, 'app1/sales_chart_input.html', d)

def sales_area(request):

    if request.method == 'POST':
        form = forms.SalesAreaForm(request.POST)

        if form.is_valid():

            area_id = form.cleaned_data['area_id']

            d = {
                'area_id': area_id,
            }

            #return render(request, 'app1/sales_area_output.html', d)
            return redirect('app1:app1_sales_area')

        else:
            return HttpResponse('invalid form')

    else:
        form = forms.SalesAreaForm()

    d = {
            'form': form
    }

    return render(request, 'app1/sales_area_input.html', d)

def sales_order(request):

    if request.method == 'POST':
        form = forms.SalesOrderForm(request.POST)

        if form.is_valid():
            
            path = './static/app1/'
            df_info = pd.read_csv(path+'info.csv')
            df_sales = pd.read_csv(path+'sales.csv')

            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            
            df_temp = df_sales[df_sales['time']==year*100+month].sort_values('sales', ascending=False)
            
            if len(df_temp) == 0:
                return render(request, 'app1/sales_order_output2.html')
            
            u_10_ids = df_temp['id'].values[:10]
            l_10_ids = df_temp['id'].values[-10:]

            u_10_names = []
            u_10_sales = []
            for i in u_10_ids:
                u_10_names.append(df_info[df_info['id']==i]['name'].values[0])
                u_10_sales.append(df_temp[df_temp['id']==i]['sales'].values[0])
          
            l_10_names = []
            l_10_sales = []
            for i in l_10_ids:
                l_10_names.append(df_info[df_info['id']==i]['name'].values[0])
                l_10_sales.append(df_temp[df_temp['id']==i]['sales'].values[0])
  
            d = {
                'year': year,
                'month': month,
                'u_1_name': u_10_names[0],
                'u_2_name': u_10_names[1],
                'u_3_name': u_10_names[2],
                'u_4_name': u_10_names[3],
                'u_5_name': u_10_names[4],
                'u_6_name': u_10_names[5],
                'u_7_name': u_10_names[6],
                'u_8_name': u_10_names[7],
                'u_9_name': u_10_names[8],
                'u_10_name': u_10_names[9],
                'u_1_sales': '{:,}'.format(u_10_sales[0]),
                'u_2_sales': '{:,}'.format(u_10_sales[1]),
                'u_3_sales': '{:,}'.format(u_10_sales[2]),
                'u_4_sales': '{:,}'.format(u_10_sales[3]),
                'u_5_sales': '{:,}'.format(u_10_sales[4]),
                'u_6_sales': '{:,}'.format(u_10_sales[5]),
                'u_7_sales': '{:,}'.format(u_10_sales[6]),
                'u_8_sales': '{:,}'.format(u_10_sales[7]),
                'u_9_sales': '{:,}'.format(u_10_sales[8]),
                'u_10_sales':'{:,}'.format(u_10_sales[9]),
                'l_1_name': l_10_names[0],
                'l_2_name': l_10_names[1],
                'l_3_name': l_10_names[2],
                'l_4_name': l_10_names[3],
                'l_5_name': l_10_names[4],
                'l_6_name': l_10_names[5],
                'l_7_name': l_10_names[6],
                'l_8_name': l_10_names[7],
                'l_9_name': l_10_names[8],
                'l_10_name': l_10_names[9],
                'l_1_sales': '{:,}'.format(l_10_sales[0]),
                'l_2_sales': '{:,}'.format(l_10_sales[1]),
                'l_3_sales': '{:,}'.format(l_10_sales[2]),
                'l_4_sales': '{:,}'.format(l_10_sales[3]),
                'l_5_sales': '{:,}'.format(l_10_sales[4]),
                'l_6_sales': '{:,}'.format(l_10_sales[5]),
                'l_7_sales': '{:,}'.format(l_10_sales[6]),
                'l_8_sales': '{:,}'.format(l_10_sales[7]),
                'l_9_sales': '{:,}'.format(l_10_sales[8]),
                'l_10_sales':'{:,}'.format(l_10_sales[9]),                             
            }

            return render(request, 'app1/sales_order_output1.html', d)
            #return redirect('app1:app1_sales_order')

        else:
            return HttpResponse('invalid form')

    else:
        form = forms.SalesOrderForm()

    d = {
            'form': form
    }

    return render(request, 'app1/sales_order_input.html', d)

def shop_info(request):
    
    if request.method == 'POST':
                  
        form = forms.ShopInfoForm(request.POST)

        if form.is_valid():
            
            path = './static/app1/'
            df_info = pd.read_csv(path+'info.csv')
            df_shop = pd.read_csv(path+'shop.csv')
                    
            shop_id = form.cleaned_data['shop_id']
            df_temp = df_info[df_info['id']==shop_id]
            df_temp2 = df_shop[df_shop['id']==shop_id]
            
            if len(df_temp) == 0:
                return render(request, 'app1/shop_info_output2.html')
            
            name = df_temp['name'].values[0]
            open_ym = df_temp['open'].values[0]
            if not np.isnan(open_ym):
                open_ym = int(open_ym)
            shop_type = df_temp2['type'].values[0]                
            n_seats = df_temp['n_seats'].values[0]
            park = df_temp['park'].values[0]
            
            d = {
                'shop_id': shop_id,
                'name': name,
                'open_ym': open_ym,
                'shop_type': shop_type,
                'n_seats': int(n_seats),
                'park': int(park),
            }
            
            return render(request, 'app1/shop_info_output1.html', d)
           
        else:
            return HttpResponse('invalid form')

    else:
        form = forms.ShopInfoForm()

    d = {
            'form': form
    }

    return render(request, 'app1/shop_info_input.html', d)
