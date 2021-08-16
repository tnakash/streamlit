import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('Display Image')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'

left_column, right_column = st.columns(2)
button = left_column.button('ボタン')
if button:
    right_column.write('ここは右からむ')

expander1 = st.expander('なっているんですか？')
expander1.write('なってます')
expander2 = st.expander('なっているんですか？')
expander2.write('なってません')

# text = st.text_input('あなたの趣味を教えてください')
# '趣味: ', text

# option = st.selectbox(
#     'あなたの好きな数字を教えてください', 
#     list(range(1,11))
# )
# '好きな数字: ', option

# condition = st.slider('あなたの今の調子は？', 0, 100, 30)
# 'コンディション: ', condition

# if st.checkbox('画像を表示'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='この世界からの…卒業', use_column_width=True)

# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

# st.write(df)

# st.table(df.style.highlight_max(axis=0))

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns=['lat','lon']
# )

# st.map(df)


# """
# # 章
# ## 節
# ### 項

# ``` python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """