pip install -g firebase-tools
import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output
from google.colab import files
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, initialize_app
from PIL import Image
 

cred = credentials.Certificate("./data-analytics-1-a1fc9-firebase-adminsdk-7pw8e-d090a8ace0.json") #key connect database
firebase_admin.initialize_app(cred)
db = firestore.client()
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])
 # home page
main = html.Div([
    html.Div([
      html.Div('HOME PAGE', style={'font-size': '60px','text-align': 'center','font-weight': 'bold','color':'white'}),
      # another page
      html.Div([
        dcc.Link('Simple Chart', href='/matplotlib', style={'font-size': '30px','color':'white'}),
        dcc.Link('Data Analysis', href='/data-analysis', style={'font-size': '30px','color':'white'})
       ],style={'display': 'flex','justify-content': 'space-evenly',}),
      html.Div([
        html.Div([
            html.Div('Giới thiệu về project: ', style={'font-size': '25px','font-weight': 'bold',}),
            html.Div([
                html.Div( [
                    html.Div('-Project U.S Air Pollution Data (Dữ liệu về ô nhiễm không khí tại Mỹ): Nghiên cứu về vấn đề liên quan ô nhiễm không khí tại Mỹ '),
                    html.Div('- Project này sử dụng Framework Dash - Plotly để xây dựng và dữ liệu được lấy từ trang data.world để phân tích ')
                ]),
            ], className='row', style={ 'font-size': '18px' ,'border':'2px black solid','background-color': '#fefbd8'})
        ])
      ]),
      html.Br(),
      html.Div([
        html.Div([
            html.Div('About my team:', style={'font-size': '25px','font-weight': 'bold',}),
            html.Div([
                html.Div([
                  html.Div('Nguyễn Thế Đạt - 18036401'),
                  html.Div('Ngô Quang Long 18039011'),
                  html.Div('Lê Dĩ Khang - 18037851'),  
                  ],className='col-6'),
                html.Div( [
                  html.Div('Nguyễn Trần Nhật Hưng - 18036971'),
                  html.Div('Bùi Thành Nam - 18055471'),
                  html.Div('Nguyễn Thanh Hoài - 18052451'),   
                  html.Div('Lý Huỳnh Gia Thịnh - 18036741')       
                  ],className='col-6'),
                ], className='row',  style={ 'font-size': '18px' ,'border':'2px black solid','background-color': '#fefbd8'})
            ])
      ]),
    ],className='col-12 bg-info') 
],className='container')

##-----------------------------------------------------
#matplotlib Link
matplotlib = html.Div([
     # home page text
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib",style={'color':'white'}),
                dcc.Link('Line Chart', href="/line-chart",style={'color':'white'}),
                dcc.Link('Bar Chart', href="/bar-chart",style={'color':'white'}),
                dcc.Link('Pie Chart', href="/pie-chart",style={'color':'white'}),
                dcc.Link('Scatter Chart', href="/scatter-chart",style={'color':'white'}),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-info',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('MATPLOTLIB',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                 html.Span('Giới thiệu về Dash - Plotly:'),
                html.Span('Dash là một framework mã nguồn mở dành cho xây dựng ứng dụng phân tích dữ liệu mà không cần đến Ngôn ngữ JavaScript, và nó được tích hợp với thi viện Plotly - một thư viện đồ họa. '
                ,style={'margin-left': '30px'})
            ])
           
        ],className='col-9 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
    ], className = 'row')
], className='container')
state_list=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Country_Of_Mexico','Delaware','District_Of_Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Missouri','Nevada','New_Hampshire','New_Jersey','New_Mexico','New_York','North_Carolina','North_Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode_Island','South_Carolina','South_Dakota','Tennessee','Texas','Utah','Virginia','Washington','Wisconsin','Wyoming']
docs =db.collection(u'linechart_AQI_year_CO').stream()
c=[]
year=[]
docsNO2 =db.collection(u'linechart_AQI_year_NO2').stream()
cNO2=[]
docsO3 =db.collection(u'linechart_AQI_year_O3').stream()
cO3=[]
docsSO2 =db.collection(u'linechart_AQI_year_SO2').stream()
cSO2=[]
for docO3 in docsO3:
  cO3.append(docO3.to_dict())
