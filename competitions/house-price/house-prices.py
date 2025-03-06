import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

train = pd.read_csv('train.csv')

test = pd.read_csv('test.csv')

features = ["OverallQual", "GrLivArea", "TotalBsmtSF", "1stFlrSF", "GarageCars", 
            "GarageArea", "Neighborhood", "YearBuilt", "YearRemodAdd", "ExterQual",
            "BsmtQual", "KitchenQual", "Fireplaces", "LotArea"]

X = train[features]
X = pd.get_dummies(X)
X.fillna(0, inplace=True)

y = train["SalePrice"]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)



rf_model = RandomForestRegressor(n_estimators=200, max_depth=20, random_state=1)
rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

error_relativo = (rf_val_mae / y.mean()) * 100
print(f"Error relativo: {error_relativo:.2f}%")
