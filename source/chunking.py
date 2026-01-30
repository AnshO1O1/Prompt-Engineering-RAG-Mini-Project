from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=90,
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_documents(documents)