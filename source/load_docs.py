from langchain_community.document_loaders import TextLoader

def load_documents():
    documents = []

    documents += TextLoader(
        "policy documentation/refund_policy.txt",
        encoding="utf-8"
    ).load()

    documents += TextLoader(
        "policy documentation/cancellation_policy.txt",
        encoding="utf-8"
    ).load()

    documents += TextLoader(
        "policy documentation/Shipping & Delivery Policy.txt",
        encoding="utf-8"
    ).load()

    return documents
    