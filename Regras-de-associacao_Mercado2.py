
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('mercado2.csv', header=None)


# In[3]:


dados.head()


# In[4]:


# Para o algoritmo Apriori do arquivo apyori, os dados devem estar em formato de lista
transacoes = []
for i in range(dados.shape[0]):
    transacoes.append([str(dados.values[i, j]) for j in range(dados.shape[1])])


# In[5]:


transacoes


# In[6]:


# Importando o arquivo com o algoritmo Apriori
from apyori import apriori


# In[13]:


regras = apriori(transacoes, min_support=0.003, min_confidence=0.5, min_lift=3, min_length=2)


# In[14]:


resultados = list(regras)


# In[15]:


len(resultados)


# In[ ]:


resultados


# In[ ]:


resultados2 = [list(x) for x in resultados]
resultados2


# In[ ]:


resultadoFormatado = []
for j in range(0,len(resultados)):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])


# In[ ]:


resultadoFormatado

