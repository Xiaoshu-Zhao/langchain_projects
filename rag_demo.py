from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain


# load the doc
loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
docs = loader.load()

# init the llm
llm = ChatOpenAI(
    base_url="https://api.chatanywhere.tech/v1",
    api_key="sk-Cz9WaW2zKjJj4pzLmuxMPcPiT9SUcC8VHvwkm5LJExI0cXiZ",
)


# init embedding model
embeddings = OpenAIEmbeddings(
    openai_api_base='https://api.chatanywhere.tech/v1'
)

# init the vector DB
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)


# init the prompt
prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)



# start retriever
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)


response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
# print(response["answer"])
print(response)