for docSO2 in docsSO2:
  cSO2.append(docSO2.to_dict())
for docNO2 in docsNO2:
  cNO2.append(docNO2.to_dict())
for doc in docs:
  c.append(doc.to_dict())
  year.append(doc.id)
y = [list() for x in range(47)]
yNO2 = [list() for x in range(47)]
yO3 = [list() for x in range(47)]
ySO2 = [list() for x in range(47)]
for i in range(16):
  for j in range(47):
    y[j].append(c[i][state_list[j]])
    yNO2[j].append(cNO2[i][state_list[j]])  
    yO3[j].append(cO3[i][state_list[j]])
    ySO2[j].append(cSO2[i][state_list[j]])
  figO3 = go.Figure()
  figCO = go.Figure()
  figO3 = go.Figure()
  figSO2 = go.Figure()
  figNO2 = go.Figure()
for k in range(46):
  figCO.add_trace(go.Scatter(x=year, y=y[k],mode='lines',name=state_list[k]))
  figNO2.add_trace(go.Scatter(x=year, y=yNO2[k],mode='lines',name=state_list[k]))
  figO3.add_trace(go.Scatter(x=year, y=yO3[k],mode='lines',name=state_list[k]))
  figSO2.add_trace(go.Scatter(x=year, y=ySO2[k],mode='lines',name=state_list[k]))
figCO.update_layout(title='Biểu đồ line mức độ AQI trung bình khí CO của các bang ở Mỹ 2000-2016',
                      xaxis_title='Năm',
                      yaxis_title='AQI')
figNO2.update_layout(title='Biểu đồ line mức độ AQI trung bình khí NO2 của các bang ở Mỹ 2000-2016',
                      xaxis_title='Năm',
                      yaxis_title='AQI')
figO3.update_layout(title='Biểu đồ line mức độ AQI trung bình khí O3 của các bang ở Mỹ 2000-2016',
                      xaxis_title='Năm',
                      yaxis_title='AQI')
figSO2.update_layout(title='Biểu đồ line mức độ AQI trung bình khí SO2 của các bang ở Mỹ2000-2016',
                      xaxis_title='năm ',
                      yaxis_title='AQI')
docs =db.collection(u'pie_and_line_mean_AQI_2000_2016').stream()
c=[]
year=[]
meana=[]
meanb=[]
meanc=[]
meand=[]
for doc in docs:
    c.append(doc.to_dict())
    year.append(doc.id)
y = [list() for x in range(17)]
for i in range(17):
    meana.append(c[i]['mean_AQI_CO'])
    meanb.append(c[i]['mean_AQI_NO2'])
    meanc.append(c[i]['mean_AQI_O3'])
    meand.append(c[i]['mean_AQI_SO2'])
figmean=go.Figure()
figmean.add_trace(go.Scatter(x=year, y=meana,mode='lines',name ='AQI CO' ))
figmean.add_trace(go.Scatter(x=year, y=meanb,mode='lines',name ='AQI NO2' ))
figmean.add_trace(go.Scatter(x=year, y=meanc,mode='lines',name ='AQI O3' ))
figmean.add_trace(go.Scatter(x=year, y=meand,mode='lines',name ='AQI SO2' ))
figmean.update_layout(title='Biểu đồ line mức độ AQI trung bình các khí ở Mỹ giai đoạn 2000-2016',
                      xaxis_title='Năm',
                      yaxis_title='AQI')
