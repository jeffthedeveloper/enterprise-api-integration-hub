import firebase_admin
from firebase_admin import credentials, firestore

# Inicializando o Firebase
cred = credentials.Certificate(""path/to/your/firebase/credentials.json"")
firebase_admin.initialize_app(cred)

# Conectando ao Firestore
db = firestore.client()

# Função para adicionar dados no Firestore
def add_data_to_firestore(collection_name, data):
    doc_ref = db.collection(collection_name).add(data)
    print(f'Dados adicionados com sucesso: {doc_ref.id}')

# Exemplo de uso
data = {
    'name': 'João',
    'age': 30
}
add_data_to_firestore('users', data)
