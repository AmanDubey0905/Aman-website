from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

def get_rag_chain():
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory="vector_db",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever()

    llm = ChatOpenAI(model="gpt-4o-mini")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
