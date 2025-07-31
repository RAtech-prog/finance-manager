import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.main import app
from src.models.user import db
from src.models.transaction import Category

def seed_categories():
    """Adiciona categorias padrão ao banco de dados"""
    
    # Categorias de despesas
    expense_categories = [
        {'name': 'Alimentação', 'type': 'expense', 'color': '#ef4444'},
        {'name': 'Transporte', 'type': 'expense', 'color': '#f97316'},
        {'name': 'Moradia', 'type': 'expense', 'color': '#eab308'},
        {'name': 'Saúde', 'type': 'expense', 'color': '#22c55e'},
        {'name': 'Educação', 'type': 'expense', 'color': '#3b82f6'},
        {'name': 'Lazer', 'type': 'expense', 'color': '#8b5cf6'},
        {'name': 'Roupas', 'type': 'expense', 'color': '#ec4899'},
        {'name': 'Serviços', 'type': 'expense', 'color': '#6b7280'},
        {'name': 'Outros', 'type': 'expense', 'color': '#64748b'}
    ]
    
    # Categorias de receitas
    income_categories = [
        {'name': 'Salário', 'type': 'income', 'color': '#10b981'},
        {'name': 'Freelance', 'type': 'income', 'color': '#059669'},
        {'name': 'Investimentos', 'type': 'income', 'color': '#047857'},
        {'name': 'Vendas', 'type': 'income', 'color': '#065f46'},
        {'name': 'Outros', 'type': 'income', 'color': '#064e3b'}
    ]
    
    all_categories = expense_categories + income_categories
    
    with app.app_context():
        # Verificar se já existem categorias
        existing_categories = Category.query.count()
        if existing_categories > 0:
            print(f"Banco já possui {existing_categories} categorias. Pulando seed.")
            return
        
        # Adicionar categorias
        for cat_data in all_categories:
            category = Category(**cat_data)
            db.session.add(category)
        
        try:
            db.session.commit()
            print(f"Adicionadas {len(all_categories)} categorias padrão ao banco de dados.")
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao adicionar categorias: {e}")

if __name__ == '__main__':
    seed_categories()