# Line Chart 
lineChart = html.Div([
     # home page text
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib",style={'color':'white'}),
                dcc.Link('Line Chart', href="/line-chart",style={'color':'white'}),
                dcc.Link('Bar Chart', href="/bar-chart",style={'color':'white'}),
                dcc.Link('Pie Chart', href="/pie-chart",style={'color':'white'}),
                dcc.Link('Scatter Chart', href="/scatter-chart",style={'color':'white'}),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-info',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('Line Chart',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                
                html.Span('-Line là dạng biểu đồ để thể hiện tiến trình thay đổi, động thái gia tăng của một đối tượng hay một nhóm đối tượng nào đó qua thời gian.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                html.Span('-Line chart (biểu đồ đường): được sử dụng khi dữ liệu được mô tả phụ thuộc vào thời gian với trục hoành biểu diễn thời gian và trục tung biểu diễn đại lượng AQI. Sử dụng để theo dõi sự thay đổi mức độ AQI các khí theo từng bang.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div('Ý nghĩa chỉ số AQI'),
            html.Img(src=Image.open('./scatter/thangdo.jpg'), className= 'col-8',style={'align':'center'}),
            html.Div('*Nhấn chọn bang trên chú thích bên phải biểu đồ để ẩn/hiện line', style={'font-size':'13px', 'color':'red'}),
            
            html.Div([
              
                html.Div(
                dcc.Graph(figure=figCO), 
                )
            ], className='row'),
            html.Div([
                  html.Br(),html.Br()
            ]),
            
             html.Div([
                html.Div(
                    dcc.Graph(figure=figNO2),
                )
            ], className='row'),
            html.Div([
                  html.Br(),html.Br()
            ]),
                html.Div([
                     dcc.Graph(figure=figO3)
            ], className='row'),
            html.Div([
                  html.Br(),html.Br()
            ]),
            html.Div([
                html.Div(
                    dcc.Graph(figure=figSO2),
                )
            ], className='row'),
           html.Div([
                  html.Br(),html.Br()
            ]),
            
            html.Div([              
                html.Div(
                    dcc.Graph(figure=figmean),
                ),
                html.Br(),

            ], className='row bg-success'),
        ],className='col-9 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
], className='container'),])
# # Bar Chart 
barChart = html.Div([
     # home page text
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib",style={'color':'white'}),
                dcc.Link('Line Chart', href="/line-chart",style={'color':'white'}),
                dcc.Link('Bar Chart', href="/bar-chart",style={'color':'white'}),
                dcc.Link('Pie Chart', href="/pie-chart",style={'color':'white'}),
                dcc.Link('Scatter Chart', href="/scatter-chart",style={'color':'white'}),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-info',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
               html.Div('Bar Chart',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                html.Span('Dạng biểu đồ này dùng để so sánh tương quan về độ lớn giữa các đại lượng hoặc thể hiện một thành phần cơ cấu trong một tổng thể.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                html.Span('Bar chart (biểu đồ cột): thường được dùng khi cần phân loại dữ liệu và so sánh độ tương quản giữa chúng. Sử dụng để so sáng AQI của từng loại khí và sự tương quan giữa các bang. '
                ,style={'margin-left': '30px'})
            ]),
          
             html.Div('Ý nghĩa chỉ số AQI '),
            html.Img(src=Image.open('./scatter/thangdo.jpg'), className= 'col-8',style={'align':'center'}),
            html.Div([
                  html.Br(),html.Br()
            ]),
            html.Div('Chọn năm'),
            html.Div([
              html.Div([

    dcc.Dropdown(id='dropdown', options=[
            {'label': '2000', 'value': '2000'},
            {'label': '2001', 'value': '2001'},
            {'label': '2002', 'value': '2002'},
            {'label': '2003', 'value': '2003'},
            {'label': '2004', 'value': '2004'},
            {'label': '2005', 'value': '2005'},
            {'label': '2006', 'value': '2006'},
            {'label': '2007', 'value': '2007'},
            {'label': '2008', 'value': '2008'},
            {'label': '2009', 'value': '2009'},
            {'label': '2010', 'value': '2010'},
            {'label': '2011', 'value': '2011'},
            {'label': '2012', 'value': '2012'},
            {'label': '2013', 'value': '2013'},
            {'label': '2014', 'value': '2014'},
            {'label': '2015', 'value': '2015'},
            {'label': '2016', 'value': '2016'},
          ], placeholder="chon nam",
            value='2000'),
    dcc.Graph(id='graph-court')

    ], style={'padding-right': '5px','padding-left': '5px'})
            ]),
        ],className='col-9 bg-light',style={'border-radius': '3px'}),
    ], className = 'row')
], className='container')


