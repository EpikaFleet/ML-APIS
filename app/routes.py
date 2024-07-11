from flask import request, jsonify
from app import app
from db import fetch_data_from_db

import pandas as pd

optimal_values_df = pd.read_csv('./DataSets/OptimalValues.csv')

def calculate_mape(input_qty, optimal_value):
    return abs((input_qty - optimal_value) / optimal_value) * 100

@app.route('/calculate_distance', methods=['POST'])
def calculate_distance():
    data = request.json
    part_id = data.get('part_id')
    input_qty = data.get('qty')

    optimal_value_row = optimal_values_df[optimal_values_df['part_id'] == part_id]
    
    if optimal_value_row.empty:
        return jsonify({'error': 'part_id not found'}), 404

    optimal_value = optimal_value_row['optimal_value'].values[0]

    mape = calculate_mape(input_qty, optimal_value)

    return jsonify({
        'part_id': part_id,
        'input_qty': input_qty,
        'optimal_value': optimal_value,
        'distance': mape
    })
    
def load_rules():
    rules = pd.read_csv('./DataSets/Rules.csv')
    rules['antecedents'] = rules['antecedents'].apply(eval).apply(frozenset)
    rules['consequents'] = rules['consequents'].apply(eval).apply(frozenset)
    return rules

def recommend_parts(existing_parts, rules):
    recommended_parts = set()
    for index, row in rules.iterrows():
        antecedents = row['antecedents']
        if antecedents.issubset(existing_parts):
            recommended_parts.update(row['consequents'])

    recommended_parts.difference_update(existing_parts)
    return list(recommended_parts)

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    if not request.json or 'invoice_id' not in request.json or 'part_ids' not in request.json:
        return jsonify({'error': 'Invalid request format. Required fields: invoice_id, part_ids'}), 400
    
    rules = load_rules()
    existing_parts = set(request.json['part_ids'])
    print(existing_parts)
    recommendations = recommend_parts(existing_parts, rules)
    recommended_parts = fetch_data_from_db(recommendations)
    return jsonify({'recommended_parts': recommended_parts})