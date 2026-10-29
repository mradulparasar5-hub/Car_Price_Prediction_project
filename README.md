# Used Car Price Prediction

Machine learning project that predicts the price of a used car (Quikr dataset) and serves it through a Flask web app.

## Files
| File | Purpose |
|---|---|
| `car_price_prediction.ipynb` | Data cleaning, EDA, model comparison, tuning, saving the model |
| `quikr_car.csv` / `cleaned_car.csv` | Raw and cleaned data |
| `model.joblib`, `metadata.json` | Saved model and the lists used by the web form |
| `app.py` | Flask server with the `/predict` API |
| `templates/index.html`, `static/style.css`, `static/script.js` | Web page |

## Run it
```
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 in your browser.

To re-train, open the notebook (`jupyter notebook`) and run all cells; it regenerates `model.joblib` and `metadata.json`.