@app.callback(Output('graph-court', 'figure'), 
              [Input('dropdown', 'value')])

def update_graph(selected_value):
  
  if selected_value ==  '2000':
    docs = db.collection(u'barchart_AQI_State_2000').stream()
  elif selected_value== '2001':
    docs = db.collection(u'barchart_AQI_State_2001').stream()

  elif selected_value== '2002':
    docs = db.collection(u'barchart_AQI_State_2002').stream()

  elif selected_value== '2003':
    docs = db.collection(u'barchart_AQI_State_2003').stream()

  elif selected_value== '2004':
    docs = db.collection(u'barchart_AQI_State_2004').stream()
 
  elif selected_value== '2005':
    docs = db.collection(u'barchart_AQI_State_2005').stream()
  
  elif selected_value== '2006':
    docs = db.collection(u'barchart_AQI_State_2006').stream()
   
  elif selected_value== '2007':
    docs = db.collection(u'barchart_AQI_State_2007').stream()
    
  elif selected_value== '2008':
    docs = db.collection(u'barchart_AQI_State_2008').stream()

  elif selected_value== '2009':
    docs = db.collection(u'barchart_AQI_State_2009').stream()
   
  elif selected_value== '2010':
    docs = db.collection(u'barchart_AQI_State_2010').stream()
    
  elif selected_value== '2011':
    docs = db.collection(u'barchart_AQI_State_2011').stream()
   
  elif selected_value== '2012':
    docs = db.collection(u'barchart_AQI_State_2012').stream()
 
  elif selected_value== '2013':
    docs = db.collection(u'barchart_AQI_State_2013').stream()
   
  elif selected_value== '2014':
    docs = db.collection(u'barchart_AQI_State_2014').stream()
  
  elif selected_value== '2015':
    docs = db.collection(u'barchart_AQI_State_2015').stream()
   
  elif selected_value== '2016':
    docs = db.collection(u'barchart_AQI_State_2016').stream()
  c=[]
  for doc in docs:
    c.append(doc.to_dict())
  state_list=[]
  AQI_NO2=[]
  AQI_O3=[]
  AQI_SO2=[]
  AQI_CO=[]
  for i in range(len(c)):
    state_list.append(c[i]['state'])
    AQI_NO2.append(c[i]['mean_AQI_NO2'])
    AQI_O3.append(c[i]['mean_AQI_O3'])
    AQI_SO2.append(c[i]['mean_AQI_SO2'])
    AQI_CO.append(c[i]['mean_AQI_CO'])
  data=[
                {'x': state_list, 'y': AQI_NO2 , 'type': 'bar', 'name': 'AQI NO2'},
                {'x': state_list, 'y': AQI_O3, 'type': 'bar', 'name': 'AQI_O3'},
                {'x': state_list, 'y': AQI_SO2, 'type': 'bar', 'name': 'AQI_SO2'},
                {'x': state_list, 'y': AQI_CO, 'type': 'bar', 'name': 'AQI_CO'},
            ]
  b=data   
  fig = go.Figure()
  fig.add_bar(x=b[0]["x"],y=b[0]["y"],name=b[0]["name"])
  fig.add_bar(x=b[1]["x"],y=b[1]["y"],name=b[1]["name"])
  fig.add_bar(x=b[2]["x"],y=b[2]["y"],name=b[2]["name"])
  fig.add_bar(x=b[3]["x"],y=b[3]["y"],name=b[3]["name"])
  fig.update_layout(title='Biểu đồ cột  thể hiện mức độ AQI của các bang ở Mỹ theo năm '+selected_value)
  return fig

