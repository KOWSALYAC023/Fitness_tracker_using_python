def calculate_nutrients(food_items):
    result = food_data[food_data['Food_Item'].isin(food_items)].sum()
    return {
        'Calories': result['Calories'],
        'Proteins': result['Proteins'],
        'Fats': result['Fats'],
        'Carbohydrates': result['Carbohydrates']
    }
