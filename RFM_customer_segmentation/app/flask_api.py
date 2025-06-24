from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data/rfm_with_segments.csv")

@app.route('/segment', methods=['POST'])
def get_segment():
    data = request.get_json()
    customer_id = str(data.get('CustomerID', ''))
    customer = df[df['CustomerID'].astype(str) == customer_id]
    if customer.empty:
        return jsonify({"error": "Customer ID not found"}), 404
    result = customer.iloc[0].to_dict()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