docs =db.collection(u'pie_and_line_mean_AQI_2000_2016').stream()
c=[]
for doc in docs:
  c.append(doc.to_dict())
  year.append(doc.id)
y = [list() for x in range(17)]
for i in range(17):
  y[i].append(c[i]['mean_AQI_CO'])
  y[i].append(c[i]['mean_AQI_NO2'])
  y[i].append(c[i]['mean_AQI_O3'])
  y[i].append(c[i]['mean_AQI_SO2'])
## pie chart
pieChart = html.Div([
     # home page text
    
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib",style={'color':'white'}),
                dcc.Link('Line Chart', href="/line-chart",style={'color':'white'}),
                dcc.Link('Bar Chart', href="/bar-chart",style={'color':'white'}),
                dcc.Link('Pie Chart', href="/pie-chart",style={'color':'white'}),
                dcc.Link('Scatter Chart', href="/scatter-chart",style={'color':'white'}),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-info',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('Pie Chart',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                html.Span('Đây là dạng biểu đồ thường được dùng để vẽ các biểu đồ liên quan đến cơ cấu, tỷ lệ các thành phần trong một tổng thể chung hoặc cũng có thể vẽ biểu đồ tròn khi tỷ lệ % trong bảng số liệu cộng lại tròn 100.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                html.Span('Pie chart (biểu đồ tròn) được sử dụng khi cần biểu diễn dữ liệu dưới dạng %. Sử dụng để thể hiện tỷ lệ % của AQI trung bình ở Mỹ của các loại khí theo từng năm.'
                ,style={'margin-left': '30px'})
            ]),
           html.Div([
                  html.Br(),html.Br(),
            ]),
            html.Div('Chọn năm'),
            html.Div([
                
                html.Div([ dcc.Dropdown(id='dropdown2', options=[
            {'label': '2000', 'value': '2000'},
            {'label': '2001', 'value': '2001'},
            {'label': '2002', 'value': '2002'},
            {'label': '2003', 'value': '2003'},
            {'label': '2004', 'value': '2004'},
            {'label': '2005', 'value': '2005'},
            {'label': '2006', 'value': '2006'},
            {'label': '2007', 'value': '2007'},
            {'label': '2008', 'value': '2008'},
            {'label': '2009', 'value': '2009'},
            {'label': '2010', 'value': '2010'},
            {'label': '2011', 'value': '2011'},
            {'label': '2012', 'value': '2012'},
            {'label': '2013', 'value': '2013'},
            {'label': '2014', 'value': '2014'},
            {'label': '2015', 'value': '2015'},
            {'label': '2016', 'value': '2016'},
          ], placeholder="chon nam",
            value='2000'),
    dcc.Graph(id='graph-court2')
                ],style={'padding-right': '5px','padding-left': '5px'})
            ]),
        ],className='col-9 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
    ], className = 'row')
], className='container')
@app.callback(Output('graph-court2', 'figure'), 
              [Input('dropdown2', 'value')])

def update_graph2(selected_value):
  docs =db.collection(u'pie_and_line_mean_AQI_2000_2016').stream()
  c=[]
  for doc in docs:
    c.append(doc.to_dict())
    year.append(doc.id)
  y = [list() for x in range(17)]
  for i in range(17):
    sum=c[i]['mean_AQI_CO']+c[i]['mean_AQI_NO2']+c[i]['mean_AQI_O3']+c[i]['mean_AQI_SO2']
    y[i].append(c[i]['mean_AQI_CO']/sum)
    y[i].append(c[i]['mean_AQI_NO2']/sum)
    y[i].append(c[i]['mean_AQI_O3']/sum)
    y[i].append(c[i]['mean_AQI_SO2']/sum)
  Air = ['CO', 'NO2', 'O3','SO2']
  fig = go.Figure()
  if selected_value ==  '2000':
    fig.add_trace(go.Pie(labels=Air, values=y[0], name="Trung bình khínam2000"))

  elif selected_value ==  '2001':
    fig.add_trace(go.Pie(labels=Air, values=y[1], name="Trung bình khínam2001"))

  elif selected_value ==  '2002':
    fig.add_trace(go.Pie(labels=Air, values=y[2], name="Trung bình khínam2002"))

  elif selected_value ==  '2003':
    fig.add_trace(go.Pie(labels=Air, values=y[3], name="Trung bình khínam2003"))

  elif selected_value ==  '2004':
    fig.add_trace(go.Pie(labels=Air, values=y[4], name="Trung bình khínam2004"))

  elif selected_value ==  '2005':
    fig.add_trace(go.Pie(labels=Air, values=y[5], name="Trung bình khínam2005"))

  elif selected_value ==  '2006':
    fig.add_trace(go.Pie(labels=Air, values=y[6], name="Trung bình khínam2006"))
 
  elif selected_value ==  '2007':
    fig.add_trace(go.Pie(labels=Air, values=y[7], name="Trung bình khínam2007"))

  elif selected_value ==  '2008':
    fig.add_trace(go.Pie(labels=Air, values=y[8], name="Trung bình khínam2008"))
  
  elif selected_value ==  '2009':
    fig.add_trace(go.Pie(labels=Air, values=y[9], name="Trung bình khínam2009"))

  elif selected_value ==  '2010':
    fig.add_trace(go.Pie(labels=Air, values=y[10], name="Trung bình khínam2010"))

  elif selected_value ==  '2011':
    fig.add_trace(go.Pie(labels=Air, values=y[11], name="Trung bình khínam2011"))
  elif selected_value ==  '2012':
    fig.add_trace(go.Pie(labels=Air, values=y[12], name="Trung bình khínam2012"))
  elif selected_value ==  '2013':
    fig.add_trace(go.Pie(labels=Air, values=y[13], name="Trung bình khínam2013"))
   
  elif selected_value ==  '2014':
    fig.add_trace(go.Pie(labels=Air, values=y[14], name="Trung bình khínam2014"))
)
  elif selected_value ==  '2015':
    fig.add_trace(go.Pie(labels=Air, values=y[15], name="Trung bình khínam2015"))

  elif selected_value ==  '2016':
    fig.add_trace(go.Pie(labels=Air, values=y[16], name="Trung bình khínam2016"))

  return fig


#scatter charts
scatterChart = html.Div([
     # home page text
    
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib",style={'color':'white'}),
                dcc.Link('Line Chart', href="/line-chart",style={'color':'white'}),
                dcc.Link('Bar Chart', href="/bar-chart",style={'color':'white'}),
                dcc.Link('Pie Chart', href="/pie-chart",style={'color':'white'}),
                dcc.Link('Scatter Chart', href="/scatter-chart",style={'color':'white'}),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-info',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('Scatter chart',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                html.Span('Biểu đồ phân tán trong tiếng Anh là Scatter diagram. Biểu đồ phân tán thực chất là một đồ thị biểu hiện mối tương quan giữa nguyên nhân và kết quả hoặc giữa các yếu tố ảnh hưởng đến chất lượng.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                html.Span('Scatter chart (biểu đồ phân tán) thường được sử dụng để thể hiện mối tương quan giữa các yếu tố trên đồ thị. Sử dụng để nghiên cứu sự tương quan giữa các loại khí.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                  html.Br(),html.Br()
            ]),
            
               
                html.Div('Biểu đồ scatter thể hiện sự tương quan giữa các loại khí',style={'font-size':'20px','text-align':'center'}),
                html.Div([
                   html.Img(src=Image.open('./scatter/scatter.jpg'), className='col -5'),
               
                   html.Img(src=Image.open('./scatter/scatter2.jpg'), className='col -5'),       
                ],className='row'),
                 html.Div([
                      html.Img(src=Image.open('./scatter/scatter3.jpg'), className='col -5'),
                     html.Img(src=Image.open('./scatter/scatter4.jpg'), className='col -5'),
                         
                 ],className ='row'),
                    
                   html.Div([
                             html.Img(src=Image.open('./scatter/scatter5.jpg'), className='col -5'),  
                                html.Img(src=Image.open('./scatter/scatter1.jpg'), className='col -5'),
                   ],className ='row')
             

         
    
        ],className='col-9 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
    ], className = 'row')
], className='container')





##---------------------------------------------------------
DataAnalysis = html.Div([
     # home page text
    html.Div([
        html.Div([
            html.Div([
                html.Div('DATA ANALYSIS', style={'font-size':'60px','text-align':'center','font-weight': 'bold','color':'white'}),
                dcc.Link('Home Page', href="/",style={'font-size':'30px','text-align':'center','color':'white'}),
            ], style={'text-align':'center'}, className='col bg-info'),
            html.Br(),
            html.Br(),
            html.Div([
                 html.Span('- Dữ liệu thu thập được:',style={'font-weight': 'bold','font-size':'18px'}),
                 html.Div('-	Dữ liệu thứ cấp: Tất cả', style={'margin-left': '30px'})]
               )
            ]),
             html.Div([
                 html.Span('- Định nghĩa các biến số:',style={'font-weight': 'bold','font-size':'18px'}),
                 html.Div([
                          html.Div('State CodeCode: Mã tiểu bang'),
                          html.Div('Country Code : Mã quốc gia '),
                          html.Div('Sit Num: Số trang wed'),
                          html.Div('State : Tiểu bang'),
                          html.Div('Country:	Quốc gia'),
                          html.Div('City:	Thành phố'),
                          html.Div('Date Local:	Ngày địa phương'),
                          html.Div('NO2 Units:	Đơn vị khí NO2'),
                          html.Div('NO2 Mean:	Giá trị trung bình NO2'),
                          html.Div('NO2 1st Max Value	Giá: trị NO2 tối đa đầu tiên'),
                          html.Div('NO2 1st Max Hour	Giá: trị tối đa giờ đầu tiên của NO2'),
                          html.Div('NO2 AQI:	Giá trị AQI của khí NO2'),
                          html.Div('O3 Units:	Đơn vị khí O3'),
                          html.Div('O3 Mean:	Giá trị trung bình O3'),
                          html.Div('O3 1st Max Value:	Giá trị O3 tối đa đầu tiên'),
                          html.Div('O3 1st Max Hour:	Giá trị tối đa giờ đầu tiên của O3'),
                          html.Div('O3 AQI:	Giá trị AQI của khí O3'),
                          html.Div('SO2 Units:	Đơn vị khí SO2'),
                          html.Div('SO2 Mean:	Giá trị trung bình O3'),
                          html.Div('SO2 1st Max Value:	Giá trị SO2 tối đa đầu tiên'),
                          html.Div('SO2 AQI:	Giá trị AQI của khí SO2'),
                          html.Div('CO Units:	Đơn vị khí CO'),
                          html.Div('CO Mean:	Giá trị trung bình CO'),
                          html.Div('CO 1st Max Value:	Giá trị CO tối đa đầu tiên'),
                          html.Div('CO 1st Max Hour:	Giá trị tối đa giờ đầu tiên của CO'),
                          html.Div('CO AQI: Giá trị AQI của khí CO'),]
                      
                          , style={'margin-left': '30px'})  
            ]),
             html.Div([
                 html.Span('- Dạng dữ liệu:',style={'font-weight': 'bold','font-size':'18px'}),
                 html.Div([
                           html.Div('Định tính: State Code, Country Code, Site Num, Address, State, Country, City, Date Local, NO2 Units, O3 Units, SO2 Units, CO Units. '),
                           html.Div('Định lượng: c: NO2 Mean, NO2 1st Max Value, NO2 1st Max Hour, NO2 AQI, O3 Mean, O3 1st Max Value, O3 1st Max Hour, O3 AQI, SO2 Mean, SO2 1st Max Value, SO2 1st Max Hour, SO2 AQI, CO Mean, CO 1st Max Value, CO 1st Max Hour, CO AQI')]
                          ,style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Thang do cho dữ liệu: ',style={'font-weight': 'bold','font-size':'18px'}),
                 html.Div([
                          html.Div('Thang do định danh (norminal):State Code, Country Code, State, Country, City'),
                          html.Div('Thang đo khoảng( (interval): Date Local, NO2 Mean, NO2 1st Max Value, NO2 1st Max Hour, NO2 AQI, O3 Mean, O3 1st Max Value, O3 1st Max Hour, O3 AQI, SO2 Mean, SO2 1st Max Value, SO2 1st Max Hour, SO2 AQI, CO Mean, CO 1st Max Value, CO 1st Max Hour, CO AQI')]
             ,style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Kiểu dữ liệu: ',style={'font-weight': 'bold','font-size':'18px'}),
                 html.Div([
                          html.Div('String: Address, State, Country, City,  NO2 Units, O3 Units, SO2 Units, CO Units. '),
                          html.Div('Integer: State Code, Country Code, Site Num, NO2 1st Max Hour, NO2 AQI, O3 1st Max Hour, O3 AQI, SO2 1st Max Hour, SO2 AQI, , CO 1st Max Hour, CO AQI '),
                          html.Div('Date: Date Local'),
                           html.Div('Float: NO2 Mean, NO2 1st Max Value, O3 Mean, O3 1st Max Value, SO2 Mean, SO2 1st Max Value, CO Mean, CO 1st Max ValueValue'),]
                          ,style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Mục tiêu nghiên cứu: ',style={'font-weight': 'bold','font-size':'18px'}),
                 html.Div('-	Nghiên cứu về mức độ ô nhiễm môi trường giữa các tiểu bang ',style={'margin-left': '30px'})]
                 )
            ,
             html.Div([
                 html.Span('- Phạm vi nghiên cứu:',style={'font-weight': 'bold','font-size':'18px'}),
                 html.Div('-	17 năm (Từ năm 2000 – 2016)',style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Nhóm biến tham gia quá trình nghiên cứu:',style={'font-weight': 'bold','font-size':'18px'}),
                 html.Div('-	State Code, Country Code, Site Num, Address, State, Country, City, Date Local, NO2 Units, NO2 Mean, NO2 1st Max Value, NO2 1st Max Hour, NO2 AQI, O3 Units, O3 Mean, O3 1st Max Value, O3 1st Max Hour, O3 AQI, SO2 Units, SO2 Mean, SO2 1st Max Value, SO2 1st Max Hour, SO2 AQI, CO Units, CO Mean, CO 1st Max Value, CO 1st Max Hour, CO AQI. ',style={'margin-left': '30px'})]
                 )
  
        ],className='col-12 bg-light',style={'border-radius': '3px','padding': '20px 40px'})

])

##---------------------------------------------------------
# and this code to transfer to another link
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/matplotlib':
        return matplotlib
    elif pathname == '/line-chart':
        return lineChart
    elif pathname =='/bar-chart':
        return barChart
    elif pathname =='/pie-chart':
        return pieChart
    elif pathname =='/scatter-chart':
        return scatterChart
    elif pathname =='/data-analysis':
        return DataAnalysis
    else:
        return main

server = app.server

if __name__ == "__main__":
    app.run_server()
